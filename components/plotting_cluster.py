import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

class PlottingKMeans:
    def __init__(self, d):
        self.data = d
        self.method =  st.session_state['dpMethod'].copy()
        self.dp = pd.DataFrame(st.session_state['dataPreparation'].copy())
        # self.column = self.data.columns.values.tolist()

    def execute_plotting(self):
        match self.method['dimension']:
            case 1:
                 self.__kmeans_1d()
            case 1:
                 self.__kmeans_2d()
            case 1:
                 self.__kmeans_3d()
    
    def __kmeans_1d(self):
        # self.dp['CLUSTER'] = self.data['result'].labels_
        st.caption('Plotting K-Means Result With One Dimension Data')
        st.write(self.dp)

        # onePlot = sns.swarmplot(data=self.data, x=self.data[self.column[1]], hue=self.data['result'].labels_)
        # oneFig = onePlot.get_figure()
        # oneFig.savefig('img/kmeans_plot1d.png')

        # st.image('img/kmeans_plot1d.png')
        

    def __kmeans_2d(self):
        st.write('Plotting K-Means Result With Two Dimension Data')

    def __kmeans_3d(self):
        st.write('Plotting K-Means Result With Three Dimension Data')
