# unstructured_data_ETL_pipeline
# **MongoDB to SQL Server ETL Pipeline**

This project implements a robust **ETL (Extract, Transform, Load)** pipeline to transfer data from a **MongoDB** collection to a **SQL Server** database. It tracks and logs each step of the pipeline for auditing purposes. The structure is modular, ensuring ease of maintenance and scalability.

## **Table of Contents**

- [**Overview**](#overview)
- [**Project Structure**](#project-structure)
- [**Prerequisites**](#prerequisites)
- [**Setup Instructions**](#setup-instructions)
- [**Usage**](#usage)
- [**Logging Mechanism**](#logging-mechanism)
- [**Notes**](#notes)
- [**Troubleshooting**](#troubleshooting)
- [**Contributing**](#contributing)
- [**License**](#license)

## **Overview**

This pipeline:
- Extracts data from a MongoDB collection (`practice_data.project`).
- Transforms and cleans the data using `pandas`.
- Loads the data into a table in SQL Server.
- Logs metadata for each step into a CSV (`meta_data.csv`) and then uploads it to a `log_table` in SQL Server.

---

## **Project Structure**

![image](https://github.com/user-attachments/assets/71446029-1b66-4ccc-aa9f-c012b1faec24)


---

## **Prerequisites**

- Python 3.x
- MongoDB (local instance at `localhost:27017`)
- SQL Server with proper ODBC driver installed
- ODBC connection string configuration
- Packages:
  - `pandas`
  - `sqlalchemy`
  - `pymongo`
  - `pyodbc`

---

## **Setup Instructions**

1. **Install Python Packages:**

   ```bash
   pip install pandas sqlalchemy pymongo pyodbc

## **Create a config.config file with the following content**

[ssms]
DRIVER=ODBC Driver 17 for SQL Server
SERVER=YOUR_SERVER_NAME
DATABASE=YOUR_DATABASE_NAME
UID=YOUR_USERNAME
PWD=YOUR_PASSWORD
