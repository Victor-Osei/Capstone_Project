import streamlit as st
import pandas as pd
import plotly.express as px
import random

# Set custom theme for dark royal blue
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
st.sidebar.title("2019 BI Solution")
st.sidebar.subheader("Navigation")
options = st.sidebar.radio("Go to", ["Sales Overview", "Product Analysis", "City Insights", "Seasonality Trends"])

# Random Sales Fact
random_facts = [
    "Did you know? Our highest sales occurred in May 2019.",
    "Fun fact: Products priced above $99.99 generate 40% more revenue.",
    "Surprising stat: The city with the highest number of deliveries is New York!",
    "Tip: Sales peaks during holidays, plan your inventory accordingly."
]
st.sidebar.markdown(f"💡 *Random Fact:* {random.choice(random_facts)}")

# Load the dataset (df_2019.csv)
@st.cache_data
def load_data():
    data = pd.read_csv('df_2019.csv')  # Replace with the actual path if needed
    return data

data = load_data()

# Pages in the app based on the client's BI needs
if options == "Sales Overview":
    st.title("📊 Sales Overview: 2019")
    
    # Summarize total sales
    total_sales = data['Sales'].sum()
    high_level_sales = data[data['Price_Each'] > 99.99]['Sales'].sum()
    basic_level_sales = data[data['Price_Each'] <= 99.99]['Sales'].sum()    

    st.metric(label="Total Sales (2019)", value=total_sales)

    st.metric(label="High-Level Product Sales (>$99.99)", value=high_level_sales)
    # Show percentage of high-level product sales
    percentage_of_high_level_products = (high_level_sales / total_sales)  # Keep as a float between 0 and 1
    st.progress(percentage_of_high_level_products)  # Display the progress bar
    

    st.metric(label="Basic-Level Product Sales (<=$99.99)", value=basic_level_sales)
    # Show percentage of basic-level product sales
    percentage_of_basic_level_products = (basic_level_sales / total_sales)  # Keep as a float between 0 and 1
    st.progress(percentage_of_basic_level_products)  # Display the progress bar
    
    # Display percentage as text
    st.write(f"High-Level Product Sales Percentage: {percentage_of_high_level_products * 100:.2f}%")  # Display the percentage as text
    st.write(f"Basic-Level Product Sales Percentage: {percentage_of_basic_level_products * 100:.2f}%")  # Display the percentage as text
    
    # Interactive sales chart by product
    fig = px.bar(data, x="Product", y="Sales", color="Product", title="Product Sales (2019)")
    fig.update_layout(title={'x': 0.5})  # Centers the title
    st.plotly_chart(fig, use_container_width=True)

# if options == "Sales Overview":
#     st.title("📊 Sales Overview: 2019")
    
#     # Summarize total sales
#     total_sales = data['Sales'].sum()
#     high_level_sales = data[data['Price_Each'] > 99.99]['Sales'].sum()
#     basic_level_sales = data[data['Price_Each'] <= 99.99]['Sales'].sum()    

#     st.metric(label="Total Sales (2019)", value=total_sales)
#     st.metric(label="High-Level Product Sales (>$99.99)", value=high_level_sales)
#     st.metric(label="Basic-Level Product Sales (<=$99.99)", value=basic_level_sales)
    
#     # Show percentage of high-level product sales
#     progress = int((high_level_sales / total_sales) * 100)
#     st.progress(progress)  # Show progress of high-level sales
    
#     # Interactive sales chart by product
#     fig = px.bar(data, x="Product", y="Sales", color="Product", title="Product Sales (2019)")
#     fig.update_layout(title={'x': 0.5})  # Centers the title
#     st.plotly_chart(fig, use_container_width=True)

elif options == "Product Analysis":
    st.title("🔍 Product Analysis")
    
   # Analyze product performance based on unit price and sales volume
    st.write("Evaluate product performance by pricing and sales.")
    fig = px.scatter(data, x="Price_Each", y="Sales", color="Product", size="Price_Each", hover_name="Product",
                 title="Product Pricing vs Sales")
    fig.update_layout(title={'x': 0.5})  # Center the title
    st.plotly_chart(fig, use_container_width=True)

elif options == "City Insights":
    st.title("🌆 City Insights")
    
    # Group sales by city
    city_sales = data.groupby("City")['Sales'].sum().reset_index()
    
    # City-wise sales distribution using a pie chart
    fig = px.pie(city_sales, names="City", values="Sales", title="City-wise Sales Distribution (2019)")
    st.plotly_chart(fig, use_container_width=True)
    
    st.success(f"The city with the highest deliveries is *{city_sales.loc[city_sales['Sales'].idxmax(), 'City']}*.")

elif options == "Seasonality Trends":
    st.title("📅 Seasonality Trends")
    
    st.write("Analyze how sales change across months to identify seasonal trends.")
    
    # Assuming the data has a 'Month' column with values like 'Jan', 'Feb', etc.
    monthly_sales = data.groupby('Month')['Sales'].sum().reset_index()
    
    # Display a line chart for monthly sales trends
    fig = px.line(monthly_sales, x="Month", y="Sales", title="Monthly Sales in 2019")
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("Note: Seasonal insights help improve stock and marketing strategies.")

# Interactive feedback with emojis
st.sidebar.markdown("### How did you find this dashboard? 😊")
st.sidebar.button("👍 Love it!")
st.sidebar.button("👎 Needs more features")

# Footer (Optional)
st.markdown("<footer>Powered by Team_Fiji | © 2024</footer>", unsafe_allow_html=True)
