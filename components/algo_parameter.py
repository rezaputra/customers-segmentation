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
        
        n_value = st.slider('The number of clusters will be generate', 2, 100, 20)
        
        params = {
                'algorithm' : 'LTKC',
                'n_value' : n_value,
        }
        return params

def fcm_parameter():
        return 3

def dbscan_parameter():
        return 4

def hdbscan_parameter():
        return 5

def single_linkage_parameter():
        return 6