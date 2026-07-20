# Import rquired libraries
import streamlit as st
import pandas as pd
from pathlib import Path

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
st.write("Here is your data:")
st.dataframe(chart_data)

# Example: Plotting the data
chart_data['OrderDate'] = pd.to_datetime(chart_data['OrderDate'])

st.line_chart(chart_data, x="OrderDate", y="TotalPrice", color="Region")
