import streamlit as st
import pandas as pd


st.title("CSV and EXCEL File to Visual Table")


uploaded_file=st.file_uploader("Choose a CSV or EXCEL file",type=["csv","xlsx"])

if uploaded_file is not None:
    try:
        
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)

          
        
        
        st.write("### File Content:")
        st.write(df)
        
    except Exception as e:
        st.error(f"Error reading file: {e}")