import streamlit as st

def creatSelectbox(title,options):
    return st.selectbox(label=title,options=options)


def csvDownloader(data,text_display="Download",file_name='data'):
    return st.download_button(
        label=text_display,
        data=data,
        file_name =file_name,
        mime='text/csv',
        )


@st.cache
def dfToCsv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

