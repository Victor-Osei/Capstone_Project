# Power BI Dashboard Project

## Project Description

This project is an end-to-end business intelligence solution developed for a client assigned by getINNOtized. The client has collected transactional data for the year 2019 but has not yet utilized it effectively. The goal is to analyze the data and provide a comprehensive report to identify sales opportunities and operational efficiencies.

### Project Objectives
The objective of this project is to develop an end-to-end business intelligence solution to analyze the client’s 2019 transactional data and identify key insights to drive sales growth and improve operational efficiency. This solution aims to help the client make data-driven decisions that optimize product offerings, improve profitability, and streamline operations across various regions.

To achieve this objective, the following were undertaken following the CRISP-DM Framework:
1. Data Extraction and Cleaning.
2. Hypothesis Testing
3. Power Bi Deloyment 
4. Streamlit App Building

### Business Questions:
1. Determine the total revenue generated in 2019.
2. Identify seasonality in the sales patterns.
3. Highlight the best and worst-selling products.
4. Compare sales performance across different periods (weeks and months).
5. Identify the cities with the highest product deliveries.
6. Compare product categories by revenue and quantities sold.
7. Provide additional insights based on data exploration.

Additionally, products priced above $99.99 are classified as **High-Level Products**, while those priced lower are classified as **Basic-Level Products**.


### Hypothesis Testing
- **Null Hypothesis (H₀)**: There is no significant relationship between unit price and sales.
- **Alternative Hypothesis (H₁)**: There is a significant relationship between unit price and sales.

### Results
- **Pearson Correlation Coefficient**: 1.00
- **Coefficient for Price_Each**: 0.9998
- **P-value for Price_Each**: 0.000

The p-value for the Price_Each coefficient is 0.000, which is well below the common significance level of 0.05. This indicates that the relationship between unit price and sales volume is statistically significant.

### Conclusion
Since the p-value is much less than 0.05, we reject the Null Hypothesis (H₀) and accept the Alternative Hypothesis (H₁). This suggests that there is a significant relationship between unit price and sales volume. The Pearson Correlation Coefficient of 1.00 further supports this, showing a very strong positive linear relationship between the two variables.

This means that changes in unit price are significantly associated with changes in sales volume, according to this regression model.

## Data and Variable Description

- **Dataset Overview**: The sales data spans the entire year of 2019. The first 6 months (January - June) were collected in Excel and stored as CSV files, while the last 6 months (July - December) are stored in a remote database.
- **Transaction Data Variables**:
  - `Order ID`: Unique identifier for each transaction.
  - `Product`: Name of the product sold.
  - `Category`: Product category.
  - `Unit Price`: Price per unit of the product.
  - `Quantity`: Number of units sold.
  - `City`: The city to which the product was delivered.
  - `Date`: The transaction date.
  - `Total Revenue`: Calculated as `Unit Price` * `Quantity`.

## Installation

To set up and run the Power BI dashboard, follow these steps:

1. Clone the repository or download the files.
2. Download Power BI Desktop from [Power BI Download Center](https://powerbi.microsoft.com/downloads/).
3. Use the provided CSV data for the first 6 months from the Onedrive link, and configure the database connection for the second 6 months data.
4. Open the Power BI file (.pbix) to load the dashboard and view the insights.

## Author

This project was developed by [Team_Fiji](mailto:your.email@example.com). Connect with me on [LinkedIn](https://www.linkedin.com/in/victor-osei-duah-a9182a13a/).

## Project Links Table

| Code  | Project Name               | Power BI Link                          | Published App Link                      |
|-------|-----------------------------|----------------------------------------|-------------------------------------|
| LP5 | Power BI Dashboard Project (2019 Sales Analysis) | [Power BI Dashboard](https://app.powerbi.com/groups/me/reports/ae796325-9ee2-4d2c-bf29-5c99ad3fae03/d79d9368ed0162806e59?experience=power-bi) | [Published Report](https://link-to-report) |
