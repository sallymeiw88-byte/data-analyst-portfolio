# 🌫️ Air Pollution Analysis by Location (Python)

## 📌 Project Overview
This project analyzes air pollution (PM2.5) measurements to identify which locations have the highest monitoring coverage and their average pollution levels.

The analysis focuses on understanding pollution intensity and data availability across different locations using Python and Pandas.

## 🎯 Business Questions
- Which locations have the highest number of pollution measurements?
- What is the average PM2.5 level for each location?

## 🗂️ Dataset
**openaq_pm25.csv** — Air quality measurements collected from sensors around the world.

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
- Sorted results by record count and location name

## 📊 Key Metrics
- Average PM2.5 concentration per location
- Total number of measurements per location

## ✅ Key Learnings
- Grouped and aggregated data using Pandas
- Cleaned and prepared real-world datasets
- Sorted data using multiple criteria
- Wrote clear, readable, and structured Python code


