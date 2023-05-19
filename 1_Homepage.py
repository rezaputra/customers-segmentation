# Import library
import pandas as pd
import streamlit as st
from components.detail_dataframe import detailDf
import json


# Set page info
st.set_page_config(page_title="Customers Segmentation", page_icon=":chart_with_upwards_trend:", layout="wide")

# Header and subheader
st.header("Welcome")


# Upload dataset csv only
st.text("Please input dataset below:")

uploaded_file = st.file_uploader("Choose a dataset", type=["csv"], help="Only csv files allowed")
unique_columns = []
dataset_id = ''

if uploaded_file is not None:
    st.session_state['rawData'] = pd.read_csv(uploaded_file, low_memory=False)
    st.session_state['fileName'] = uploaded_file.name
    

if 'rawData' in st.session_state:
    df = pd.DataFrame(st.session_state['rawData'])
    column_headers = list(df.columns.values)

    # for column in st.session_state['rawData']:
    #     if st.session_state['rawData'][column].is_unique:
    #         unique_columns.append(column)

    # st.caption('')
    # if unique_columns:
    #     select_id = st.selectbox('Which id to identifier the data sample from dataset:', unique_columns)
    #     st.caption('The ID is :  ' + select_id)
    #     dataset_id = select_id
    # else:
    #     df['id'] = df.index + 1
    #     st.warning('Warning: Dataset does not contain unique column as id for identifier, The id will generate automatically')
    #     dataset_id = 'id'
    # column_headers.remove(dataset_id)

    df['id'] = df.index + 1
    dataset_id = 'id'
    

    st.caption('')
    st.caption('')

    # column_headers.remove(dataset_id)
    attributes = st.multiselect('Please select attributes from dataset to use for clustering:', column_headers, column_headers)
    st.caption('Total selected attributes :  ' + str(len(attributes)))

    attributes.insert(0, dataset_id)

    btnGetData = st.button('Select')
    
    if btnGetData:
        st.session_state['dataFrame'] = df[attributes]
        st.session_state['idName'] = dataset_id


        # Open and read the existing JSON file
        with open('evaluation/dataset.json', 'r') as file:
            json_data = json.load(file)

        new_dataset = {"dataset": st.session_state['fileName']}

        # Check if the new dataset already exists in the JSON data
        existing_datasets = [data["dataset"] for data in json_data]

        if new_dataset["dataset"] not in existing_datasets:
            # Add the new dataset to the JSON data
            json_data.append(new_dataset)

        # Write the updated JSON data back to the file
        with open('evaluation/dataset.json', 'w') as file:
            json.dump(json_data, file, indent=2)

        detailDf(st.session_state['dataFrame'])