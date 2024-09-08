# Power BI Dashboard Project

## Project Description

This project is an end-to-end business intelligence solution developed for a client assigned by getINNOtized. The client has collected transactional data for the year 2019 but has not yet utilized it effectively. The goal is to analyze the data and provide a comprehensive report to identify sales opportunities and operational efficiencies.

### Key Objectives:
1. Determine the total revenue generated in 2019.
2. Identify seasonality in the sales patterns.
3. Highlight the best and worst-selling products.
4. Compare sales performance across different periods (weeks and months).
5. Identify the cities with the highest product deliveries.
6. Compare product categories by revenue and quantities sold.
7. Provide additional insights based on data exploration.

Additionally, products priced above $99.99 are classified as **High-Level Products**, while those priced lower are classified as **Basic-Level Products**.

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
3. Use the provided CSV data for the first 6 months from the link, and configure the database connection for the remaining data.
4. Open the Power BI file (.pbix) to load the dashboard and view the insights.

## Author

This project was developed by [Your Name](mailto:your.email@example.com). Connect with me on [LinkedIn](https://www.linkedin.com/in/yourprofile).

## Project Links Table

| Code  | Project Name               | Power BI Link                          | Published Link                      |
|-------|-----------------------------|----------------------------------------|-------------------------------------|
| BI001 | 2019 Sales Analysis         | [Power BI Dashboard](https://link-to-powerbi) | [Published Report](https://link-to-report) |
