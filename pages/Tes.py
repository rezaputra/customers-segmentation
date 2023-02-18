import streamlit as st
from components.detail_dataframe import detailDf
from method.clean import Clean
import pandas as pd


if 'dataPreparation' in st.session_state:
    data = pd.DataFrame(st.session_state['dataPreparation'])

    st.write('Before cleaning')
    detailDf(data)

    btn =  st.button('Run clean')

    if btn:
        st.write('After cleaning')

        clean = Clean()

        result = clean.cleanDf(data)

        # st.write(data.iloc[:,0])

        detailDf(result)

