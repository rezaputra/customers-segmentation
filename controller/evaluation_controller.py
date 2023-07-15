import streamlit as st
import json
from components.detail_evaluation import dataset_based_view, algorithm_based_view


class Evaluation:
    def __init__(self, b):
        self.basedOn = b

    # @st.cache(allow_output_mutation=True)
    def datasetBased(self):
        kmeans = self.openEvalData('K-Means', False)
        agglomerative = self.openEvalData('Agglomerative', False)
        dbscan = self.openEvalData('DBSCAN', False)
        hdbscan = self.openEvalData('HDBSCAN', False)
        optics = self.openEvalData('OPTICs', False)
        meanshift = self.openEvalData('MeanShift', False)
        hdbcsan_pca = self.openEvalData('HDBSCAN', "PCA")

        dataset1 = [kmeans['onlineretail.csv'], agglomerative['onlineretail.csv'], dbscan['onlineretail.csv'], hdbscan['onlineretail.csv'], optics['onlineretail.csv'], meanshift['onlineretail.csv'], hdbcsan_pca['onlineretail.csv']]
        dataset2 = [kmeans['bankchurners.csv'], agglomerative['bankchurners.csv'], dbscan['bankchurners.csv'], hdbscan['bankchurners.csv'], optics['bankchurners.csv'], meanshift['bankchurners.csv'], hdbcsan_pca['bankchurners.csv']]
        dataset3 = [kmeans['dwimedialestari.csv'], agglomerative['dwimedialestari.csv'], dbscan['dwimedialestari.csv'], hdbscan['dwimedialestari.csv'], optics['dwimedialestari.csv'], meanshift['dwimedialestari.csv'], hdbcsan_pca['dwimedialestari.csv']]

        sort_dataset1 = self.sortingData(dataset1)
        sort_dataset2 = self.sortingData(dataset2)
        sort_dataset3 = self.sortingData(dataset3)

        dataset_based_view(sort_dataset1, sort_dataset2, sort_dataset3, self.basedOn['rank_type'])

        # dataset_based_view(dataset1, dataset2, dataset3, self.basedOn['rank_type'])

    def algorithmBased(self):
        jd = {
            'kmeans' : self.openEvalData('K-Means', False),
            'agglomerative' : self.openEvalData('Agglomerative', False),
            'dbscan' : self.openEvalData('DBSCAN', False),
            'hdbscan' : self.openEvalData('HDBSCAN', False),
            'optics' : self.openEvalData('OPTICs', False),
            'meanshift' : self.openEvalData('MeanShift', False),
            'hdbscan_pca' : self.openEvalData('HDBSCAN', "PCA")
        }

        algorithm_based_view(jd, self.basedOn['rank_type'])


    def openEvalData(self, a, e):
        algo = a
        extraction = e
        match algo:
            case "K-Means":
                with open('evaluation/kmeans.json', 'r') as file:
                    json_data = json.load(file)
                    dataEval = self.getBest(json_data)                   

            case "Agglomerative":
                with open('evaluation/agglomerative.json', 'r') as file:
                    json_data = json.load(file)
                    dataEval = self.getBest(json_data)

            case "DBSCAN":
                with open('evaluation/dbscan.json', 'r') as file:
                    json_data = json.load(file)
                    dataEval = self.getBest(json_data)

            case "HDBSCAN":
                with open('evaluation/hdbscan.json', 'r') as file:
                    json_data = json.load(file)
                    if extraction == "PCA":
                        dataEval = self.getBestPCA(json_data)
                    else:
                        dataEval = self.getBest(json_data)

            case "OPTICs":
                with open('evaluation/optics.json', 'r') as file:
                    json_data = json.load(file)
                    dataEval = self.getBest(json_data)

            case "MeanShift":
                with open('evaluation/meanshift.json', 'r') as file:
                    json_data = json.load(file)
                    dataEval = self.getBest(json_data)

        return dataEval
    

    def getBest(self, jd):
        json_d = jd
        filter_dataset1 = [item for item in json_d if item["dataset"] == "onlineretail.csv" and item["cluster"] == self.basedOn['cluster_dataset1'] and item["extraction"] == False]
        filter_dataset2 = [item for item in json_d if item["dataset"] == "bankchurners.csv" and item["cluster"] == self.basedOn['cluster_dataset2'] and item["extraction"] == False]
        filter_dataset3 = [item for item in json_d if item["dataset"] == "dwimedialestari.csv" and item["cluster"] == self.basedOn['cluster_dataset3'] and item["extraction"] == False]
        match self.basedOn['rank_type']:
            case "Silhouette score":
                max_dataset1 = max(filter_dataset1, key=lambda x: x["indexScore"])
                max_dataset2 = max(filter_dataset2, key=lambda x: x["indexScore"])
                max_dataset3 = max(filter_dataset3, key=lambda x: x["indexScore"])
            case "Davies–Bouldin score":
                max_dataset1 = min(filter_dataset1, key=lambda x: x["dbScore"])
                max_dataset2 = min(filter_dataset2, key=lambda x: x["dbScore"])
                max_dataset3 = min(filter_dataset3, key=lambda x: x["dbScore"])
            case "Computation time":
                max_dataset1 = min(filter_dataset1, key=lambda x: x["time"])
                max_dataset2 = min(filter_dataset2, key=lambda x: x["time"])
                max_dataset3 = min(filter_dataset3, key=lambda x: x["time"])

        best_data = {
            'onlineretail.csv' : max_dataset1, 
            'bankchurners.csv' : max_dataset2, 
            'dwimedialestari.csv' : max_dataset3, 
        }

        return best_data
    
    def getBestPCA(self, jd):
        json_d = jd
        filter_dataset1 = [item for item in json_d if item["dataset"] == "onlineretail.csv" and item["cluster"] == self.basedOn['cluster_dataset1'] and item["extraction"] == "PCA"]
        filter_dataset2 = [item for item in json_d if item["dataset"] == "bankchurners.csv" and item["cluster"] == self.basedOn['cluster_dataset2'] and item["extraction"] == "PCA"]
        filter_dataset3 = [item for item in json_d if item["dataset"] == "dwimedialestari.csv" and item["cluster"] == self.basedOn['cluster_dataset3'] and item["extraction"] == "PCA"]
        match self.basedOn['rank_type']:
            case "Silhouette score":
                max_dataset1 = max(filter_dataset1, key=lambda x: x["indexScore"])               
                max_dataset2 = max(filter_dataset2, key=lambda x: x["indexScore"])
                max_dataset3 = max(filter_dataset3, key=lambda x: x["indexScore"])
            case "Davies–Bouldin score":
                max_dataset1 = max(filter_dataset1, key=lambda x: x["dbScore"])
                max_dataset2 = max(filter_dataset2, key=lambda x: x["dbScore"])
                max_dataset3 = max(filter_dataset3, key=lambda x: x["dbScore"])
            case "Computation time":
                max_dataset1 = max(filter_dataset1, key=lambda x: x["time"])
                max_dataset2 = max(filter_dataset2, key=lambda x: x["time"])
                max_dataset3 = max(filter_dataset3, key=lambda x: x["time"])

        max_dataset1['clustering'] = max_dataset1['clustering'] + " + " + max_dataset1['extraction']
        max_dataset2['clustering'] = max_dataset2['clustering'] + " + " + max_dataset2['extraction']
        max_dataset3['clustering'] = max_dataset3['clustering'] + " + " + max_dataset3['extraction']

        best_data = {
            'onlineretail.csv' : max_dataset1, 
            'bankchurners.csv' : max_dataset2, 
            'dwimedialestari.csv' : max_dataset3, 
        }

        return best_data
    

    def sortingData(self, od):
        object_data = od
        match self.basedOn['rank_type']:
            case "Silhouette score":
                sort_data = sorted(object_data, key=lambda x: x['indexScore'], reverse=True)                
            case "Davies–Bouldin score":
                sort_data = sorted(object_data, key=lambda x: x['dbScore'], reverse=False)
            case "Computation time":
                sort_data = sorted(object_data, key=lambda x: x['time'], reverse=False)

        
        return sort_data

    
