**Weather and Air Quality ETL Pipeline**


**Project Overview**

This project demonstrates an ETL (Extract, Transform, Load) pipeline that integrates weather and air quality data for a specified city. The data is extracted from external APIs, transformed (cleaned and processed), and loaded into a PostgreSQL database. The goal of this project is to provide a clean, well-structured dataset.

**Technologies Used**


Programming Language: Python

Database: PostgreSQL

Data Sources:

Weather API: VisualCrossing
Python Libraries:

requests: For interacting with APIs.
pandas: For data manipulation and cleaning.
psycopg2: For database interaction.
dotenv: To handle environment variables (API keys, DB credentials).


**ETL Pipeline Breakdown**

*1. Data Extraction*

Weather Data: Collected using the VisualCrossing API. Data includes temperature, humidity, wind speed, and weather conditions.

*2. Data Transformation*

Handle missing data and clean the dataset.
Transforming measurements to correct datatype.

*4. Data Loading*

Store the cleaned and transformed data into a PostgreSQL database.
Database schema include table for weather data.


