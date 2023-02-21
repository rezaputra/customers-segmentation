import streamlit as st
from method.clustering import Clustering

class ClusteringController:
    def __init__(self, d, a):
         self.data = d
         self.algo = a

    @st.cache
    def execute_clustering(self):
        clustering  = Clustering(self.data)
        match self.algo['algorithm']:

            case 'K-means':
                km = clustering.kMeans(self.algo['n_cluster'], self.algo['max_iter'])
                return km
                
            case 'LTKC':
                ltkc = clustering.ltkc(self.algo['k_value'])
                return ltkc

            case 'Agglomerative':
                agglo = clustering.agglomerative(self.algo['n_cluster'], self.algo['linkage'])
                return agglo

            case 'DBSCAN':
                dbscan = clustering.dbscan(self.algo['eps'], self.algo['min_samples'])
                return dbscan

            case 'HDBSCAN':
                hdbscan = clustering.hdbscan(self.algo['min_samples'], self.algo['min_cluster_size'])
                return hdbscan

            case 'Affinity Propagation':
                ap = clustering.affinity_propagation(self.algo['damping'], self.algo['max_iter'])
                return ap