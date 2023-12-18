import streamlit as st
import helpers.input_helpers as input_helpers


def main():

    with st.sidebar:
        st.header("Welcom To My Reports")
        uploaded_file = input_helpers.fileUploader()
        if uploaded_file is not None:
            st.header("ADD")
            table = st.button("Table")
            chart = st.button("Chart")


if __name__ == "__main__":
    main()
