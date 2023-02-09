import streamlit as st
import pandas as pd
from controller.data_preparation import dataEncode, dataScale, dimensionReduction
from view.detail import viewDetails


if 'dataPreparation' in st.session_state:
    data = st.session_state['dataPreparation']
    df = pd.DataFrame(data)

    st.markdown('### Choose Data Preparation Method')

    col1, col2, col3 = st.columns([1.4,1,1])

    with col1:
        scale = st.selectbox(
        'Data scaling method:',
        ('Standard Scaler', 'Min Max Scaler', 'Max Abs Scaler', 'Robust Scaler'))
        encode = st.radio(
            "Data encoding method:",
            ('One Hot Encoding', 'Label Encoding', 'Ordinal Encoding'))
    
    with col2:
        check = st.checkbox("Disabled feature extraction", value=1)
        extract = st.radio(
            "Feature extraction method:",
            ('PCA', 'UMAP'), disabled=check)
        dimension = st.slider(
        'Select number dimension reduction:', 1, len(df.axes[1]), 2, disabled=check)
    
        
    with col3:
    # st.write('Encoding method:', encode)
    # st.write('Scaling method:', scale)
    # st.write('Dimension reduction:', extract)
    # st.success('This is a success message!', icon="✅")

        st.text('Method')
        if check:
            method = {
            'encode' : encode,
            'scale' : scale,
            }
        else:
            method = {
            'encode' : encode,
            'scale' : scale,
            'extraction' : extract,
            'dimension' : dimension
            }
        st.write(method)


    st.subheader('Data preparation')
    run = st.button('Run')

    if run:
        if len(method) == 4:
            enResult= dataEncode(method, df)
            seResult = dataScale(method, enResult)
            reResult = dimensionReduction(method, seResult)

            reResult
                    
            # viewDetails(reResult)
        else:
            st.write('R')

else:
    st.subheader('Empty data')
    st.text("Please run previous step first.")
