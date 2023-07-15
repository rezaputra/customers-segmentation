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


    reducer = PCA(n_components=2)
    embedding = reducer.fit_transform(df)

    # reducer = umap.UMAP(n_components=2, metric='euclidean', min_dist=0.1)
    # embedding = reducer.fit_transform(df)

    data = pd.concat([pd.DataFrame(embedding), pd.DataFrame(labels)], axis=1) 

    u_labels = pd.unique(data['CLUSTER'])
    column = data.columns.values.tolist()

    plt.figure(figsize = (10,10))
    plt.scatter(x = data[column[0]], y = data[column[1]], c=data[column[2]], alpha = 0.8, label = u_labels)
    plt.grid()
    plt.title("2D CLuster")

    plt.savefig('img/cluster_plot2d_nopca.png')


def plot_dataset_based(jd, vb, fd):
    value_based = vb
    figure_details = fd
    json_data = jd

    algo_names = [entry['clustering'] for entry in json_data]
    values = [entry[value_based] for entry in json_data]
    colors = ['#fdcce5' if algorithm == 'HDBSCAN' else '#ffb55a' if algorithm == 'HDBSCAN + PCA' else '#54bebe' for algorithm in algo_names]
    font = {'family': 'Roboto',
        'color':  'black',
        'weight': 'light',
        'size': 14,
        }

    plt.figure(figsize = (10,12))
    plt.bar(range(len(json_data)), values, tick_label=algo_names, color=colors)
    plt.title(figure_details['title'], fontdict={'size' : 19}, pad=35)
    plt.ylabel(figure_details['y_label'], fontdict=font, style='italic')
    plt.xlabel(figure_details['x_label'], fontdict=font)
    plt.xticks(rotation=45) 

    plt.savefig(figure_details['file_path'])


def plot_algorithm_based(jd, vb, fd):
    json_data = jd
    figure_details = fd
    value_based = vb

    json_keys = list(json_data.keys())
    dataset_names = [f"Dataset {i+1}" for i in range(len(json_keys))]
    values = [entry[value_based] for entry in json_data.values()]
    colors = ['#FF9B9B' if dataset == dataset_names[0] else '#78C1F3' if dataset == dataset_names[1] else '#FFD966' for dataset in dataset_names]
    font = {'family': 'Roboto',
        'color':  'black',
        'weight': 'light',
        'size': 14,
        }
    
    plt.figure(figsize = (10,15))
    plt.bar(range(len(json_data)), values, tick_label=dataset_names, color=colors)
    plt.title(figure_details['title'], fontdict={'size' : 20}, pad=35)
    plt.ylabel(figure_details['y_label'], fontdict=font, style='italic')
    plt.xlabel(figure_details['x_label'], fontdict=font)
    plt.xticks(rotation=45) 

    plt.savefig(figure_details['file_path'])







    
    
