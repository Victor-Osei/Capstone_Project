import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Set Webpage Name
st.set_page_config(page_title="2019 BI Solution for Sales & Efficiency", page_icon="📊", layout="wide")

# Apply light theme with dark text for better readability
st.markdown("""
    <style>
        .main {
            background-color: #F8F9FA;
            color: #212529;
        }
        footer {visibility: hidden;}
        .css-18e3th9 {
            background-color: #F8F9FA;
            color: #212529;
        }
        .stButton>button {
            color: #212529;
            background-color: #E9ECEF;
            border-color: #CED4DA;
        }
        .stTextInput>div>div>input {
            color: #212529;
        }
    </style>
    """, unsafe_allow_html=True)




# Sidebar Navigation
st.sidebar.title("2019 Sales BI Solution")
st.sidebar.subheader("Navigation")
options = st.sidebar.radio("Go to", ["Home", "Sales Overview", "Product Analysis", "City Insights", "Seasonality Trends"])

# Random Sales Fact
random_facts = [
    "Did you know? Our highest sales occurred in April 2019.",
    "Fun fact: Products priced above $99.99 generated more revenue.",
    "Surprising stat: The city with the highest number of deliveries is San Francisco!",
    "Tip: Sales peaks during holidays, plan your inventory accordingly."
]
st.sidebar.markdown(f"💡 *Random Fact:* {random.choice(random_facts)}")

# Load the dataset (df_2019.csv)
@st.cache_data
def load_data():
    data = pd.read_csv('df_2019.csv')
    return data

data = load_data()

# Pages in the app based on the client's BI needs

# Home Page
if options == "Home":
    st.title("📊 2019 Sales & Efficiency BI Solution")

# Add a banner image
    st.image("images\Gadget7.jpg", use_column_width=True)  # Replace with your image URL


    # Introduction about the app
    st.subheader("About This App")
    st.write("""
        Welcome to the 2019 Sales & Efficiency Business Intelligence (BI) Solution! 
        This app provides insightful data analysis to help businesses understand their sales trends, 
        product performance, and seasonal variations. 
        It's designed to help improve decision-making and identify growth opportunities through interactive visualizations.
    """)
    
    # Information about the creator
    st.subheader("About the Creator")
    st.write("""
        **Creator:** Team_Fiji 
             
        A group of data enthusiasts with experience in business intelligence, data analysis, and machine learning.
        They are passionate about turning data into actionable insights, improving business efficiency, 
        and solving real-time problems through data-driven solutions.
    """)
    
    st.write("""
        The 2019 Sales BI Solution was developed to address the needs of businesses in analyzing their sales data, 
        identifying seasonal trends, and improving sales strategies. 
        Through this app, you can explore various dimensions of sales, from product performance to city-wise distributions.
    """)
    # Contact and GitHub Repository
    st.subheader("Need Help or Collaboration?")
    st.markdown("""
    For collaboration or support, please contact Team_Fiji.
""")

# Create a clickable button to GitHub
    github_url = "https://github.com/Victor-Osei/Capstone_Project"
    st.markdown(f"""
    <a href="{github_url}" target="_blank">
        <button style="background-color:#4CAF50; color:white; padding:10px 20px; 
                        text-align:center; text-decoration:none; display:inline-block; 
                        font-size:16px; margin:4px 2px; cursor:pointer; border:none;">
            Visit Our GitHub Repository
        </button>
    </a>
    """, unsafe_allow_html=True)


# Sales Page
elif options == "Sales Overview":
    st.title("📊 Sales Overview: 2019")
    
    # Summarize total sales
    total_sales = round(data['Sales'].sum(), 2)
    high_level_sales = round(data[data['Price_Each'] > 99.99]['Sales'].sum(), 2)
    basic_level_sales = round(data[data['Price_Each'] <= 99.99]['Sales'].sum(), 2)    

    # Format the numbers as money values with $ and commas
    total_sales_formatted = f"${total_sales:,.2f}"
    high_level_sales_formatted = f"${high_level_sales:,.2f}"
    basic_level_sales_formatted = f"${basic_level_sales:,.2f}"

    st.metric(label="Total Sales (2019)", value=total_sales_formatted)
    st.metric(label="High-Level Product Sales (>$99.99)", value=high_level_sales_formatted)
    
    # Show percentage of high-level product sales
    percentage_of_high_level_products = (high_level_sales / total_sales)  
    st.progress(percentage_of_high_level_products)  # Display the progress bar
    
    st.metric(label="Basic-Level Product Sales (<=$99.99)", value=basic_level_sales_formatted)
    
    # Show percentage of basic-level product sales
    percentage_of_basic_level_products = (basic_level_sales / total_sales)  
    st.progress(percentage_of_basic_level_products)  # Display the progress bar
    
    # Display percentage as text
    st.write(f"High-Level Product Sales Percentage: {percentage_of_high_level_products * 100:.2f}%") 
    st.write(f"Basic-Level Product Sales Percentage: {percentage_of_basic_level_products * 100:.2f}%")
    
    # Interactive sales chart by product
    fig = px.bar(data, x="Product", y="Sales", color="Product", title="Product Sales (2019)")
    fig.update_layout(title={'x': 0.5})  # Centers the title
    st.plotly_chart(fig, use_container_width=True)

# Product Analysis Page
elif options == "Product Analysis":
    st.title("🔍 Product Analysis")
    
    # Analyze product performance based on unit price and sales volume
    st.write("Evaluate product performance by pricing and sales.")
    fig = px.scatter(data, x="Price_Each", y="Sales", color="Product", size="Price_Each", hover_name="Product",
                 title="Product Pricing vs Sales")
    fig.update_layout(title={'x': 0.5})  # Center the title
    st.plotly_chart(fig, use_container_width=True)

# City Page
elif options == "City Insights":
    st.title("🌆 City Insights")
    
    # Group sales by city
    city_sales = data.groupby("City")['Sales'].sum().reset_index()
    
    # City-wise sales distribution using a pie chart
    fig = px.pie(city_sales, names="City", values="Sales", title="City-wise Sales Distribution (2019)")
    fig.update_layout(title={'x': 0.5})  # Center the title
    st.plotly_chart(fig, use_container_width=True)

# Seasonal Trend Page
elif options == "Seasonality Trends":
    st.title("📅 Seasonality Trends")
    
    st.write("Analyze how sales change across months to identify seasonal trends.")
    
    # Assuming the data has a 'Month' column with values like 'Jan', 'Feb', etc.
    monthly_sales = data.groupby('Month')['Sales'].sum().reset_index()
    
    # Display a line chart for monthly sales trends
    fig = px.line(monthly_sales, x="Month", y="Sales", title="Monthly Sales in 2019")
    fig.update_layout(title={'x': 0.5})  # Center the title
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("Note: Seasonal insights help improve stock and marketing strategies.")

# Interactive feedback with emojis
st.sidebar.markdown("### How did you find this dashboard? 😊")
st.sidebar.button("👍 Love it!")
st.sidebar.button("👎 Needs more features")

# Footer (Optional)
st.markdown("<footer>Powered by Team_Fiji | © 2024</footer>", unsafe_allow_html=True)
