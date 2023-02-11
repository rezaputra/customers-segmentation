import streamlit as st
import pandas as pd

if 'clusteringData' in st.session_state:
    df = st.session_state['clusteringData']
    timeDp = st.session_state['dpTimeProcessing']
    data = pd.DataFrame(df)

    st.write(data)
    st.write(timeDp)
