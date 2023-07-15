import streamlit as st
import json
from controller.evaluation_controller import Evaluation


# Membaca file JSON yang sudah ada
with open('evaluation/dataset.json', 'r') as file:
    dataset_names = json.load(file)

if len(dataset_names) != 0:
    st.subheader("Comparing Clustering Results")
    st.caption("")

    colCluster, colDataset, colInfo = st.columns([1,1,1], gap="large")

    with colCluster:
        cluster_dataset1 = st.number_input('Number of cluster result dataset 1', min_value=2,max_value=20, value=2)
        cluster_dataset2 = st.number_input('Number of cluster result dataset 2', min_value=2,max_value=20, value=3)
        cluster_dataset3 = st.number_input('Number of cluster result dataset 3', min_value=2,max_value=20, value=5)

    with colDataset:
        # dataset_array = [item["dataset"] for item in dataset_names]
        groupby = st.selectbox('Group by',['Dataset', 'Algorithm'])
        ranktype = st.radio("Rank type", ['Silhouette score', 'Davies–Bouldin score', 'Computation time'])

    with colInfo:
        based_on = {
            'group_by' : groupby,
            'rank_type' : ranktype,
            'cluster_dataset1' : cluster_dataset1,
            'cluster_dataset2' : cluster_dataset2,
            'cluster_dataset3' : cluster_dataset3,
        }
        st.caption('Information')
        st.json(based_on)

    st.caption(''); st.caption('')


    st.subheader("Results")
    if st.button('Run'):
        eval = Evaluation(based_on)

        if based_on['group_by'] == "Dataset":
            try:
                eval.datasetBased()
            except:
                st.warning("Either of the algorithms does not have the desired number of clusters😅")


        if based_on['group_by'] == "Algorithm":
            try:
                eval.algorithmBased()
            except:
                st.warning("Either of the algorithms does not have the desired number of clusters😅")

