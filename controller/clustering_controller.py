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
            case 'K-Means':
                cluster = clustering.kmeans(self.algo['n_cluster'], self.algo['max_iter'])
                count_cluster = int(max(cluster['result'].labels_)+1)

                new_eval =  {         
                    "dataset": st.session_state['fileName'],
                    "clustering": self.algo['algorithm'],
                    "extraction": st.session_state['dpMethod'][ 'extraction'],
                    "cluster": count_cluster,
                    "indexScore": cluster['indexScore'],
                    "dbScore": cluster['dbScore'],
                    "time": cluster['time'],
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

                return cluster


            case 'Agglomerative':
                cluster = clustering.agglomerative(self.algo['n_cluster'], self.algo['linkage'])
                count_cluster = int(max(cluster['result'].labels_)+1)

                new_eval =  {         
                    "dataset": st.session_state['fileName'],
                    "clustering": self.algo['algorithm'],
                    "extraction": st.session_state['dpMethod'][ 'extraction'],
                    "cluster": count_cluster,
                    "indexScore": cluster['indexScore'],
                    "dbScore": cluster['dbScore'],
                    "time": cluster['time'],
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

                return cluster
            

            case 'DBSCAN':
                cluster = clustering.dbscan(self.algo['eps'], self.algo['min_samples'])
                count_cluster = int(max(cluster['result'].labels_)+1)

                new_eval =  {         
                    "dataset": st.session_state['fileName'],
                    "clustering": self.algo['algorithm'],
                    "extraction": st.session_state['dpMethod'][ 'extraction'],
                    "cluster": count_cluster,
                    "indexScore": cluster['indexScore'],
                    "dbScore": cluster['dbScore'],
                    "time": cluster['time'],
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

                return cluster
            

            case 'HDBSCAN':
                cluster = clustering.hdbscan(self.algo['min_samples'], self.algo['min_cluster_size'], self.algo['cluster_selection_epsilon'])
                count_cluster = int(max(cluster['result'].labels_)+1)

                new_eval =  {         
                    "dataset": st.session_state['fileName'],
                    "clustering": self.algo['algorithm'],
                    "extraction": st.session_state['dpMethod'][ 'extraction'],
                    "cluster": count_cluster,
                    "indexScore": cluster['indexScore'],
                    "dbScore": cluster['dbScore'],
                    "time": cluster['time'],
                    "details":{
                        "clustering_parameter": [
                            "min_samples",
                            "min_cluster_size",
                            "cluster_selection_epsilon"
                        ],
                        "parameter_value": [
                            self.algo['min_samples'],
                            self.algo['min_cluster_size'],
                            self.algo['cluster_selection_epsilon']
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

                return cluster
            

            
            case 'OPTICs':
                cluster = clustering.optics(self.algo['min_samples'], self.algo['max_eps'])
                count_cluster = int(max(cluster['result'].labels_)+1)

                new_eval =  {         
                    "dataset": st.session_state['fileName'],
                    "clustering": self.algo['algorithm'],
                    "extraction": st.session_state['dpMethod'][ 'extraction'],
                    "cluster": count_cluster,
                    "indexScore": cluster['indexScore'],
                    "dbScore": cluster['dbScore'],
                    "time": cluster['time'],
                    "details":{
                        "clustering_parameter": [
                            "min_samples",
                            "max_eps"
                        ],
                        "parameter_value": [
                            self.algo['min_samples'],
                            self.algo['max_eps']
                        ]
                    }
                }
                        # Membaca file JSON yang sudah ada
                with open('evaluation/optics.json', 'r') as file:
                    existing_result = json.load(file)

                # Menambahkan data baru ke objek JSON yang sudah ada
                existing_result.append(new_eval)

                # Menulis ulang objek JSON ke file
                with open('evaluation/optics.json', 'w') as file:
                    json.dump(existing_result, file, indent=4)

                return cluster
            
            case 'MeanShift':
                cluster = clustering.meanshift(self.algo['bandwidth'], self.algo['max_iter'])
                count_cluster = int(max(cluster['result'].labels_)+1)
                
                new_eval =  {         
                    "dataset": st.session_state['fileName'],
                    "clustering": self.algo['algorithm'],
                    "extraction": st.session_state['dpMethod'][ 'extraction'],
                    "cluster": count_cluster,
                    "indexScore": cluster['indexScore'],
                    "dbScore": cluster['dbScore'],
                    "time": cluster['time'],
                    "details":{
                        "clustering_parameter": [
                            "bandwidth",
                            "max_iter"
                        ],
                        "parameter_value": [
                            self.algo['bandwidth'],
                            self.algo['max_iter']
                        ]
                    }
                }
                        # Membaca file JSON yang sudah ada
                with open('evaluation/meanshift.json', 'r') as file:
                    existing_result = json.load(file)

                # Menambahkan data baru ke objek JSON yang sudah ada
                existing_result.append(new_eval)

                # Menulis ulang objek JSON ke file
                with open('evaluation/meanshift.json', 'w') as file:
                    json.dump(existing_result, file, indent=4)

                return cluster
            


            # case 'DENCLUE':
            #     cluster = clustering.denclue(self.algo['epsilon'], self.algo['min_samples'])
            #     new_eval =  {         
            #         "dataset": st.session_state['fileName'],
            #         "clustering": self.algo['algorithm'],
            #         "extraction": st.session_state['dpMethod'][ 'extraction'],
            #         "indexScore": cluster['indexScore'],
            #         "dbScore": cluster['dbScore'],
            #         "time": cluster['time'],
            #         "details":{
            #             "clustering_parameter": [
            #                 "epsilon",
            #                 "min_samples"
            #             ],
            #             "parameter_value": [
            #                 self.algo['epsilon'],
            #                 self.algo['min_samples']
            #             ]
            #         }
            #     }
            #             # Membaca file JSON yang sudah ada
            #     with open('evaluation/denclue.json', 'r') as file:
            #         existing_result = json.load(file)

            #     # Menambahkan data baru ke objek JSON yang sudah ada
            #     existing_result.append(new_eval)

            #     # Menulis ulang objek JSON ke file
            #     with open('evaluation/denclue.json', 'w') as file:
            #         json.dump(existing_result, file, indent=4)

            #     return cluster
            
            

            # case 'Affinity Propagation':
            #     ap = clustering.affinity_propagation(self.algo['damping'], self.algo['max_iter'])
            #     new_eval =  {         
            #         "dataset": st.session_state['fileName'],
            #         "clustering": self.algo['algorithm'],
            #         "extraction": st.session_state['dpMethod'][ 'extraction'],
            #         "score": ap['score'],
            #         "time": ap['time'],
            #         "details":{
            #             "clustering_parameter": [
            #                 "damping",
            #                 "max_iter"
            #             ],
            #             "parameter_value": [
            #                 self.algo['damping'],
            #                 self.algo['max_iter']
            #             ]
            #         }
            #     }
            #             # Membaca file JSON yang sudah ada
            #     with open('evaluation/ap.json', 'r') as file:
            #         existing_result = json.load(file)

            #     # Menambahkan data baru ke objek JSON yang sudah ada
            #     existing_result.append(new_eval)

            #     # Menulis ulang objek JSON ke file
            #     with open('evaluation/ap.json', 'w') as file:
            #         json.dump(existing_result, file, indent=4)

            #     return ap