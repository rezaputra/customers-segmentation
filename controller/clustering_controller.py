import streamlit as st
from method.clustering import Clustering
import json

class ClusteringController:
    def __init__(self, d, a):
         self.data = d
         self.algo = a

    # @st.cache(allow_output_mutation=True)
    def execute_clustering(self):
        clustering  = Clustering(self.data)


        match self.algo['algorithm']:
            case 'K-means':
                km = clustering.kMeans(self.algo['n_cluster'], self.algo['max_iter'])

                new_eval =  {         
                    "dataset": st.session_state['fileName'],
                    "clustering": self.algo['algorithm'],
                    "extraction": st.session_state['dpMethod'][ 'extraction'],
                    "score": km['score'],
                    "time": km['time'],
                    "details":{
                        "clustering_parameter": [
                            "n_cluster",
                            "max_iter"
                        ],
                        "parameter_value": [
                            self.algo['n_cluster'],
                            self.algo['max_iter']
                        ]
                    }
                }
                        # Membaca file JSON yang sudah ada
                with open('evaluation/kmeans.json', 'r') as file:
                    existing_result = json.load(file)

                # Menambahkan data baru ke objek JSON yang sudah ada
                existing_result.append(new_eval)

                # Menulis ulang objek JSON ke file
                with open('evaluation/kmeans.json', 'w') as file:
                    json.dump(existing_result, file, indent=4)

                return km


            case 'Agglomerative':
                agglo = clustering.agglomerative(self.algo['n_cluster'], self.algo['linkage'])
                new_eval =  {         
                    "dataset": st.session_state['fileName'],
                    "clustering": self.algo['algorithm'],
                    "extraction": st.session_state['dpMethod'][ 'extraction'],
                    "score": agglo['score'],
                    "time": agglo['time'],
                    "details":{
                        "clustering_parameter": [
                            "n_cluster",
                            "linkage"
                        ],
                        "parameter_value": [
                            self.algo['n_cluster'],
                            self.algo['linkage']
                        ]
                    }
                }
                        # Membaca file JSON yang sudah ada
                with open('evaluation/agglomerative.json', 'r') as file:
                    existing_result = json.load(file)

                # Menambahkan data baru ke objek JSON yang sudah ada
                existing_result.append(new_eval)

                # Menulis ulang objek JSON ke file
                with open('evaluation/agglomerative.json', 'w') as file:
                    json.dump(existing_result, file, indent=4)

                return agglo
            

            case 'DBSCAN':
                dbscan = clustering.dbscan(self.algo['eps'], self.algo['min_samples'])
                new_eval =  {         
                    "dataset": st.session_state['fileName'],
                    "clustering": self.algo['algorithm'],
                    "extraction": st.session_state['dpMethod'][ 'extraction'],
                    "score": dbscan['score'],
                    "time": dbscan['time'],
                    "details":{
                        "clustering_parameter": [
                            "eps",
                            "min_samples"
                        ],
                        "parameter_value": [
                            self.algo['eps'],
                            self.algo['min_samples']
                        ]
                    }
                }
                        # Membaca file JSON yang sudah ada
                with open('evaluation/dbscan.json', 'r') as file:
                    existing_result = json.load(file)

                # Menambahkan data baru ke objek JSON yang sudah ada
                existing_result.append(new_eval)

                # Menulis ulang objek JSON ke file
                with open('evaluation/dbscan.json', 'w') as file:
                    json.dump(existing_result, file, indent=4)

                return dbscan
            

            case 'HDBSCAN':
                hdbscan = clustering.hdbscan(self.algo['min_samples'], self.algo['min_cluster_size'])
                new_eval =  {         
                    "dataset": st.session_state['fileName'],
                    "clustering": self.algo['algorithm'],
                    "extraction": st.session_state['dpMethod'][ 'extraction'],
                    "score": hdbscan['score'],
                    "time": hdbscan['time'],
                    "details":{
                        "clustering_parameter": [
                            "min_samples",
                            "min_cluster_size"
                        ],
                        "parameter_value": [
                            self.algo['min_samples'],
                            self.algo['min_cluster_size']
                        ]
                    }
                }
                        # Membaca file JSON yang sudah ada
                with open('evaluation/hdbscan.json', 'r') as file:
                    existing_result = json.load(file)

                # Menambahkan data baru ke objek JSON yang sudah ada
                existing_result.append(new_eval)

                # Menulis ulang objek JSON ke file
                with open('evaluation/hdbscan.json', 'w') as file:
                    json.dump(existing_result, file, indent=4)

                return hdbscan

            case 'Affinity Propagation':
                ap = clustering.affinity_propagation(self.algo['damping'], self.algo['max_iter'])
                new_eval =  {         
                    "dataset": st.session_state['fileName'],
                    "clustering": self.algo['algorithm'],
                    "extraction": st.session_state['dpMethod'][ 'extraction'],
                    "score": ap['score'],
                    "time": ap['time'],
                    "details":{
                        "clustering_parameter": [
                            "damping",
                            "max_iter"
                        ],
                        "parameter_value": [
                            self.algo['damping'],
                            self.algo['max_iter']
                        ]
                    }
                }
                        # Membaca file JSON yang sudah ada
                with open('evaluation/ap.json', 'r') as file:
                    existing_result = json.load(file)

                # Menambahkan data baru ke objek JSON yang sudah ada
                existing_result.append(new_eval)

                # Menulis ulang objek JSON ke file
                with open('evaluation/ap.json', 'w') as file:
                    json.dump(existing_result, file, indent=4)

                return ap