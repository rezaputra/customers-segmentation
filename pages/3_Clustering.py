import streamlit as st
import pandas as pd
from components.get_clustering_parameter import *
from components.detail_clustering_result import *
from controller.clustering_controller import ClusteringController
import time


if 'dataPreparation' in st.session_state:
    data = st.session_state['dataPreparation']
    dpTime = st.session_state['dpTimeProcessing']
    dpMethod = st.session_state['dpMethod']
    df = pd.DataFrame(data)

    st.markdown('### Clustering Algorithm Options')
    columnInputAlgorithm, columnInputParameter, columnParams = st.columns([1,1,1], gap='large')

    with columnInputAlgorithm:
        algorithm = st.radio("Please select clustering algorithm will be use to cluster the dataset",
            ["K-Means", "LTKC", "Agglomerative","DBSCAN", "HDBSCAN", "Affinity Propagation"],
            index=1, key="input_algo")
        
        st.caption(algorithm)

    with columnInputParameter:
        if 'input_algo' in st.session_state:
            args = st.session_state.input_algo
            st.write("Input", args, "Parameter")

            match args:
                case 'K-Means':
                    km_p = k_kmean_parameter()
                    st.session_state['algorithm parameter'] = km_p
                    
                case 'LTKC':
                    ltkc_p = ltkc_parameter()
                    st.session_state['algorithm parameter'] = ltkc_p

                case 'Agglomerative':
                    fcm_p = am_parameter()
                    st.session_state['algorithm parameter'] = fcm_p

                case 'DBSCAN':
                    dbscan_p = dbscan_parameter()
                    st.session_state['algorithm parameter'] = dbscan_p

                case 'HDBSCAN':
                    hdbscan_p = hdbscan_parameter()
                    st.session_state['algorithm parameter'] = hdbscan_p

                case 'Affinity Propagation':
                    ap_p = affinity_propagation_parameter()
                    st.session_state['algorithm parameter'] = ap_p

                case _:
                    st.warning("Error")
        
        with columnParams:
            st.text('Algorithm info')
            st.write(st.session_state['algorithm parameter'])


    st.markdown('### ')
    st.markdown('### Clustering')
    select = st.button("Run")

    if select:
        cc = ClusteringController(data, st.session_state['algorithm parameter'])
        result = cc.execute_clustering()
        
        dimension = st.session_state['dpMethod']['dimension']

        tabShowPlot, tabDetailResult = st.tabs(['🗃 Plotting', 'ℹ Details'])

        with tabShowPlot:
            match dimension:
                case 1:
                    st.write(dimension) 
                    st.write(st.session_state['algorithm parameter']) 
                    
                case 2:
                    st.write(dimension) 
                    st.write(st.session_state['algorithm parameter']) 
                    
                case 3:
                    st.warning('gg')

        
        with tabDetailResult:
            match result['algorithm']:
                case 'K-Means':
                    kmeans_result_detail(result)
                    



    
