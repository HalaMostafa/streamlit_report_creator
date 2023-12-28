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


def groupby_table(df,groupby_column:list,**kwargs):
    """this function takes a df and returns groupby table from it
    Args:
    -df: pandas df (required)
    -groupby_column: list of strings (requiered)
    -kwargs: name of each aggrigartion function and the value is list of column names to be aggregated (requiered)
    """
    aggrigation_dictionary = {}
    for key, value in kwargs.items():
        aggrigation_dictionary.update(**{v: str(key) for v in value})
    return df.groupby(groupby_column).agg(aggrigation_dictionary)

def pivot_table_analysis(df,index_columns:list,columns:list,value:str, agg_func:str):
    """rturn a spreadsheet-style pivot table as a DataFrame.
    Args:
    -df: pandas df (required).
    -index_columns: list(required).
    -columns: list(required).
    -value: column to be aggrigated string (required).
    -agg_func: string (required).
    returns:
    two level table as Dataframe    
    """
    return pd.pivot_table(df, values=value, index=index_columns,
                       columns=columns, aggfunc=agg_func)