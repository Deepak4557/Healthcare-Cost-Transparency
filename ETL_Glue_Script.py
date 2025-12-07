import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue import DynamicFrame
from pyspark.sql import functions as F

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx):
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = glueContext.spark_session.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)

# Read arguments
args = getResolvedOptions(sys.argv, ["JOB_NAME", "S3_SOURCE_PATH", "S3_DESTINATION_PATH"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

DEFAULT_DATA_QUALITY_RULESET = """
Rules = [
    ColumnCount > 0
]
"""

# ---- LOAD CSV ----
input_dyf = glueContext.create_dynamic_frame.from_options(
    format="csv",
    connection_type="s3",
    format_options={"withHeader": True, "separator": ","},
    connection_options={"paths": [args["S3_SOURCE_PATH"]], "recurse": True},
    transformation_ctx="input_dyf"
)

# Convert to DataFrame for transformations
df = input_dyf.toDF()

# ---- REPLACE gs_concat ----
# Create claimlinenumber = CLAIM_ID + '-' + CLAIM_LINE_ID
df = df.withColumn(
    "claimlinenumber",
    F.concat_ws("-", F.col("CLAIM_ID"), F.col("CLAIM_LINE_ID"))
)

# ---- DROP COLUMNS ----
drop_cols = [
    "CH_MEMBER_ID", "CLAIM_ID", "CLAIM_LINE_ID", "CH_EMPLOYER_ID",
    "PROVIDER_NPI", "FACILITY_NPI", "BILLING_PROVIDER_NPI",
    "PROVIDER_TIN", "SERVICE_PROVIDER_ID", "CHECK_NUMBER"
]
df = df.drop(*drop_cols)

# ---- REPLACE gs_now ----
df = df.withColumn(
    "imported_date",
    F.date_format(F.current_timestamp(), "yyyyMMddHHmmss")
)

# Rename field SOURCEFILENAME → SRCFILENAME
df = df.withColumnRenamed("SOURCEFILENAME", "SRCFILENAME")

# Convert back to DynamicFrame
output_dyf = DynamicFrame.fromDF(df, glueContext, "output_dyf")

# ---- SQL query (kept same as original) ----
sql_query = """
select * from source
"""

final_dyf = sparkSqlQuery(
    glueContext,
    query=sql_query,
    mapping={"source": output_dyf},
    transformation_ctx="final_dyf"
)

# ---- DATA QUALITY CHECK ----
EvaluateDataQuality().process_rows(
    frame=final_dyf,
    ruleset=DEFAULT_DATA_QUALITY_RULESET,
    publishing_options={"dataQualityEvaluationContext": "DQ_Context"},
    additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT"}
)

# ---- WRITE PARQUET TO S3 ----
glueContext.write_dynamic_frame.from_options(
    frame=final_dyf,
    connection_type="s3",
    format="glueparquet",
    connection_options={"path": args["S3_DESTINATION_PATH"], "partitionKeys": []},
    format_options={"compression": "snappy"},
    transformation_ctx="output"
)

job.commit()
