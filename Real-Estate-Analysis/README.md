# 🏠 Real Estate Commercial Analysis (Power BI)

> ⚠️ Note: The dashboard visuals are presented in Spanish as part of a real-world business scenario.

## 📌 Project Overview
This project analyzes the commercial performance of a real estate company using a data-driven approach, focusing on sales trends, customer segmentation, and retention through cohort analysis.

## 🎯 Business Questions
* Which property types generate the highest revenue?
* How has the company grown compared to the previous year (YoY)?
* Which sales channels (Brokers vs. Direct) are most effective?
* What is the customer retention rate based on their first purchase month (Cohort Analysis)?

## 🗂️ Dataset
* **hecho_ventas_propiedades:** The fact table containing all transactional sales records, prices, and dates.
* **dim_clientes:** Dimension table with buyer details and segmentation.
* **dim_propiedades:** Dimension table containing property characteristics.
* **dim_fecha:** A dedicated calendar table for advanced Time Intelligence calculations.

## 🛠️ Tools & Skills Used
* Power BI (data visualization & dashboard design)
* DAX (time intelligence, cohort analysis, advanced measures)
* Power Query (data cleaning and transformation)

## 📊 Key Metrics
* **Total Revenue:** ~$6bn with a **111.14% Year-over-Year growth**.
* **Top Property Type:** Houses ("Casa") are the top-performing property type in terms of revenue.
* **Sales Force:** Brokers ("Corredores") drive 72.8% of the total revenue.
* **Retention:** The October 2024 cohort showed a peak in customer recurrence (26.5%).

## ✅ Key Learnings
* Developed complex DAX formulas to calculate business growth and retention.
* Designed an executive-level interactive dashboard for stakeholders.
* Applied Cohort Analysis to understand long-term customer behavior.

## 🧩 Data Model
The data model follows a star schema:
- Fact table: sales transactions
- Dimension tables: customers, properties, and date

Relationships are designed with one-to-many cardinality and single-direction filtering to ensure accurate aggregations.


## 📸 Dashboard Visuals
![Dashboard Overview](./Overview.png)
![Commercial Analysis](./Analisis%20Comercial.png)
![Cohort Analysis](./Cohortes.png)

