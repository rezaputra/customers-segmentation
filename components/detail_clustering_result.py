import streamlit as st
import pandas as pd


def kmeans_result_detail(d):
    data = d
    col1, col2, col3 = st.columns([1.2,1,1], gap='large')
    x = st.session_state['dataPreparation'].copy()
    dfResult = pd.DataFrame(x)

    with col1:
        st.caption('Clustering Result') 
        if 'CLUSTER' not in dfResult.columns:
            dfResult.insert(loc=len(dfResult.columns), column='CLUSTER' ,value=data['result'].labels_)
        st.write(dfResult) 

    with col2:
        st.caption('Cluster Center')
        st.write(data['result'].cluster_centers_)
        
        st.caption('')
        st.caption('More Information')
        st.write('Number of iterations run :', data['result'].n_iter_)
        st.write('Silhouette score:', round(data['score'], 4))


    with col3:
        st.caption('Computation Time')
        st.write('Data preparation :',round(st.session_state['dpTimeProcessing']['total'], 4))     
        st.write('K-Means clustering :',round(data['time'], 4))     
        st.write('Total time :',round(st.session_state['dpTimeProcessing']['total'] + data['time'], 4))     



