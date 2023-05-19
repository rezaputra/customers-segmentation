import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from components.plotting import dp_two_dimension, dp_three_dimension

perc = [0.20, 0.40, 0.60, 0.80]
inc = ['object', 'float', 'int']


def viewDetailDpWithFE(e, m, d):
    data = pd.DataFrame(d.copy())
    method = m
    column = data.columns.values.tolist()
    id = pd.DataFrame(st.session_state['datasetId'].copy())

    if 'ID' not in data.columns:
        data.insert(loc=0, column='ID', value=id.values)

    tabShowData, tabPlot = st.tabs(['🗃 Result', 'ℹ Plotting'])

    with tabShowData:
        colShowData, colDetail ,colTimeExecute = st.columns([1,1,1], gap="medium")
        with colShowData:
            st.caption("Dataset")         
            st.write(data)

        with colDetail:
            st.caption("Detail")          
            st.write(data.describe(percentiles = perc, include = inc))
        with colTimeExecute:
            st.caption("Processing time")        
            st.write("Clean : ", round(e['Clean'], 4))                
            st.write(method['encode'] + " : ", round(e['encode'], 4))              
            st.write(method['scale'] + " : ", round(e['scale'], 4))              
            st.write(method['extraction'] + " : ", round(e['extraction'], 4))    
            st.write( "Total time: ", round(e['total'], 4))  

    with tabPlot:
        match method['dimension']:                
            case 2:
                dp_two_dimension(data, column)

            case 3:
                dp_three_dimension(data, column)


def viewDetailDpWithoutFE(e, m, d):
    data = pd.DataFrame(d.copy())
    method = m
    id = pd.DataFrame(st.session_state['datasetId'].copy())

    if 'ID' not in data.columns:
        data.insert(loc=0, column='ID', value=id.values)

    tabShowData, tabDetail = st.tabs(['🗃 Result', 'ℹ Time'])
    with tabShowData:
        st.caption("Dataset")         
        st.write(data)
    with tabDetail:
        colDetail ,colTimeExecute = st.columns([2,1],gap="medium")
        with colDetail:
            st.caption("Detail")          
            st.write(data.describe(percentiles = perc, include = inc))
        with colTimeExecute:
            st.caption("Processing time")        
            st.write("Clean : ", round(e['Clean'], 4))                
            st.write(method['encode'] + " : ", round(e['encode'], 4))              
            st.write(method['scale'] + " : ", round(e['scale'], 4))              
            st.write( "Total time: ", round(e['total'], 4))  

