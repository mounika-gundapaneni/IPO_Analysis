# filepath: /c:/Users/saigm/IPO_Analysis/main/windows/displayModules/display_streamlit.py
import streamlit as st
import pandas as pd

# Read the Excel file
excel_file_path = r"C:\Users\saigm\Downloads\hpi_master.csv"
df = pd.read_csv(excel_file_path)

# Select specific columns
selected_columns = df[['yr', 'period', 'frequency']]  # Replace with your column names

# Display the selected columns in Streamlit
st.write("Selected Columns")
st.dataframe(selected_columns)

# Plot a line chart for the selected columns
st.line_chart(selected_columns)