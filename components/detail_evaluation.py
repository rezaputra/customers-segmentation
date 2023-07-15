import streamlit as st
from components.plotting import plot_dataset_based, plot_algorithm_based


def dataset_based_view(d1, d2, d3, vb):
    dataset1 = d1
    dataset2 = d2
    dataset3 = d3

    match vb:
        case "Silhouette score":
            value_based = "indexScore"
            x_label = "Higher is Better"
        case "Davies–Bouldin score":
            value_based = "dbScore"
            x_label = "Lower is Better"
        case "Computation time":
            value_based = "time"
            x_label = "Lower is Better"

    tabDataset1, tabDataset2, tabDataset3 = st.tabs(["Dataset 1", "Dataset 2", "Dataset 3"])

    with tabDataset1:
        figure_details = { 
            "file_path" : 'img/'+value_based+'_dataset1.png',
            "title" : "Dataset 1 Results Based on " + vb,
            "y_label" : vb,
            "x_label" : x_label}
        
        plot_dataset_based(dataset1, value_based, figure_details)

        colFigDaataset1, colRankDataset1 = st.columns([1,1], gap="small")
        with colFigDaataset1:
            st.image(figure_details['file_path'], width=700)

        with colRankDataset1:
            st.caption("")
            st.caption("")
            st.caption("")
            st.markdown("##### Ranking")
            for i, item in enumerate(dataset1):
                clustering_algo = item["clustering"]
                clustering_value = item[value_based]
                st.write(f"{i+1}. {clustering_algo} : {round(clustering_value,4)}")

    with tabDataset2:
        figure_details = { 
            "file_path" : 'img/'+value_based+'_dataset2.png',
            "title" : "Dataset 2 Results Based on " + vb,
            "y_label" : vb,
            "x_label" : x_label}
        
        plot_dataset_based(dataset2, value_based, figure_details)

        colFigDaataset2, colRankDataset2 = st.columns([1,1], gap="small")
        with colFigDaataset2:
            st.image(figure_details['file_path'], width=700)

        with colRankDataset2:
            st.caption("")
            st.caption("")
            st.caption("")
            st.markdown("##### Ranking")
            for i, item in enumerate(dataset2):
                clustering_algo = item["clustering"]
                clustering_value = item[value_based]
                st.write(f"{i+1}. {clustering_algo} : {round(clustering_value,4)}")

    with tabDataset3:
        figure_details = { 
            "file_path" : 'img/'+value_based+'_dataset3.png',
            "title" : "Dataset 3 Results Based on " + vb,
            "y_label" : vb,
            "x_label" : x_label}
        
        plot_dataset_based(dataset3, value_based, figure_details)

        colFigDaataset3, colRankDataset3 = st.columns([1,1], gap="small")
        with colFigDaataset3:
            st.image(figure_details['file_path'], width=700)

        with colRankDataset3:
            st.caption("")
            st.caption("")
            st.caption("")
            st.markdown("##### Ranking")
            for i, item in enumerate(dataset3):
                clustering_algo = item["clustering"]
                clustering_value = item[value_based]
                st.write(f"{i+1}. {clustering_algo} : {round(clustering_value,4)}")



def algorithm_based_view(jd, vb):
    json_data = jd
    match vb:
        case "Silhouette score":
            value_based = "indexScore"
            x_label = "Higher is Better"
        case "Davies–Bouldin score":
            value_based = "dbScore"
            x_label = "Lower is Better"
        case "Computation time":
            value_based = "time"
            x_label = "Lower is Better"

    tabHdbscan, tabHdbscanPca, tabKmeans, tabAgglomerative, tabDbscan, tabOptics, tabMeanshift = st.tabs(['HDBSCAN', 'HDBSCAN + PCA', 'K-Means', 'Agglomerative', 'DBSCAN', 'OPTICs', 'MeanShift'])

    with tabHdbscan:
        figure_details = { 
            "file_path" : 'img/'+value_based+'_hdbscan.png',
            "title" : "HDBSCAN Results Based on " + vb,
            "y_label" : vb,
            "x_label" : x_label}
        
        plot_algorithm_based(json_data['hdbscan'],value_based ,figure_details)

        colFig, colInfo = st.columns([1,1], gap="small")
        with colFig:
            st.image(figure_details['file_path'], width=600)

        with colInfo:
            st.caption("")
            st.caption("")
            st.caption("")
            st.caption("")
            st.markdown("##### HDBSCAN Results")
            st.write("---")
            for i, (dataset_name, dataset_details) in enumerate(json_data['hdbscan'].items()):
                st.markdown(f"**Dataset {i+1} Information**")
                st.write(f"Dataset name: _{dataset_name}_")
                st.write(f"{vb}: _{round(dataset_details[value_based], 4)}_")
                st.write("**Parameter**")
                for param, value in zip(dataset_details['details']['clustering_parameter'], dataset_details['details']['parameter_value']):
                    st.write(f"{param}: _{value}_")
                st.write("---")

    with tabHdbscanPca:
        figure_details = { 
            "file_path" : 'img/'+value_based+'_hdbscan_pca.png',
            "title" : "HDBSCAN With PCA Results Based on " + vb,
            "y_label" : vb,
            "x_label" : x_label}
        
        plot_algorithm_based(json_data['hdbscan_pca'],value_based ,figure_details)

        colFig, colInfo = st.columns([1,1], gap="small")
        with colFig:
            st.image(figure_details['file_path'], width=600)

        with colInfo:
            st.caption("")
            st.caption("")
            st.caption("")
            st.caption("")
            st.markdown("##### HDBSCAN With PCA Results")
            st.write("---")
            for i, (dataset_name, dataset_details) in enumerate(json_data['hdbscan_pca'].items()):
                st.markdown(f"**Dataset {i+1} Information**")
                st.write(f"Dataset name: _{dataset_name}_")
                st.write(f"{vb}: _{round(dataset_details[value_based], 4)}_")
                st.write("**Parameter**")
                for param, value in zip(dataset_details['details']['clustering_parameter'], dataset_details['details']['parameter_value']):
                    st.write(f"{param}: _{value}_")
                st.write("---")

    with tabKmeans:
        figure_details = { 
            "file_path" : 'img/'+value_based+'_kmeans.png',
            "title" : "HDBSCAN With PCA Results Based on " + vb,
            "y_label" : vb,
            "x_label" : x_label}
        
        plot_algorithm_based(json_data['kmeans'],value_based ,figure_details)

        colFig, colInfo = st.columns([1,1], gap="small")
        with colFig:
            st.image(figure_details['file_path'], width=600)

        with colInfo:
            st.caption("")
            st.caption("")
            st.caption("")
            st.caption("")
            st.markdown("##### K-Means Results")
            st.write("---")
            for i, (dataset_name, dataset_details) in enumerate(json_data['kmeans'].items()):
                st.markdown(f"**Dataset {i+1} Information**")
                st.write(f"Dataset name: _{dataset_name}_")
                st.write(f"{vb}: _{round(dataset_details[value_based], 4)}_")
                st.write("**Parameter**")
                for param, value in zip(dataset_details['details']['clustering_parameter'], dataset_details['details']['parameter_value']):
                    st.write(f"{param}: _{value}_")
                st.write("---")

    with tabAgglomerative:
        figure_details = { 
            "file_path" : 'img/'+value_based+'_agglomerative.png',
            "title" : "HDBSCAN With PCA Results Based on " + vb,
            "y_label" : vb,
            "x_label" : x_label}
        
        plot_algorithm_based(json_data['agglomerative'],value_based ,figure_details)

        colFig, colInfo = st.columns([1,1], gap="small")
        with colFig:
            st.image(figure_details['file_path'], width=600)

        with colInfo:
            st.caption("")
            st.caption("")
            st.caption("")
            st.caption("")
            st.markdown("##### Agglomerative Results")
            st.write("---")
            for i, (dataset_name, dataset_details) in enumerate(json_data['agglomerative'].items()):
                st.markdown(f"**Dataset {i+1} Information**")
                st.write(f"Dataset name: _{dataset_name}_")
                st.write(f"{vb}: _{round(dataset_details[value_based], 4)}_")
                st.write("**Parameter**")
                for param, value in zip(dataset_details['details']['clustering_parameter'], dataset_details['details']['parameter_value']):
                    st.write(f"{param}: _{value}_")
                st.write("---")

    with tabDbscan:
        figure_details = { 
            "file_path" : 'img/'+value_based+'_dbscan.png',
            "title" : "HDBSCAN With PCA Results Based on " + vb,
            "y_label" : vb,
            "x_label" : x_label}
        
        plot_algorithm_based(json_data['dbscan'],value_based ,figure_details)

        colFig, colInfo = st.columns([1,1], gap="small")
        with colFig:
            st.image(figure_details['file_path'], width=600)

        with colInfo:
            st.caption("")
            st.caption("")
            st.caption("")
            st.caption("")
            st.markdown("##### DBSCAN Results")
            st.write("---")
            for i, (dataset_name, dataset_details) in enumerate(json_data['dbscan'].items()):
                st.markdown(f"**Dataset {i+1} Information**")
                st.write(f"Dataset name: _{dataset_name}_")
                st.write(f"{vb}: _{round(dataset_details[value_based], 4)}_")
                st.write("**Parameter**")
                for param, value in zip(dataset_details['details']['clustering_parameter'], dataset_details['details']['parameter_value']):
                    st.write(f"{param}: _{value}_")
                st.write("---")

    with tabOptics:
        figure_details = { 
            "file_path" : 'img/'+value_based+'_optics.png',
            "title" : "Hoptics With PCA Results Based on " + vb,
            "y_label" : vb,
            "x_label" : x_label}
        
        plot_algorithm_based(json_data['optics'],value_based ,figure_details)

        colFig, colInfo = st.columns([1,1], gap="small")
        with colFig:
            st.image(figure_details['file_path'], width=600)

        with colInfo:
            st.caption("")
            st.caption("")
            st.caption("")
            st.caption("")
            st.markdown("##### Optics Results")
            st.write("---")
            for i, (dataset_name, dataset_details) in enumerate(json_data['optics'].items()):
                st.markdown(f"**Dataset {i+1} Information**")
                st.write(f"Dataset name: _{dataset_name}_")
                st.write(f"{vb}: _{round(dataset_details[value_based], 4)}_")
                st.write("**Parameter**")
                for param, value in zip(dataset_details['details']['clustering_parameter'], dataset_details['details']['parameter_value']):
                    st.write(f"{param}: _{value}_")
                st.write("---")

    with tabMeanshift:
        figure_details = { 
            "file_path" : 'img/'+value_based+'_meanshift.png',
            "title" : "Hmeanshift With PCA Results Based on " + vb,
            "y_label" : vb,
            "x_label" : x_label}
        
        plot_algorithm_based(json_data['meanshift'],value_based ,figure_details)

        colFig, colInfo = st.columns([1,1], gap="small")
        with colFig:
            st.image(figure_details['file_path'], width=600)

        with colInfo:
            st.caption("")
            st.caption("")
            st.caption("")
            st.caption("")
            st.markdown("##### meanshift Results")
            st.write("---")
            for i, (dataset_name, dataset_details) in enumerate(json_data['meanshift'].items()):
                st.markdown(f"**Dataset {i+1} Information**")
                st.write(f"Dataset name: _{dataset_name}_")
                st.write(f"{vb}: _{round(dataset_details[value_based], 4)}_")
                st.write("**Parameter**")
                for param, value in zip(dataset_details['details']['clustering_parameter'], dataset_details['details']['parameter_value']):
                    st.write(f"{param}: _{value}_")
                st.write("---")