🌟 Promoting Transparent and Predictable Healthcare Costs for Students

A Fully Automated AWS Data Pipeline + Power BI Dashboard

📌 Project Overview

Students often struggle to understand how much they will pay for medical care because healthcare prices and insurance coverage are unclear. This leads to confusion, stress, and delayed treatment.

Our project solves this problem by building an automated cloud system that processes healthcare claim data and presents it in a simple, easy-to-read dashboard. The system runs end-to-end with minimal manual work and helps students gain clear insights into healthcare costs.

🚀 Key Features

Fully automated AWS pipeline triggered by file upload

Clean and standardized data ready for analysis

Fast SQL querying using Amazon Athena

Interactive Power BI dashboard for simple cost insights

Scalable architecture ready for future real-time and predictive analytics

User-friendly design suitable even for non-technical students

🏗️ Architecture Overview

Our system uses the following AWS services:

Component	Purpose
Amazon S3	Stores raw and processed healthcare data
AWS Lambda	Automatically triggers ETL when a CSV is uploaded
AWS Glue ETL	Cleans, transforms, and prepares data for analytics
Glue Crawler	Updates schema and metadata in the Data Catalog
Amazon Athena	Runs SQL queries on transformed data
Power BI	Displays insights through an interactive dashboard
🔄 End-to-End Data Pipeline Flow

Upload a healthcare CSV file into the S3 source bucket

Lambda detects the upload and triggers the ETL job

AWS Glue cleans and transforms the data

Output is saved as Parquet in the target S3 bucket

Glue Crawler updates the Data Catalog

Athena queries the latest cleaned data

Power BI visualizes the results for easy student understanding

📊 Dashboard Insights

Our Power BI dashboard provides clear visual insights, including:

💰 Total Paid Amount

🧾 Total Billed Amount

👥 Member Count

🏥 Provider Type–Wise Member Count

🩺 Specialty-Wise Member Count

🧬 Diagnosis Trends

📅 Year-Wise Member Count

The dashboard is simple, interactive, and built specifically for student users.

📝 How to Run the System

Upload a new CSV to your S3 source bucket

Wait for the automated pipeline to run (Lambda → Glue → Crawler)

Open Athena and verify the latest data

Refresh Power BI report connected to Athena

View updated insights instantly

👨‍💻 Technologies Used

AWS S3

AWS Lambda

AWS Glue ETL

AWS Glue Crawler

Amazon Athena

Python

Power BI

Parquet & CSV formats

👥 Team Members

Deepak

Trinath

Satish

Kavya

🎯 Project Goal

To empower students with clear, reliable, and predictable healthcare cost information through an automated data engineering solution.

📂 Repository Structure (Suggested)
/scripts          → Lambda + Glue ETL scripts
/data             → Sample CSV or synthetic dataset
/dashboard        → Power BI screenshots or PBIX file
/docs             → Technical report, presentation, diagrams
README.md

🙌 Acknowledgements

AWS Documentation

Power BI Community

CRISP-DM Framework

Instructors and Teaching Assistants
