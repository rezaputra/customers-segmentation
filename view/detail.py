import pandas as pd
import streamlit as st

def viewDetails(d):
    x = pd.DataFrame(d)
    s = (x.dtypes != "object")
    t = (x.dtypes == "object")
    perc = [0.20, 0.40, 0.60, 0.80]
    inc = ['object', 'float', 'int']

    object_cols = list(s[s].index)
    non_object_cols = list(t[t].index)
    

    tabShowData, TabDetail = st.tabs(['🗃 Dataset', 'ℹ Details'])
    with tabShowData:
        st.write(x)        

    with TabDetail:
        colCleanDetails1, colCleanDetails2 = st.columns([3,1])
        with colCleanDetails1:
            st.write(x.describe(percentiles = perc, include = inc))
            # st.write(x.info())

        with colCleanDetails2:
            st.markdown("##### Recaps")
            nullValue = x.isna().values.sum()
            st.write("Total record:", len(x))
            st.write("Total elements:", x.size)
            st.write("Total attributes:", x.shape[1])
            st.write("Categorical attributes:", len(object_cols))
            st.write("Numeric attributes:", len(non_object_cols))
            st.write("Total duplicate data:", x.duplicated(keep=False).sum())
            st.write("Total Null or NA values:", nullValue)