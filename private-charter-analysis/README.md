✈️ Private Charter Profitability Analysis (SQL Project)
📊 Project Overview

This project analyzes private charter flight operations to evaluate revenue, cost, and profitability across different routes and aircraft models.

The objective is to identify high-performing areas of the business and support data-driven decision-making.

🎯 Business Questions
Which routes generate the highest profit?
Which aircraft models are the most profitable?
What are the total revenue, cost, and profit?
How many bookings are completed vs canceled?
🧠 Key Insights
🥇 Most profitable route: FLL–CUN ($12,742 profit)
✈️ Top aircraft: Challenger 604 ($56,646 profit)
💰 Total revenue: $1,932,364
📉 Total cost: $1,644,761
📊 Total profit: $287,603
📊 Overall Financial Summary

📌 Aggregated totals from completed bookings:

📈 Top Routes by Profit ![Top Routes](top_routes.png)

📌 The table below shows the most profitable routes based on completed bookings:

✈️ Top Aircraft by Profit ![Top Aircraft](top_aircraft.png)

📌 The table below ranks aircraft models by total profit:

📊 Booking Status Distribution  ![Booking Status](

📌 Total number of bookings by status:

💡 Most bookings are completed, indicating strong operational efficiency.

🧮 SQL Queries
💰 Financial Summary
SELECT
    SUM(price_charged_usd) AS total_revenue,
    SUM(operator_cost_usd) AS total_cost,
    SUM(price_charged_usd - operator_cost_usd) AS total_profit
FROM bookings
WHERE booking_status = 'Completed';
📈 Top Routes by Profit
SELECT
    departure_airport,
    arrival_airport,
    SUM(price_charged_usd - operator_cost_usd) AS total_profit
FROM bookings
WHERE booking_status = 'Completed'
GROUP BY departure_airport, arrival_airport
ORDER BY total_profit DESC;


✈️ Top Aircraft by Profit
SELECT
    aircraft_model,
    SUM(price_charged_usd - operator_cost_usd) AS total_profit
FROM bookings
WHERE booking_status = 'Completed'
GROUP BY aircraft_model
ORDER BY total_profit DESC;
📊 Booking Status Count
SELECT
    booking_status,
    COUNT(*) AS total_bookings
FROM bookings
GROUP BY booking_status;
🛠️ Tools & Skills
SQL (Aggregations, GROUP BY)
Data Analysis & Business Metrics
Profitability Analysis
Data Interpretation
Data Visualization (Tables & Charts)

📌 Conclusion

This analysis highlights key profitability drivers in private charter operations. By focusing on high-performing routes and aircraft, stakeholders can optimize pricing strategies, reduce costs, and improve overall efficiency.



































