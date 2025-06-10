import pandas as pd
import numpy as np
import streamlit as st


def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded data as a DataFrame.
    """
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def display_data(data):
    """
    Display the DataFrame in Streamlit.
    
    Parameters:
    data (pd.DataFrame): The DataFrame to display.
    """
    if data is not None:
        st.write("### Data Preview")
        st.data_editor(data, use_container_width=True, key="data_editor")
    else:
        st.error("No data to display.")