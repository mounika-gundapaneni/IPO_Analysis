# filepath: /c:/Users/saigm/IPO_Analysis/main/windows/displayModules/display_streamlit.py
import streamlit as st
import pandas as pd
import os

# Path to the results folder
results_folder = r"C:\Users\saigm\IPO_Analysis\Results\IPOs_List\2024"

# List all JSON files in the results folder
json_files = [f for f in os.listdir(results_folder) if f.endswith('.json')]

st.title("Results Folder Data Viewer (JSON)")

if not json_files:
    st.warning("No JSON files found in the results folder.")
else:
    # Let user select a file
    selected_file = st.selectbox("Select a JSON file to display:", json_files)
    file_path = os.path.join(results_folder, selected_file)
    df = pd.read_json(file_path)

    st.write(f"Data from: {selected_file}")
    st.dataframe(df)

    # Let user select columns to plot
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    if len(numeric_cols) >= 2:
        x_col = st.selectbox("Select X-axis column:", numeric_cols)
        y_col = st.selectbox("Select Y-axis column:", numeric_cols, index=1)
        st.line_chart(df[[x_col, y_col]])
    else:
        st.info("Not enough numeric columns to plot a line chart.")