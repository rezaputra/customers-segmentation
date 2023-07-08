# import streamlit as st
# import json
# import pandas as pd



# def bestMainScoreDefault(json_data, dataset, pca):
#     desired_data = next(item for item in json_data if item["dataset"] == dataset and item["extraction"] == pca)

#     return desired_data


# def bestComparedScoreDefault(json_data, dataset):
#     desired_data = next((item for item in json_data if item["dataset"] == dataset))

#     return desired_data


# def bestComparedScore(json_data, dataset):
#     # Filter and select rows with dwimedialestari.csv dataset and extraction as PCA
#     filtered_data = [item for item in json_data if item["dataset"] == dataset and item["extraction"] == False]

#     # Find the item with the highest score among the filtered data
#     max_score_item = max(filtered_data, key=lambda x: x["score"])

#     return max_score_item


# def bestMainScore(json_data, dataset, pca):
#     # Filter and select rows with dwimedialestari.csv dataset and extraction as PCA
#     filtered_data = [item for item in json_data if item["dataset"] == dataset and item["extraction"] == pca]

#     # Find the item with the highest score among the filtered data
#     max_score_item = max(filtered_data, key=lambda x: x["score"])

#     return max_score_item

# def bestComparedScore(json_data, dataset):
#     # Filter and select rows with dwimedialestari.csv dataset and extraction as PCA
#     filtered_data = [item for item in json_data if item["dataset"] == dataset and item["extraction"] == False]

#     # Find the item with the highest score among the filtered data
#     max_score_item = max(filtered_data, key=lambda x: x["score"])

#     return max_score_item



# def bestMainTime(json_data, dataset, pca):
#     # Filter and select rows with dwimedialestari.csv dataset and extraction as PCA
#     filtered_data = [item for item in json_data if item["dataset"] == dataset and item["extraction"] == pca and item["time"] >=0]

#     # Find the item with the highest score among the filtered data
#     min_time_item = min(filtered_data, key=lambda x: x["time"])

#     return min_time_item


# def bestComparedTime(json_data, dataset):
#     # Filter and select rows with dwimedialestari.csv dataset and extraction as PCA
#     filtered_data = [item for item in json_data if item["dataset"] == dataset and item["extraction"] == False and item["time"] >=0]

#     # Find the item with the highest score among the filtered data
#     if len(filtered_data) >= 1:
#         min_time_item = min(filtered_data, key=lambda x: x["time"])

#         return min_time_item
    
#     else:
#         return filtered_data



# # Membaca file JSON yang sudah ada
# with open('evaluation/dataset.json', 'r') as file:
#     dataset_names = json.load(file)

# with open('evaluation/agglomerative.json', 'r') as file:
#     agglomerative = json.load(file)

# # with open('evaluation/ap.json', 'r') as file:
# #     ap = json.load(file)

# with open('evaluation/dbscan.json', 'r') as file:
#     dbscan = json.load(file)

# with open('evaluation/hdbscan.json', 'r') as file:
#     hdbscan = json.load(file)

# with open('evaluation/kmeans.json', 'r') as file:
#     kmeans = json.load(file)

# with open('evaluation/optics.json', 'r') as file:
#     kmeans = json.load(file)

# with open('evaluation/meanshift.json', 'r') as file:
#     kmeans = json.load(file)




# st.subheader("Evaluate HDBSCAN Clustering")
# st.subheader("")

# colDataset, colPCA = st.columns([1,2], gap="large")
# with colDataset:
#     # Extract the "dataset" values into an array
#     dataset_array = [item["dataset"] for item in dataset_names]

#     dataset = st.selectbox('Choose dataset name',dataset_array, index=0)

# with colPCA:
#     mode = st.radio(
#         "Select mode HDBSCAN",
#         ["With PCA", "Without PCA"],
#         horizontal=True, 
#     )
#     if mode == "With PCA" :
#         mode = "PCA"
#     else:
#         mode = False


# st.caption(''); st.caption('')


# default_hdbscan = bestMainScoreDefault(hdbscan, dataset, mode)
# default_kmeans = bestComparedScoreDefault(kmeans, dataset)
# default_ap = bestComparedScoreDefault(ap, dataset)
# default_agglomerative = bestComparedScoreDefault(agglomerative, dataset)
# default_dbscan = bestComparedScoreDefault(dbscan, dataset)


# score_hdbscan = bestMainScore(hdbscan, dataset, mode)
# score_kmeans = bestComparedScore(kmeans, dataset)
# score_ap = bestComparedScore(ap, dataset)
# score_agglomerative = bestComparedScore(agglomerative, dataset)
# score_dbscan = bestComparedScore(dbscan, dataset)


# time_hdbscan = bestMainTime(hdbscan, dataset, mode)
# time_kmeans = bestComparedTime(kmeans, dataset)
# time_ap = bestComparedTime(ap, dataset)
# time_agglomerative = bestComparedTime(agglomerative, dataset)
# time_dbscan = bestComparedTime(dbscan, dataset)

# plot_default_data = [default_hdbscan,default_kmeans, default_ap, default_agglomerative, default_dbscan]
# plot_tuning_data = [score_hdbscan,score_kmeans,score_ap,score_agglomerative,score_dbscan]

# sorted_default_score = sorted(plot_default_data, key=lambda x: x["score"], reverse=True)
# sorted_default_time = sorted(plot_default_data, key=lambda x: x["time"], reverse=False)

# sorted_tuning_score = sorted(plot_tuning_data, key=lambda x: x["score"], reverse=True)
# sorted_tuning_time = sorted(plot_tuning_data, key=lambda x: x["time"], reverse=False)

# # Extract scores and clustering algorithms from the data Default
# chart_default_score = {"Score": {item["clustering"]: item["score"] for item in plot_default_data}}
# chart_default_time = {"Time": {item["clustering"]: item["time"] for item in plot_default_data}}

# # Extract scores and clustering algorithms from the data Tuning
# chart_tuning_score = {"Score": {item["clustering"]: item["score"] for item in plot_tuning_data}}
# chart_tuning_time = {"Time": {item["clustering"]: item["time"] for item in plot_tuning_data}}



# st.caption('')
# st.caption('')


# # st.json(plot_tuning_data)

# st.markdown("#### **_Before Tuning Parameter_**")
# with st.expander('Default Result', expanded=False):
#     st.caption('')
#     st.markdown("###### **_By Score_**")
#     tabScoreDefault, tabParameterDefault = st.tabs(['Result', 'Parameter'])
#     with tabScoreDefault:
#         # st.caption('result')
#         colPlotScore, colRankScore = st.columns([3,1], gap="large")
#         with colPlotScore:
#             st.caption('Score : Higher is better')
#             st.bar_chart(chart_default_score)

#         with colRankScore:
#             st.caption('Ranked')
#             for i, item in enumerate(sorted_default_score, start=1):
#                 st.write(f"{i}. {item['clustering']} : {round(item['score'], 4)}")


#     with tabParameterDefault:
#         col1, col2 = st.columns([1,1])
#         with col1:
#             st.caption('')
#             st.caption(plot_default_data[0]['clustering'])
#             st.write(pd.DataFrame(plot_default_data[0]['details']))

#             st.caption('')
#             st.caption(plot_default_data[1]['clustering'])
#             st.write(pd.DataFrame(plot_default_data[1]['details']))

#             st.caption('')
#             st.caption(plot_default_data[2]['clustering'])
#             st.write(pd.DataFrame(plot_default_data[2]['details']))

#         with col2:            
#             st.caption('')
#             st.caption(plot_default_data[3]['clustering'])
#             st.write(pd.DataFrame(plot_default_data[3]['details']))
            
#             st.caption('')
#             st.caption(plot_default_data[4]['clustering'])
#             st.write(pd.DataFrame(plot_default_data[4]['details']))


#     st.caption('')
#     st.caption('')
#     st.markdown("###### **_By Time_**")
#     tabScoreDefault, tabParameterDefault = st.tabs(['Result', 'Parameter'])
#     with tabScoreDefault:
#         # st.caption('result')
#         colPlotTime, colRankTime = st.columns([3,1], gap="large")
#         with colPlotTime:
#             st.caption('Time : Lower is better')
#             st.bar_chart(chart_default_time)

#         with colRankTime:
#             st.caption('Ranked')
#             for i, item in enumerate(sorted_default_time, start=1):
#                 st.write(f"{i}. {item['clustering']} : {round(item['time'], 4)}s")


#     with tabParameterDefault:
#         col1, col2 = st.columns([1,1])
#         with col1:
#             st.caption('')
#             st.caption(plot_default_data[0]['clustering'])
#             st.write(pd.DataFrame(plot_default_data[0]['details']))

#             st.caption('')
#             st.caption(plot_default_data[1]['clustering'])
#             st.write(pd.DataFrame(plot_default_data[1]['details']))

#             st.caption('')
#             st.caption(plot_default_data[2]['clustering'])
#             st.write(pd.DataFrame(plot_default_data[2]['details']))

#         with col2:            
#             st.caption('')
#             st.caption(plot_default_data[3]['clustering'])
#             st.write(pd.DataFrame(plot_default_data[3]['details']))
            
#             st.caption('')
#             st.caption(plot_default_data[4]['clustering'])
#             st.write(pd.DataFrame(plot_default_data[4]['details']))


# st.caption('')
# st.caption('')

# st.markdown("#### **_After Tuning Parameter_**")
# with st.expander('Optimize Result', expanded=False):
#     st.caption('')
#     st.markdown("###### **_By Score_**")
#     tabScoreDefault, tabParameterDefault = st.tabs(['Result', 'Parameter'])
#     with tabScoreDefault:
#         # st.caption('result')
#         colPlotScore, colRankScore = st.columns([3,1], gap="large")
#         with colPlotScore:
#             st.caption('Score : Higher is better')
#             st.bar_chart(chart_tuning_score)

#         with colRankScore:
#             st.caption('Ranked')
#             for i, item in enumerate(sorted_tuning_score, start=1):
#                 st.write(f"{i}. {item['clustering']} : {round(item['score'], 4)}")


#     with tabParameterDefault:
#         col1, col2 = st.columns([1,1])
#         with col1:
#             st.caption('')
#             st.caption(score_hdbscan['clustering'])
#             st.write(pd.DataFrame(score_hdbscan['details']))

#             st.caption('')
#             st.caption(score_agglomerative['clustering'])
#             st.write(pd.DataFrame(score_agglomerative['details']))

#             st.caption('')
#             st.caption(score_kmeans['clustering'])
#             st.write(pd.DataFrame(score_kmeans['details']))

#         with col2:            
#             st.caption('')
#             st.caption(score_dbscan['clustering'])
#             st.write(pd.DataFrame(score_dbscan['details']))
            
#             st.caption('')
#             st.caption(score_ap['clustering'])
#             st.write(pd.DataFrame(score_ap['details']))


#     st.caption('')
#     st.caption('')
#     st.markdown("###### **_By Time_**")
#     tabScoreDefault, tabParameterDefault = st.tabs(['Result', 'Parameter'])
#     with tabScoreDefault:
#         # st.caption('result')
#         colPlotTime, colRankTime = st.columns([3,1], gap="large")
#         with colPlotTime:
#             st.caption('Time : Lower is better')
#             st.bar_chart(chart_tuning_time)

#         with colRankTime:
#             st.caption('Ranked')
#             for i, item in enumerate(sorted_tuning_time, start=1):
#                 st.write(f"{i}. {item['clustering']} : {round(item['time'], 4)}s")


#     with tabParameterDefault:
#         col1, col2 = st.columns([1,1])
#         with col1:
#             st.caption('')
#             st.caption(time_hdbscan['clustering'])
#             st.write(pd.DataFrame(time_hdbscan['details']))

#             st.caption('')
#             st.caption(time_agglomerative['clustering'])
#             st.write(pd.DataFrame(time_agglomerative['details']))

#             st.caption('')
#             st.caption(time_kmeans['clustering'])
#             st.write(pd.DataFrame(time_kmeans['details']))

#         with col2:            
#             st.caption('')
#             st.caption(score_dbscan['clustering'])
#             st.write(pd.DataFrame(time_dbscan['details']))
            
#             st.caption('')
#             st.caption(score_ap['clustering'])
#             st.write(pd.DataFrame(time_ap['details']))
