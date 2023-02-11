import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt

perc = [0.20, 0.40, 0.60, 0.80]
inc = ['object', 'float', 'int']


def viewDetailHome(d):
    data = pd.DataFrame(d)
    s = (data.dtypes == "object")
    t = (data.dtypes != "object")

    object_cols = list(s[s].index)
    non_object_cols = list(t[t].index)
    

    tabShowData, tabDetail = st.tabs(['🗃 Dataset', 'ℹ Details'])
    with tabShowData:
        st.write(data)        

    with tabDetail:
        colCleanDetails1, colCleanDetails2 = st.columns([3,1])
        with colCleanDetails1:
            st.write(data.describe(percentiles = perc, include = inc))
            # st.write(x.info())

        with colCleanDetails2:
            st.markdown("##### Recaps")
            nullValue = data.isna().values.sum()
            st.write("Total record:", len(data))
            st.write("Total elements:", data.size)
            st.write("Total attributes:", data.shape[1])
            st.write("Categorical attributes:", len(object_cols))
            st.write("Numeric attributes:", len(non_object_cols))
            st.write("Total duplicate data:", data.duplicated(keep=False).sum())
            st.write("Total Null or NA values:", nullValue)




def viewDetailDpWithFE(e, m, d):
    data = pd.DataFrame(d)
    method = m
    column = data.columns.values.tolist()
    total = sum(e.values())

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
            st.write( "Total time: ", round(total, 4))  

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
                st.image('img/dp_plot3d.png', width=800, caption='Features extraction result')




def viewDetailDpWithoutFE(e, m, d):
    data = pd.DataFrame(d)
    method = m
    total = sum(e.values())

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
            st.write( "Total time: ", round(total, 4))  


