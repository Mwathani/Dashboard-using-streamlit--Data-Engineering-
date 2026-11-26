# Import rquired libraries
import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px
import altair as alt

# 01. Cached function to load data
@st.cache_data

def load_data():
    # Get the dir of this file location
    script_dir = Path(__file__).parent

    # Build the path
    file_path = script_dir / "Product-Sales-Region.xlsx"

    # Read the file
    df = pd.read_excel(file_path)
    return df 

# 02. Call the function to get the data
chart_data = load_data()


# 03. Use the data in app. 
st.write("Product Sales Regional Data:")
st.dataframe(chart_data)

# Example: Plotting the data
chart_data['OrderDate'] = pd.to_datetime(chart_data['OrderDate'])

# 01. Line Charts
# st.line_chart(chart_data, x="OrderDate", y="TotalPrice", color="Region")

# 02. Bar and Column charts
# st.bar_chart(chart_data, x="Region", y="TotalPrice")

# 03. Scatter Plots
# fig = px.scatter(chart_data, x="UnitPrice", y="Quantity", color="Region", title="Unit Price vs Quantity")
# st.plotly_chart(fig)

# 04. Altair Charts
# chart = alt.Chart(chart_data).mark_circle(size=60).encode(
#     x = "UnitPrice",
#     y = "Quantity",
#     color = "Region",
#     tooltip = ["Product", "UnitPrice", "Quantity", "Region"]  
# ).interactive()

# st.altair_chart(chart, use_container_width=True)


# 05. Area Charts
# st.area_chart(chart_data, x="OrderDate", y="TotalPrice")


# 06. Metrics & KPIs Indicators
# """
# Real-life usecase: Used in Executive dashboards by managers 
#                 -> To see the totals instantly at a glance
# """

# total_sales = chart_data["TotalPrice"].sum()
# st.metric(label="TotalRevenue", value=f"${total_sales:,.2f}", delta="4.2%")


# 07. Data Tables & DataFrames
# st.dataframe(chart_data)
# st.table(chart_data)
