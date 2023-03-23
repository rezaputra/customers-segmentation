import streamlit as st
import pandas as pd

def download_with_label(d):
    data = pd.DataFrame(d.copy())
    df = data.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="Download",
        data=df,
        file_name='clustering_result.csv',
        mime='text/csv',
        )


def kmeans_result_detail(d):
    data = d.copy()
    col1, col2, col3 = st.columns([1.2,1,1.2], gap='large')

    with col1:
        st.caption('Clustering Result') 
        st.write(data['labeled']) 


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

        st.caption('')
        st.caption('')
        st.caption('Download Results')
        download_with_label(data['labeled'])



def agglomerative_result_detail(d):
    data = d.copy()
    col1, col2, col3 = st.columns([1.2,1,1.2], gap='large')

    with col1:
        st.caption('Clustering Result') 
        st.write(data['labeled']) 

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

        st.caption('')
        st.caption('')
        st.caption('Download Results')
        download_with_label(data['labeled'])



def dbscan_detail(d):
    data = d.copy()
    col1, col2, col3 = st.columns([1.2,1,1.2], gap='large')

    with col1:
        st.caption('Clustering Result') 
        st.write(data['labeled']) 

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

        st.caption('')
        st.caption('')
        st.caption('Download Results')
        download_with_label(data['labeled'])


def hdbscan_detail(d):
    data = d.copy()
    col1, col2, col3 = st.columns([1.2,1,1.2], gap='large')

    with col1:
        st.caption('Clustering Result') 
        st.write(data['labeled']) 

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

        st.caption('')
        st.caption('')
        st.caption('Download Results')
        download_with_label(data['labeled'])



def affinity_propagation_detail(d):
    data = d.copy()
    col1, col2, col3 = st.columns([1.2,1,1.2], gap='large')

    with col1:
        st.caption('Clustering Result') 
        st.write(data['labeled']) 

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

        st.caption('')
        st.caption('')
        st.caption('Download Results')
        download_with_label(data['labeled'])

