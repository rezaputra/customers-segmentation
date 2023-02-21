import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt

perc = [0.20, 0.40, 0.60, 0.80]
inc = ['object', 'float', 'int']


def viewDetailDpWithFE(e, m, d):
    data = pd.DataFrame(d)
    method = m
    column = data.columns.values.tolist()

    tabShowData, tabPlot = st.tabs(['🗃 Result', 'ℹ Plotting'])

    with tabShowData:
        colShowData, colDetail ,colTimeExecute = st.columns([1,1,1])
        with colShowData:
            st.caption("Dataset")         
            st.write(data)
        with colDetail:
            st.caption("Detail")          
            st.write(data.describe(percentiles = perc, include = inc))
        with colTimeExecute:
            st.caption("Processing time")        
            st.write("Clean : ", round(e['Clean'], 4))                
            st.write(method['encode'] + " : ", round(e['encode'], 4))              
            st.write(method['scale'] + " : ", round(e['scale'], 4))              
            st.write(method['extraction'] + " : ", round(e['extraction'], 4))    
            st.write( "Total time: ", round(e['total'], 4))  

    with tabPlot:
        match method['dimension']:
            case 1:
                st.caption("Plotting 1D")
                st.bar_chart(data)

            case 2:
                chart = alt.Chart(data=data).mark_circle().encode(
                    x = column[0],
                    y = column[1],

                )
                st.caption("Plotting 2D")
                st.altair_chart(chart, theme="streamlit", use_container_width=True)

            case 3:
                fig = plt.figure(figsize = (10,10))
                ax = plt.axes(projection='3d')
                ax.grid()

                ax.scatter(data[column[0]], data[column[1]], data[column[2]])
                ax.set_title('3D Scatter Plot')

                ax.set_xlabel(column[0], labelpad=20)
                ax.set_ylabel(column[1], labelpad=20)
                ax.set_zlabel(column[2], labelpad=20)

                plt.savefig('img/dp_plot3d.png')
                st.caption("Plotting 3D")
                st.image('img/dp_plot3d.png', width=800, caption='Features Extraction Result')




def viewDetailDpWithoutFE(e, m, d):
    data = pd.DataFrame(d)
    method = m

    tabShowData, tabDetail = st.tabs(['🗃 Result', 'ℹ Time'])
    with tabShowData:
        st.caption("Dataset")         
        st.write(data)
    with tabDetail:
        colDetail ,colTimeExecute = st.columns([2,1])
        with colDetail:
            st.caption("Detail")          
            st.write(data.describe(percentiles = perc, include = inc))
        with colTimeExecute:
            st.caption("Processing time")        
            st.write("Clean : ", round(e['Clean'], 4))                
            st.write(method['encode'] + " : ", round(e['encode'], 4))              
            st.write(method['scale'] + " : ", round(e['scale'], 4))              
            st.write( "Total time: ", round(e['total'], 4))  


