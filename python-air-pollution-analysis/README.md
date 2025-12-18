# Project 3: Air Pollution Analysis by Location (Python)

## 📌 Overview
This project analyzes air pollution (PM2.5) measurements to identify which locations have the highest number of records and their average pollution levels.

The goal is to understand monitoring coverage and pollution intensity across different locations using Python and Pandas.

## 🧠 Business Question
- Which locations have the highest number of pollution measurements?
- What is the average PM2.5 level for each location?

## 🗂️ Dataset
- `openaq_pm25.csv`: Air quality measurements collected from sensors around the world.

Key columns used:
- `location`: Sensor location
- `value`: PM2.5 concentration (µg/m³)

## 🛠 Tools Used
- Python
- Pandas

## 🧮 Analysis Steps
- Removed duplicate records
- Converted pollution values to numeric format
- Removed missing values
- Grouped data by location
- Calculated:
  - Average pollution level
  - Number of records per location
- Sorted results by number of records and location name

## 📈 Key Metrics
- Average PM2.5 concentration per location
- Total number of measurements per location

## ✅ Key Learnings
- Grouping and aggregating data with Pandas
- Sorting data using multiple criteria
- Cleaning real-world datasets
- Writing clear and readable Python code

