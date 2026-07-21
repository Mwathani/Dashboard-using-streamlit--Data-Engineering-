# Import rquired libraries
import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

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
fig = px.scatter(chart_data, x="UnitPrice", y="Quantity", color="Region", title="Unit Price vs Quantity")
st.plotly_chart(fig)
