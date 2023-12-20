import streamlit as st
import pandas as pd
import helpers.input_helpers as input_helpers
import helpers.analysis_helpers as analysis_helpers

     

def sideBar():
        
    with st.sidebar:
        st.header("Welcom To My Reports")
        uploaded_file = input_helpers.fileUploader()
        analysis_helpers.getDataframe(uploaded_file)

def main():
    option = None # Initialize selected_option outside the sidebar
    sideBar()
    try:
        st.write(df.head())
        if 'click_count' not in st.session_state:
            st.session_state.click_count = 0
        if 'click_history' not in st.session_state:
            st.session_state.click_history = []

        if st.button('Add Analysis'):
            st.session_state.click_count += 1
            st.session_state.click_history.append(f'Button clicked {st.session_state.click_count} times')

        for _ in st.session_state.click_history:
            with st.sidebar:
                option = st.selectbox("Select Analysis",[None,'one level pivot table','two level pivot table'])
            if option is not None:
                st.write('You Selected',option) 
    except NameError:
        print("waiting for data to be uploaded!")











if __name__ == "__main__":
    main()
