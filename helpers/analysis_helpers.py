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

def time_series_analysis(df, date_column: list, groupby_period: str, **kwargs):
    """return one level group table with, take a datetime column and convert it into periods in which get the periond this date belongs to
    Args:
    -df: pandas Dataframe(requiered).
    -date_column: (string) name of date column to group with (requiered).
    -groupby_period: (string) one of [y,q,m,D] (requiered).
    -kwargs: dict like with values refer to aggregation function and values refer to columns to aggregate(required)
    returns:
    one level grouppped table with date period index
    """
    aggrigation_dictionary = {}
    for key, value in kwargs.items():
        aggrigation_dictionary.update(**{v: str(key) for v in value})
    df[date_column] = df[date_column].apply(pd.to_datetime())
    periods = df[date_column].dt.to_period(groupby_period).astype(str)
    return df.groupby(periods).agg(aggrigation_dictionary)