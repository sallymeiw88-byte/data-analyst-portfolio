✈️ Private Charter Profitability Analysis (SQL Project)

📊 Project Overview

This project analyzes private charter flight operations to evaluate financial performance, route profitability, aircraft efficiency, customer segment dynamics, and manufacturer performance.
The objective is to identify high-margin business areas and support strategic decision-making using relational database queries (SQL).

🎯 Business Questions

- What are the company's total revenue, total cost, and total profit?
- Which aircraft models generate the highest profit?
- Which flight routes are the most profitable?
- Which customer type generates the highest revenue?
- Which aircraft manufacturer generates the highest total profit?

🧠 Key Insights

🥇 Top Route: Teterboro to Cancun ($935,844 profit)
✈️ Top Aircraft: Gulfstream G450 ($4,541,353.1 profit | 181 flights)
🏭 Top Manufacturer: Bombardier ($8,060,980.1 profit | 314 flights)
👥 Primary Revenue Driver: Entertainment Segment ($7,495,027.5 revenue | 207 flights)
💰 Total Profitability: $25,338,506.3 Total Profit on $36,116,435.2 Total Revenue

📊 Visualizations & Results

📌 Financial Overview
![Financial Summary](financial_summary.png)

📌 Profitability by Aircraft Model
![Top Aircraft](top_aircraft.png)

📌 Top Routes Analysis
![Top Routes](top_routes.png)

📌 Customer Segment Revenue Breakdown
![Customer Analysis](customer_analysis.png)

📌 Manufacturer Profit Performance
![Manufacturer Analysis](manufacturer_analysis.png)

🧮 SQL Queries

```sql
-- 1. Financial Summary
SELECT
    SUM(Revenue) AS Total_Revenue,
    SUM(Total_Cost) AS Total_Cost,
    SUM(Profit) AS Total_Profit
FROM private_charter_flights_dataset;

-- 2. Top Aircraft by Profit
SELECT
    Aircraft_Model,
    COUNT(*) AS Total_Flights,
    SUM(Revenue) AS Total_Revenue,
    SUM(Profit) AS Total_Profit
FROM private_charter_flights_dataset
GROUP BY Aircraft_Model
ORDER BY Total_Profit DESC;

-- 3. Top Routes by Profit
SELECT
    Origin,
    Destination,
    COUNT(*) AS Total_Flights,
    SUM(Profit) AS Total_Profit
FROM private_charter_flights_dataset
GROUP BY Origin, Destination
ORDER BY Total_Profit DESC;

-- 4. Customer Analysis
SELECT
    Customer_Type,
    COUNT(*) AS Total_Flights,
    SUM(Revenue) AS Total_Revenue,
    SUM(Profit) AS Total_Profit
FROM private_charter_flights_dataset
GROUP BY Customer_Type
ORDER BY Total_Revenue DESC;

-- 5. Manufacturer Analysis (JOIN)
SELECT
    a.Manufacturer,
    COUNT(*) AS Total_Flights,
    SUM(f.Revenue) AS Total_Revenue,
    SUM(f.Profit) AS Total_Profit
FROM private_charter_flights_dataset f
JOIN aircraft_dimension a
  ON f.Aircraft_Model = a.Aircraft_Model
GROUP BY a.Manufacturer
ORDER BY Total_Profit DESC;

🛠️ Tools & Skills

* 💻 **SQL**: Aggregations (`SUM`, `COUNT`), Grouping (`GROUP BY`), Sorting (`ORDER BY`), Relational Joins (`INNER JOIN`).
* 📊 **Data Analytics**: Profitability Analysis, Revenue Breakdown, Fleet Optimization.
* 🗄️ **Data Modeling**: Relational Table Schemas (Fact & Dimension Tables).

💡 Business Impact

* ✈️ **Fleet Optimization**: Prioritize charter availability and maintenance investment for high-margin aircraft models like Gulfstream G450 and Cessna Citation XLS.
* 🗺️ **Route Planning**: Focus commercial strategies on top-tier international routes such as Teterboro–Cancun and Orlando–Toronto.
* 🎯 **Customer Targeting**: Reallocate marketing budgets toward the Entertainment and Private customer segments to maximize profit margins.
