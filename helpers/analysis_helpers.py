import pandas as pd
import streamlit as st

def getDataframe(file):
    """create pandas dataframe from csv file
    Args:
        - file: csv file
    returns:
        - pandas dataframe
    """
    try:
        global df
        df = pd.read_csv(file)
        
    except ValueError:
            st.write("Upload Your Data To Start!")
