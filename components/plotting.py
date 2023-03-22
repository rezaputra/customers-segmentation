import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


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
    st.image('img/dp_plot2d.png', width=800, caption='2D Plotting')



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
    st.image('img/dp_plot3d.png', width=800, caption='3D Plotting')


def clustering_result_two_dimension(d, c):
    data = d.copy()
    column = c.copy()
    
