# Import library
import pandas as pd
import streamlit as st
from components.detail_df import detailDf


# Set page info
st.set_page_config(page_title="Customers Segmentation", page_icon=":chart_with_upwards_trend:", layout="wide")

# Header and subheader
st.header("Welcome")


# Upload dataset csv only
st.text("Please input your data below:")

uploaded_file = st.file_uploader("Choose a file", type=["csv"], help="Only csv files allowed")


if uploaded_file is not None:
    st.session_state['dataFrame'] = pd.read_csv(uploaded_file)
    

if 'dataFrame' in st.session_state:
    df = st.session_state['dataFrame']

    column_headers = list(df.columns.values)
    attributes = st.multiselect('Select Attributes Below:', column_headers, column_headers)

    btnGetData = st.button('Select')
    
    if btnGetData:
        st.session_state['dataPreparation'] = df[attributes].copy()
        x =  st.session_state['dataPreparation']

        detailDf(x)
            
    

    

    
