import streamlit as st
import pandas as pd



def kmeans_result_detail(d):
    data = d.copy()
    col1, col2, col3 = st.columns([1.2,1,1.2], gap='large')
    x = st.session_state['dataPreparation'].copy()
    dfResult = pd.DataFrame(x)
    id = pd.DataFrame(st.session_state['datasetId'].copy())

    with col1:
        st.caption('Clustering Result') 
        dfResult['CLUSTER'] = data['result'].labels_
        if 'ID' not in dfResult.columns:
            dfResult.insert(loc=0, column='ID', value=id.values)
        st.write(dfResult) 

    with col2:
        st.caption('Cluster Center')
        st.write(data['result'].cluster_centers_)
                
    with col3:
        st.caption('Computation Time')
        st.write('Data preparation :',round(st.session_state['dpTimeProcessing']['total'], 4))     
        st.write(data['algorithm'],' clustering :',round(data['time'], 4))     
        st.write('Total time :',round(st.session_state['dpTimeProcessing']['total'] + data['time'], 4))    

        st.caption('')
        st.caption('')
        st.caption('More Information')
        st.write('Number of iterations run :', data['result'].n_iter_)
        st.write('Sum of squared distances of samples :', round(data['result'].inertia_, 0))
        st.write('Silhouette score :', round(data['score'], 4)) 



def agglomerative_result_detail(d):
    data = d.copy()
    col1, col2, col3 = st.columns([1.2,1,1.2], gap='large')
    x = st.session_state['dataPreparation'].copy()
    dfResult = pd.DataFrame(x)
    id = pd.DataFrame(st.session_state['datasetId'].copy())


    with col1:
        st.caption('Clustering Result') 
        dfResult['CLUSTER'] = data['result'].labels_
        if 'ID' not in dfResult.columns:
            dfResult.insert(loc=0, column='ID', value=id.values)
        st.write(dfResult) 

    with col2:
         st.caption('Children of each non-leaf node')
         st.write(data['result'].children_)

    with col3:
        st.caption('Computation Time')
        st.write('Data preparation :',round(st.session_state['dpTimeProcessing']['total'], 4))     
        st.write(data['algorithm'],' clustering :',round(data['time'], 4))     
        st.write('Total time :',round(st.session_state['dpTimeProcessing']['total'] + data['time'], 4))
        
        st.caption('')
        st.caption('')
        st.caption('More Information')
        st.write('Number of leaves in the hierarchical tree :', data['result'].n_leaves_)
        st.write('Silhouette score :', round(data['score'], 4))



def dbscan_detail(d):
    data = d.copy()
    col1, col2, col3 = st.columns([1.2,1,1.2], gap='large')
    x = st.session_state['dataPreparation'].copy()
    dfResult = pd.DataFrame(x)
    id = pd.DataFrame(st.session_state['datasetId'].copy())


    with col1:
        st.caption('Clustering Result') 
        dfResult['CLUSTER'] = data['result'].labels_
        if 'ID' not in dfResult.columns:
            dfResult.insert(loc=0, column='ID', value=id.values)
        st.write(dfResult) 

    with col2:
         st.caption('Components', )
         st.write(data['result'].components_)

    with col3:
        st.caption('Computation Time')
        st.write('Data preparation :',round(st.session_state['dpTimeProcessing']['total'], 4))     
        st.write(data['algorithm'],' clustering :',round(data['time'], 4))     
        st.write('Total time :',round(st.session_state['dpTimeProcessing']['total'] + data['time'], 4))
        
        st.caption('')
        st.caption('')
        st.caption('More Information')
        st.write('Silhouette score :', round(data['score'], 4))


def hdbscan_detail(d):
    data = d.copy()
    col1, col2, col3 = st.columns([1.2,1,1.2], gap='large')
    x = st.session_state['dataPreparation'].copy()
    dfResult = pd.DataFrame(x)
    id = pd.DataFrame(st.session_state['datasetId'].copy())


    with col1:
        st.caption('Clustering Result') 
        dfResult['CLUSTER'] = data['result'].labels_
        if 'ID' not in dfResult.columns:
            dfResult.insert(loc=0, column='ID', value=id.values)
        st.write(dfResult) 

    with col2:
         st.caption('Strength of each sample', )
         st.write(data['result'].probabilities_)

    with col3:
        st.caption('Computation Time')
        st.write('Data preparation :',round(st.session_state['dpTimeProcessing']['total'], 4))     
        st.write(data['algorithm'],' clustering :',round(data['time'], 4))     
        st.write('Total time :',round(st.session_state['dpTimeProcessing']['total'] + data['time'], 4))
        
        st.caption('')
        st.caption('')
        st.caption('More Information')
        st.write('Silhouette score :', round(data['score'], 4))



def affinity_propagation_detail(d):
    data = d.copy()
    col1, col2, col3 = st.columns([1.2,1,1.2], gap='large')
    x = st.session_state['dataPreparation'].copy()
    dfResult = pd.DataFrame(x)
    id = pd.DataFrame(st.session_state['datasetId'].copy())

    with col1:
        st.caption('Clustering Result') 
        dfResult['CLUSTER'] = data['result'].labels_
        if 'ID' not in dfResult.columns:
            dfResult.insert(loc=0, column='ID', value=id.values)
        st.write(dfResult) 

    with col2:
         st.caption('Cluster centers', )
         st.write(data['result'].cluster_centers_)

    with col3:
        st.caption('Computation Time')
        st.write('Data preparation :',round(st.session_state['dpTimeProcessing']['total'], 4))     
        st.write(data['algorithm'],' clustering :',round(data['time'], 4))     
        st.write('Total time :',round(st.session_state['dpTimeProcessing']['total'] + data['time'], 4))
        
        st.caption('')
        st.caption('')
        st.caption('More Information')
        st.write('Number of iterations run :', round(data['result'].n_iter_, 4))
        st.write('Silhouette score :', round(data['score'], 4))

