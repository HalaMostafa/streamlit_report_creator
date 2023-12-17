import streamlit as st
import helpers.input_helpers as input_helpers

def main_app():
    file = input_helpers.fileUploader()
    df = input_helpers.getDataFrame(file)
    st.write(df.head())

main_app()