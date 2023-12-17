import streamlit as st
import pandas as pd
from PIL import Image


def fileUploader():
    """
    input widget to Browse csv file from local machine 
    """
    uploaded_file = st.file_uploader("Upload CSV", type=['csv'])
    if uploaded_file is not None:
        # Process the uploaded file
        st.write("File uploaded successfully!")
        # Add your processing logic here
    return uploaded_file

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

