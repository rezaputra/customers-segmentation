import streamlit as st
import pandas as pd


perc = [0.20, 0.40, 0.60, 0.80]
inc = ['object', 'float', 'int']


def detailDf(d):
    data = pd.DataFrame(d)
    s = (data.dtypes == "object")
    t = (data.dtypes != "object")

    object_cols = list(s[s].index)
    non_object_cols = list(t[t].index)
    

    tabShowData, tabDetail = st.tabs(['🗃 Dataset', 'ℹ Details'])
    with tabShowData:
        st.write(data)        

    with tabDetail:
        colCleanDetails1, colCleanDetails2 = st.columns([3,1])
        with colCleanDetails1:
            st.write(data.describe(percentiles = perc, include = inc))
            # st.write(x.info())

        with colCleanDetails2:
            st.markdown("##### Recaps")
            nullValue = data.isna().values.sum()
            st.write("Total record:", len(data))
            st.write("Total elements:", data.size)
            st.write("Total attributes:", data.shape[1])
            st.write("Categorical attributes:", len(object_cols))
            st.write("Numeric attributes:", len(non_object_cols))
            st.write("Total duplicate data:", data.duplicated(keep=False).sum())
            st.write("Total Null or NA values:", nullValue)


