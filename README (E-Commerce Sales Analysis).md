# 📊 E-Commerce Sales Analysis

## 📌 Overview
This project analyzes an e-commerce sales dataset to extract meaningful insights about sales performance, customer behavior, and product trends.

It demonstrates a complete data analysis workflow including data cleaning, transformation, visualization, and interpretation using Python.

---

## 🎯 Objectives
- Analyze overall sales distribution  
- Identify top-performing products  
- Understand customer purchasing patterns  
- Visualize monthly sales trends  
- Detect high and low sales periods  

---

## 🛠️ Tech Stack
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

---

## 📂 Dataset Description
The dataset contains:
- Product details  
- Customer information  
- Transaction date  
- Quantity and price  

---

## 🔍 Project Workflow

### 1. Data Cleaning
- Removed missing values  
- Dropped duplicate records  
- Filtered invalid entries (negative quantity/price)  

### 2. Feature Engineering
- Created **TotalAmount = Quantity × Price**  
- Extracted **Month, Day, Year** from transaction date  

### 3. Exploratory Data Analysis
- Top selling products  
- Least selling products  
- Top customers  
- Country-wise analysis  

### 4. Data Visualization
- 📈 Monthly Sales Trend (Time Series)  
- 🔥 Sales Heatmap (Month vs Day)  
- 📊 Sales Distribution (Histogram)  

---

## 📊 Key Insights
- Sales are unevenly distributed (right-skewed)  
- A few products contribute to major revenue  
- Certain months show higher sales peaks  
- Heatmap reveals high-performing days and patterns  

---

## 🧠 OOP Implementation
The project uses a class-based approach:

```python
class ECommerceAnalysis: