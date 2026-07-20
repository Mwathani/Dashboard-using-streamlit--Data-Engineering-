import streamlit as st

# Imports the pandas library
import pandas as pd

student_info = pd.DataFrame({
    'FullName': [
        'John Doe', 
        'Rooney Mwathani',
        'John Rooney'
        ],
    'Admission No': [
        'ICTM/00056/023', 
        'BE/00016/019',
        'CIT/00041/024']
})

student_info
