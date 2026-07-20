import streamlit as st

# Imports the pandas library
import pandas as pd

st.write(pd.DataFrame({
    'FullName': [
        'John Doe', 
        'Rooney Mwathani',
        'John Rooney'
        ],
    'Admission No': [
        'ICTM/00056/021', 
        'BE/00016/019',
        'CIT/00041/025']
}))

