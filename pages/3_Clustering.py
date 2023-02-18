import streamlit as st
import pandas as pd
from components.algo_parameter import *
from controller.clustering_controller import ClusteringController


if 'clusteringData' in st.session_state:
    data = st.session_state['clusteringData']
    dpTime = st.session_state['dpTimeProcessing']
    dpMethod = st.session_state['dpMethod']
    df = pd.DataFrame(data)

    st.markdown('### Choose Clustering Algorithm')


    columnInputAlgorithm, columnInputParameter, empty, columnParams = st.columns([1,1,0.25,1])

    with columnInputAlgorithm:
        algorithm = st.radio("Select Clustering Algorithm",
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
            st.text('Algorithm')
            st.write(st.session_state['algorithm parameter'])


    st.markdown('### Clustering')
    select = st.button("Run")

    if select:
        algo = st.session_state['algorithm parameter']
        st.write(algo)

        cc = ClusteringController(data, algo)

        result  = cc.execute_clustering()

        st.write(result)




    
