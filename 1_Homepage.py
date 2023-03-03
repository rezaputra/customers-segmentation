# Import library
import pandas as pd
import streamlit as st
from components.detail_dataframe import detailDf


# Set page info
st.set_page_config(page_title="Customers Segmentation", page_icon=":chart_with_upwards_trend:", layout="wide")

# Header and subheader
st.header("Welcome")


# Upload dataset csv only
st.text("Please input your data below:")

uploaded_file = st.file_uploader("Choose a file", type=["csv"], help="Only csv files allowed")
unique_columns = []
dataset_id = ''

if uploaded_file is not None:
    st.session_state['rawData'] = pd.read_csv(uploaded_file)
    

if 'rawData' in st.session_state:
    df = pd.DataFrame(st.session_state['rawData'])
    column_headers = list(df.columns.values)

    for column in st.session_state['rawData']:
        if st.session_state['rawData'][column].is_unique:
            unique_columns.append(column)

    st.caption('')
    if unique_columns:
        select_id = st.selectbox('Which id to identifier the data sample from dataset:', unique_columns)
        st.caption('The ID is :  ' + select_id)
        dataset_id = select_id
    else:
        df['id'] = df.index + 1
        st.warning('Warning: Dataset does not contain unique column as id for identifier, The id will generate automatically')
        dataset_id = 'id'
    column_headers.remove(dataset_id)

    st.caption('')
    st.caption('')
    attributes = st.multiselect('Please select attributes from dataset to use for clustering:', column_headers, column_headers)
    st.caption('Total selected attributes :  ' + str(len(attributes)))

    attributes.insert(0, dataset_id)

    btnGetData = st.button('Select')
    
    if btnGetData and df[dataset_id].is_unique:
        st.session_state['dataFrame'] = df[attributes]
        st.session_state['idName'] = dataset_id

        detailDf(st.session_state['dataFrame'])