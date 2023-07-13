import pandas as pd
import time
import streamlit as st
from hdbscan import HDBSCAN
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN, OPTICS, MeanShift
from sklearn.metrics import silhouette_score, davies_bouldin_score



class Clustering:
    def __init__(self, d):
        self.data = pd.DataFrame(d)
        # self.rawData = st.session_state['dataPreparation']



    def hdbscan(self,mcs, ms, cse):
        startTime = time.time()
        hdb = HDBSCAN(max_cluster_size=mcs, min_samples=ms, cluster_selection_epsilon=cse, algorithm='boruvka_kdtree')
        fit = hdb.fit(self.data)
        endTime = time.time() - startTime

        indexScore = silhouette_score(st.session_state['data_scale'], fit.labels_)
        dbScore = davies_bouldin_score(st.session_state['data_scale'], fit.labels_)

        result = {
            'algorithm' : 'HDBSCAN',
            'result' : fit,
            'indexScore' : indexScore,
            'dbScore' : dbScore,
            'time' : endTime
        }

        return result
    

    
    def kmeans(self, k, mi):
        startTime = time.time()
        km = KMeans(n_clusters=k, max_iter=mi)
        fit = km.fit(self.data)
        endTime = time.time() - startTime

        indexScore = silhouette_score(st.session_state['data_scale'], fit.labels_)
        dbScore = davies_bouldin_score(st.session_state['data_scale'], fit.labels_)

        result = {
            'algorithm' : 'K-Means',
            'result' : fit,
            'indexScore' : indexScore,
            'dbScore' : dbScore,
            'time' : endTime
        }

        return result
    

    def optics(self, ms, me):
        startTime = time.time()
        cluster = OPTICS(min_samples=ms, max_eps=me)
        fit = cluster.fit(self.data)
        endTime = time.time() - startTime

        indexScore = silhouette_score(st.session_state['data_scale'], fit.labels_)
        dbScore = davies_bouldin_score(st.session_state['data_scale'], fit.labels_)

        result = {
            'algorithm' : 'OPTICs',
            'result' : fit,
            'indexScore' : indexScore,
            'dbScore' : dbScore,
            'time' : endTime
        }

        return result
    

    
    def agglomerative(self, nc, li):
        startTime = time.time()
        cluster = AgglomerativeClustering(n_clusters=nc, linkage=li)
        fit = cluster.fit(self.data)
        endTime = time.time() - startTime

        indexScore = silhouette_score(st.session_state['data_scale'], fit.labels_)
        dbScore = davies_bouldin_score(st.session_state['data_scale'], fit.labels_)

        result = {
            'algorithm' : 'Agglomerative',
            'result' : fit,
            'indexScore': indexScore,
            'dbScore' : dbScore,
            'time' : endTime
        }
        return result
    
    
    def dbscan(self, eps, ms):
        startTime = time.time()
        cluster = DBSCAN(eps=eps, min_samples=ms)
        fit = cluster.fit(self.data)
        endTime = time.time() - startTime
        
        indexScore = silhouette_score(st.session_state['data_scale'], fit.labels_)
        dbScore = davies_bouldin_score(st.session_state['data_scale'], fit.labels_)

        result = {
            'algorithm' : 'DBSCAN',
            'result' : fit,
            'indexScore': indexScore,
            'dbScore' : dbScore,
            'time' : endTime
        }

        return result
    

    def meanshift(self,bw, mi):
        startTime = time.time()
        cluster = MeanShift(bandwidth=bw, max_iter=mi)
        fit = cluster.fit(self.data)
        endTime = time.time() - startTime
        
        indexScore = silhouette_score(st.session_state['data_scale'], fit.labels_)
        dbScore = davies_bouldin_score(st.session_state['data_scale'], fit.labels_)

        result = {
            'algorithm' : 'Mean Shift',
            'result' : fit,
            'indexScore': indexScore,
            'dbScore' : dbScore,
            'time' : endTime
        }

        return result
    
    


    
    # def denclue(self, eps, ms):
    #     startTime = time.time()
    #     cluster = DBSCAN(eps=eps, min_samples=ms)
    #     fit = cluster.fit(self.data)
    #     endTime = time.time() - startTime
        
    #     indexScore = silhouette_score(st.session_state['data_scale'], fit.labels_)
    #     dbScore = davies_bouldin_score(st.session_state['data_scale'], fit.labels_)

    #     result = {
    #         'algorithm' : 'DBSCAN',
    #         'result' : fit,
    #         'indexScore': indexScore,
    #         'dbScore' : dbScore,
    #         'time' : endTime
    #     }

    #     return result

    
    
    # def affinity_propagation(self, damping, max_iter):
    #     startTime = time.time()
    #     ap = AffinityPropagation(damping=damping, max_iter=max_iter)
    #     fit = ap.fit(self.data)
    #     endTime = time.time() - startTime

    #     score = silhouette_score(self.data, fit.labels_)

    #     result = {
    #         'algorithm' : 'Affinity Propagation',
    #         'result' : fit,
    #         'score' : score,
    #         'time' : endTime
    #     }

    #     return result
    

    # def ltkc(self, k_value):
    #     result = {
    #         'algorithm' : 'LTKC',
    #         'result' : False,
    #         'score' : False,
    #         'time' : False
    #     }

    #     return result
    