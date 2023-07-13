import streamlit as st

def kmeans_parameter():
        n_cluster = st.slider('The number of clusters will be generate', 2, 20, 4)
        max_iter = st.number_input('Maximal iteration', step=10, max_value=1000, min_value=100, value=300)
        params = {
                'algorithm' : 'K-Means',
                'n_cluster' : n_cluster,
                'max_iter' : max_iter
        }
        return params


def am_parameter():
        linkage = st.selectbox('Which linkage criterion to use',
                ('ward', 'average', 'complete', 'single'))
        n_cluster = st.slider('Number of clusters to find', 2, 20, 2)
        params = {
                'algorithm' : 'Agglomerative',
                'linkage' : linkage,
                'n_cluster' : n_cluster,
        }
        return params

def dbscan_parameter():
        eps =  st.number_input('Epsilon', step=0.1, max_value=10.0, min_value=0.1, value=0.5)
        min_s = st.slider('Minimal points', 2, 100, 5)
        params = {
                'algorithm' : 'DBSCAN',
                'eps' : eps,
                'min_samples' : min_s
        }
        return params

def hdbscan_parameter():
        min_cluster_size = st.slider('Minimal cluster size', 10, 200, 15)
        min_samples = st.number_input('Minimal samples', step=5, max_value=50, min_value=1, value=5)
        cluster_selection_epsilon =  st.number_input('Cluster selection epsilon', step=0.1, max_value=10.0, min_value=0.1, value=0.5)
        params = {
                'algorithm' : 'HDBSCAN',
                'min_cluster_size' : min_cluster_size,
                'min_samples' : min_samples,
                "cluster_selection_epsilon" : cluster_selection_epsilon
        }
        return params

def optics_parameter():
        min_samples = st.slider('Minimal samples', 2, 1000, 5)
        max_eps = st.number_input('Maximal epsilon', step=0.2, max_value=10.0, min_value=0.1, value=0.5)
        params = {
                'algorithm' : 'OPTICs',
                'min_samples' : min_samples,
                'max_eps' : max_eps
        }
        return params

def meanshift_parameter():
        bandwidth = st.number_input('Bandwidth', step=0.1, max_value=10.0, min_value=0.1, value=0.2)
        max_iter = st.slider('Maximal iteration', 2, 1000, 300)
        params = {
                'algorithm' : 'MeanShift',
                'bandwidth' : bandwidth,
                'max_iter' : max_iter
        }
        return params

# def affinity_propagation_parameter():
#         damping = st.number_input('Damping factor', step=0.1, max_value=1.0, min_value=0.5, value=0.5)
#         max_iter = st.slider('Maximal iteration', 100, 1000, 200)
#         params = {
#                 'algorithm' : 'Affinity Propagation',
#                 'damping' : damping,
#                 'max_iter' : max_iter,
#         }
#         return params