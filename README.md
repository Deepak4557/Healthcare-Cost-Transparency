# Promoting Transparent and Predictable Healthcare Costs for Students

## Project Overview
This project aims to help students understand healthcare costs in a clear and simple way.  
Many students avoid or delay medical care because they are unsure how much they will have to pay.
We built an automated data pipeline on AWS that processes healthcare claim data and shows insights
through an interactive Power BI dashboard.

## Architecture
Our solution uses the following AWS services:
- **Amazon S3** – stores raw and transformed data
- **AWS Lambda** – triggers the ETL job when a CSV file is uploaded
- **AWS Glue** – cleans and transforms the data and writes it in Parquet format
- **Glue Crawler** – updates the Data Catalog with the latest schema
- **Amazon Athena** – queries the transformed data
- **Power BI** – visualizes key metrics for students

## Data Pipeline Flow
1. Upload a healthcare claims CSV file into the S3 source bucket.
2. An S3 event triggers a Lambda function.
3. Lambda starts an AWS Glue ETL job.
4. Glue cleans, transforms, and writes data to the target S3 bucket in Parquet format.
5. A Glue Crawler updates the Data Catalog.
6. Athena queries the latest data.
7. Power BI connects to Athena and displays dashboards for students.

## Dashboard Highlights
The Power BI dashboard shows:
- Total paid amount
- Total billed amount
- Member count
- Provider type–wise member count
- Specialty-wise member count
- Diagnosis-wise trends
- Year-wise member count

## How to Run (High Level)
1. Upload a CSV file into the S3 source bucket.
2. Wait for the Lambda + Glue pipeline to complete.
3. Confirm the data in Athena using SQL queries.
4. Refresh your Power BI report connected to Athena.
5. Explore the dashboard visuals.

## Team Members
- Deepak
- Trinath
- Satish
- Kavya

## Technologies Used
- AWS S3, Lambda, Glue, Glue Crawler, Athena
- Python (Glue ETL, Lambda)
- Power BI
- Parquet, CSV
