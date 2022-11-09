import streamlit as st
import pandas as pd
from PIL import Image

def fileUploader():
    """
    input widget to Browse csv file from local machine 
    """
    return st.file_uploader(
        label  = "Choose a CSV file",
        accept_multiple_files = False,
        )

def getDataFrame(uploaded_file):
    """
    convert csv file into pandas dataframe
    """
    if uploaded_file is not None:
        return  pd.read_csv(uploaded_file)
    else:
        return "No Data Uploaded"

def imageUploader():
    """input widget to upload image
    return image 
    """
    return st.file_uploader("Browse Image", type=["png","jpg","jpeg"])

def load_image(image_file):
    return Image.open(image_file)

