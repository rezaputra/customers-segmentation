import pandas as pd
import hdbscan
import sklearn.cluster
import streamlit as st

class Clustering:
    def __init__(self, d):
        self.data = pd.DataFrame(d)

    def kMeans(self, n_cluster, max_iter):
        st.write(n_cluster,max_iter)
        return 1
    
    def ltkc(self, k_value):
        st.write(k_value)
        return 2
    
    def agglomerative(self, n_cluster, matrix):
        st.write(n_cluster,matrix)
        return 3
    
    def dbscan(self, eps, min_samples):
        st.write(eps, min_samples)
        return 4
    
    def hdbscan(self, min_samples, min_cluster_size):
        st.write(min_samples, min_cluster_size)
        return 5
    
    def affinity_propagation(self, damping, max_iter):
        st.write(damping, max_iter)
        return 6