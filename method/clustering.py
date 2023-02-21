import streamlit as st
import pandas as pd
import time
from hdbscan import HDBSCAN
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN, AffinityPropagation
from sklearn.metrics import silhouette_score



class Clustering:
    def __init__(self, d):
        self.data = pd.DataFrame(d)


    def kMeans(self, n_cluster, max_iter):
        startTime = time.time()
        km = KMeans(n_clusters=n_cluster, max_iter=max_iter, n_init='auto')
        fit = km.fit(self.data)
        endTime = time.time() - startTime
        
        score = silhouette_score(self.data, fit.labels_)

        result = {
            'algorithm' : 'K-Means',
            'result' : fit,
            'score' : score,
            'time' : endTime
        }

        return result
    

    def ltkc(self, k_value):
        result = {
            'algorithm' : 'LTKC',
            'result' : False,
            'score' : False,
            'time' : False
        }

        return result
    
    
    def agglomerative(self, n_cluster, linkage):
        startTime = time.time()
        agglo = AgglomerativeClustering(n_clusters=n_cluster, linkage=linkage)
        fit = agglo.fit(self.data)
        endTime = time.time() - startTime

        score = silhouette_score(self.data, fit.labels_)

        result = {
            'algorithm' : 'Agglomerative',
            'result' : fit,
            'score' : score,
            'time' : endTime
        }

        return result
    
    
    def dbscan(self, eps, min_samples):
        startTime = time.time()
        db = DBSCAN(eps=eps, min_samples=min_samples)
        fit = db.fit(self.data)
        endTime = time.time() - startTime
        
        score = silhouette_score(self.data, fit.labels_)

        result = {
            'algorithm' : 'DBSCAN',
            'result' : fit,
            'score' : score,
            'time' : endTime
        }

        return result
    
    
    def hdbscan(self, min_samples, min_cluster_size):
        startTime = time.time()
        hdb = HDBSCAN(min_samples=min_samples, min_cluster_size=min_cluster_size)
        fit = hdb.fit(self.data)
        endTime = time.time() - startTime

        score = silhouette_score(self.data, fit.labels_)

        result = {
            'algorithm' : 'HDBSCAN',
            'result' : fit,
            'score' : score,
            'time' : endTime
        }

        return result
    
    
    def affinity_propagation(self, damping, max_iter):
        startTime = time.time()
        ap = AffinityPropagation(damping=damping, max_iter=max_iter)
        fit = ap.fit(self.data)
        endTime = time.time() - startTime

        score = silhouette_score(self.data, fit.labels_)

        result = {
            'algorithm' : 'Affinity Propagation',
            'result' : fit,
            'score' : score,
            'time' : endTime
        }

        return result