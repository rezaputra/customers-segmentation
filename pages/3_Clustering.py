import streamlit as st
import pandas as pd
from components.get_clustering_parameter import *
from components.detail_clustering_result import *
from components.plotting_cluster import *
from controller.clustering_controller import ClusteringController
from components.plotting import clustering_result_two_dimension


if 'dataPreparation' in st.session_state:
    dpTime = st.session_state['dpTimeProcessing'].copy()
    dpMethod = st.session_state['dpMethod'].copy()
    dpResult = pd.DataFrame(st.session_state['dataPreparation'].copy())
    id = pd.DataFrame(st.session_state['datasetId'].copy())

    st.markdown('### Clustering Algorithm Options')
    columnInputAlgorithm, columnInputParameter, columnParams = st.columns([1,1,1], gap='large')

    with columnInputAlgorithm:
        algorithm = st.radio("Please select clustering algorithm ",
            ["K-Means", "LTKC", "Agglomerative","DBSCAN", "HDBSCAN", "Affinity Propagation"],
            index=1, key="input_algo")
        
        
        isPlot = st.checkbox('Plot ' + algorithm, value=1)
        
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
        cc = ClusteringController(dpResult, st.session_state['algorithm parameter'])
        result = cc.execute_clustering()
        dpResult['CLUSTER'] = result['result'].labels_
        if 'ID' not in dpResult.columns:
            dpResult.insert(loc=0, column='ID', value=id.values)  
        result['labeled'] = dpResult


        if isPlot:
            tabShowPlot, tabDetailResult = st.tabs(['🗃 Plotting', 'ℹ Details'])

            with tabShowPlot:
                plotcol, recapcol = st.columns([3,1], gap='small')
                match dpMethod['dimension']:
                    case 2:
                        with plotcol:
                            clustering_result_two_dimension(dpResult)
                            st.caption(algorithm + " 2D Plotting")
                            try:
                                st.image('img/cluster_plot2d.png', width=700)
                            except:
                                st.warning('Something was wrong!')
                        with recapcol:
                            st.caption('')
                            st.caption('')
                            st.caption('')
                            st.caption('')
                            st.caption('')
                            st.caption('')
                            st.caption('Recaps')
                            st.write('Computation time :',round(result['time'], 4))
                            st.write('Total cluster :', max(result['result'].labels_) + 1)    
                            st.write('Silhouette score :', round(result['score'], 4))    
                        
                    case 2:
                        st.write(st.session_state['algorithm parameter'])              
    
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
    
