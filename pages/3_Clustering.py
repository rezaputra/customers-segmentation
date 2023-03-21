import streamlit as st
import pandas as pd
from components.get_clustering_parameter import *
from components.detail_clustering_result import *
from components.plotting_cluster import *
from controller.clustering_controller import ClusteringController


if 'dataPreparation' in st.session_state:
    data = st.session_state['dataPreparation'].copy()
    dpTime = st.session_state['dpTimeProcessing'].copy()
    dpMethod = st.session_state['dpMethod'].copy()
    id = st.session_state['datasetId'].copy()
    df = pd.DataFrame(data)

    st.markdown('### Clustering Algorithm Options')
    columnInputAlgorithm, columnInputParameter, columnParams = st.columns([1,1,1], gap='large')

    with columnInputAlgorithm:
        algorithm = st.radio("Please select clustering algorithm will be use to cluster the dataset",
            ["K-Means", "LTKC", "Agglomerative","DBSCAN", "HDBSCAN", "Affinity Propagation"],
            index=1, key="input_algo")
        
        
        isPlot = st.checkbox('Plot ' + algorithm, value=0)
        
        # st.caption(algorithm)

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
    # select = st.button("Run")

    if st.button("Run"):
        if isPlot:
            cc = ClusteringController(data, st.session_state['algorithm parameter'])
            result = cc.execute_clustering()

            tabShowPlot, tabDetailResult = st.tabs(['🗃 Plotting', 'ℹ Details'])

            with tabShowPlot:
                match result['algorithm']:
                    case 'K-Means':
                        kmPlot = PlottingKMeans(result)
                        kmPlot.execute_plotting()
                        
                    case 'Agglomerative':
                        st.write(st.session_state['algorithm parameter']) 
                        
                    case 'DBSCAN':
                        st.warning('gg')

                    case 'HDBSCAN':
                        st.warning('gg')

                    case 'Affinity Propagation':
                        st.warning('gg')
                        
    
            with tabDetailResult:
                st.caption('')
                match result['algorithm']:
                    case 'K-Means':
                        kmeans_result_detail(result)
                    case 'Agglomerative':
                        agglomerative_result_detail(result)
                    case 'DBSCAN':
                        dbscan_detail(result)
                    case 'HDBSCAN':
                        hdbscan_detail(result)
                    case 'Affinity Propagation':
                        affinity_propagation_detail(result)

        else:
            cc = ClusteringController(data, st.session_state['algorithm parameter'])
            result = cc.execute_clustering()

            st.caption('')
            match result['algorithm']:
                case 'K-Means':
                    kmeans_result_detail(result)
                case 'Agglomerative':
                    agglomerative_result_detail(result)
                case 'DBSCAN':
                    dbscan_detail(result)
                case 'HDBSCAN':
                    hdbscan_detail(result)
                case 'Affinity Propagation':
                    affinity_propagation_detail(result)


# st.write(st.session_state['dataPreparation'])
    
