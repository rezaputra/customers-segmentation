import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import umap


def dp_two_dimension(d, c):
    data = d.copy()
    column = c.copy()

    plt.figure(figsize = (10,10))

    plt.scatter(data[column[0]], data[column[1]])
    plt.grid()
    plt.xlabel(column[0], labelpad=20)
    plt.ylabel(column[1], labelpad=20)
    plt.title("2D Features Extraction")

    plt.savefig('img/dp_plot2d.png')
    st.caption("Scatter 2D Plotting")
    st.image('img/dp_plot2d.png', width=800)



def dp_three_dimension(d, c):
    data = d.copy()
    column = c.copy()

    plt.figure(figsize = (10,10))
    ax = plt.axes(projection='3d')
    ax.grid()

    ax.scatter(data[column[0]], data[column[1]], data[column[2]])
    ax.set_title('3D Features Extraction')

    ax.set_xlabel(column[0], labelpad=20)
    ax.set_ylabel(column[1], labelpad=20)
    ax.set_zlabel(column[2], labelpad=20)

    plt.savefig('img/dp_plot3d.png')
    st.caption("Data Preparation 3D Plotting")
    st.image('img/dp_plot3d.png', width=800)


def clustering_result_two_dimension(d):
    data = d.copy()
    column = data.columns.values.tolist()
    column.pop(0)
    u_labels = pd.unique(data['CLUSTER'])

    plt.figure(figsize = (10,10))
    plt.scatter(x = data[column[0]], y = data[column[1]], c=data[column[2]], alpha = 0.8, label = u_labels)
    plt.grid()
    plt.title("2D CLuster")

    plt.savefig('img/cluster_plot2d.png')


def clustering_result_two_dimension_nopca(d):
    df = pd.DataFrame(d)
    labels = df['CLUSTER']
    df.pop('CLUSTER')
    df.pop('ID')


    # pca = PCA(n_components=2)
    # pca_x = pca.fit_transform(df)

    reducer = umap.UMAP(n_components=2, metric='euclidean', min_dist=0.1)
    embedding = reducer.fit_transform(df)

    data = pd.concat([pd.DataFrame(embedding), pd.DataFrame(labels)], axis=1) 

    u_labels = pd.unique(data['CLUSTER'])
    column = data.columns.values.tolist()

    plt.figure(figsize = (10,10))
    plt.scatter(x = data[column[0]], y = data[column[1]], c=data[column[2]], alpha = 0.8, label = u_labels)
    plt.grid()
    plt.title("2D CLuster")

    plt.savefig('img/cluster_plot2d_nopca.png')


    
    
