# ✈️ Private Charter Profitability Analysis (SQL Project)

## 📊 Project Overview

This project analyzes private charter flight operations to evaluate **revenue, cost, and profitability** across different routes and aircraft models.

The goal is to identify high-performing areas of the business and support **data-driven decision-making**.

---

## 🎯 Business Questions

* Which routes generate the highest profit?
* Which aircraft models are the most profitable?
* What are the total revenue, cost, and profit?
* What percentage of bookings are completed vs canceled?

---

## 🧠 Key Insights

* 🥇 Most profitable route: **FLL–CUN** ($12,742 profit)
* ✈️ Top aircraft: **Challenger 604**
* 📊 Total revenue: **$88,859**
* 💰 Total profit: **$12,742**
* 📦 Total trips analyzed: **5 (top route)**

---

## 📈 Top Routes by Profit

📌 The table below shows the most profitable routes based on completed bookings:

![Top Routes](top_routes.png)

---

## ✈️ Top Aircraft by Profit

📌 The table below ranks aircraft models by total profit:

![Top Aircraft](top_aircraft.png)

---

## 🛠️ Tools & Skills

* SQL (Data Aggregation: `SUM`, `COUNT`)
* Business Metrics (Revenue, Cost, Profit)
* Data Analysis
* Data Interpretation

---

## 🧾 SQL Queries

### Top Routes by Profit

```sql
SELECT 
    route,
    COUNT(*) AS trips,
    SUM(price_charged_usd) AS revenue,
    SUM(price_charged_usd - operator_cost_usd) AS profit
FROM bookings
WHERE booking_status = 'Completed'
GROUP BY route
ORDER BY profit DESC;
```

### Top Aircraft by Profit

```sql
SELECT 
    aircraft_model,
    COUNT(*) AS trips,
    SUM(price_charged_usd) AS revenue,
    SUM(price_charged_usd - operator_cost_usd) AS profit
FROM bookings
WHERE booking_status = 'Completed'
GROUP BY aircraft_model
ORDER BY profit DESC;
```

---

## 📂 Dataset

* Source: Simulated dataset (for analysis purposes)
* Rows: 200
* Columns: 14
* Description: Flight bookings including route, aircraft model, revenue, and cost

---

## 💡 Business Impact

* Identified high-profit routes to prioritize operations
* Highlighted most efficient aircraft models
* Supports pricing strategy and route optimization
* Helps reduce focus on low-profit routes

---



