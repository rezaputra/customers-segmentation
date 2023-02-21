import streamlit as st

def k_kmean_parameter():
        n_cluster = st.slider('The number of clusters will be generate', 2, 20, 4)
        max_iter = st.number_input('Maximal iteration', step=10, max_value=1000, min_value=100, value=300)
        params = {
                'algorithm' : 'K-means',
                'n_cluster' : n_cluster,
                'max_iter' : max_iter
        }
        return params

def ltkc_parameter():   
        k_value = st.slider('The number of k-value', 2, 100, 20)
        params = {
                'algorithm' : 'LTKC',
                'k_value' : k_value,
        }
        return params

def am_parameter():
        linkage = st.selectbox('Which linkage criterion to use',
                ('ward', 'average', 'complete', 'single'))
        n_cluster = st.slider('The number of clusters to find', 2, 10, 2)
        params = {
                'algorithm' : 'Agglomerative',
                'linkage' : linkage,
                'n_cluster' : n_cluster,
        }
        return params

def dbscan_parameter():
        eps =  st.number_input('Epsilon', step=0.2, max_value=10.0, min_value=0.1, value=0.5)
        min_p = st.slider('Minimal points', 2, 20, 5)
        params = {
                'algorithm' : 'DBSCAN',
                'eps' : eps,
                'min_samples' : min_p,
        }
        return params

def hdbscan_parameter():
        min_samples = st.number_input('Minimal samples', step=1, max_value=20, min_value=1, value=2)
        min_cluster_size = st.slider('Minimal cluster size', 2, 100, 15)
        params = {
                'algorithm' : 'HDBSCAN',
                'min_samples' : min_samples,
                'min_cluster_size' : min_cluster_size,
        }
        return params

def affinity_propagation_parameter():
        damping = st.number_input('Damping factor', step=0.1, max_value=1.0, min_value=0.5, value=0.5)
        max_iter = st.slider('Maximal iteration', 100, 1000, 200)
        params = {
                'algorithm' : 'Affinity Propagation',
                'damping' : damping,
                'max_iter' : max_iter,
        }
        return params