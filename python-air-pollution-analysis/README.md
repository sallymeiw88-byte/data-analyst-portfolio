# 🌫️ Air Pollution Analysis by Location (Python)

## 📌 Project Overview
This project analyzes global air pollution (PM2.5) data to evaluate pollution levels and data coverage across different locations.

The goal is to transform raw environmental data into structured insights by applying data cleaning, aggregation, and analysis techniques using Python and Pandas.

## 🎯 Business Questions
- Which locations have the highest number of pollution measurements?
- What are the average PM2.5 levels by location?

## 🗂️ Dataset
**openaq_pm25.csv** — Air quality measurements collected from sensors worldwide.

**Key columns used:**
- `location`: Sensor location
- `value`: PM2.5 concentration (µg/m³)

## 🛠 Tools Used
- Python
- Pandas

## 🧮 Analysis Steps
- Removed duplicate records
- Converted pollution values to numeric format
- Handled missing values
- Grouped data by location
- Calculated:
  - Average PM2.5 concentration
  - Number of measurements per location
- Sorted results to identify top locations by data volume

## 📊 Key Metrics
- Identified locations with the highest monitoring activity.
- Compared pollution levels across different regions.
- Highlighted variations in data availability between locations.

## ✅ Key Learnings
- Cleaned and structured raw environmental data.
- Applied grouping and aggregation using Pandas.
- Produced a dataset ready for analysis and reporting.
- Wrote clear, structured, and reproducible Python code.


