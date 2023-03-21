import streamlit as st
import pandas as pd
from controller.data_preparation_controller import DataPreparation
from components.detail_data_preparation import viewDetailDpWithFE, viewDetailDpWithoutFE


if 'dataFrame' in st.session_state:
    data = pd.DataFrame(st.session_state['dataFrame'].copy())

    st.markdown('### Choose Data Preparation Method')

    col1, col2, col3 = st.columns([1.2,1,1], gap='large')

    with col1:
        scale = st.selectbox(
        'Data scaling method:',
        ('Standard Scaler', 'Min Max Scaler', 'Max Abs Scaler', 'Robust Scaler'))
        encode = st.radio(
            "Data encoding method:",
            ('One Hot Encoding', 'Label Encoding', 'Ordinal Encoding'), index=1)
        
        
    
    with col2:
        check = st.checkbox("Disabled feature extraction", value=0)
        extract = st.radio(
            "Feature extraction method:",
            ('PCA', 'T-SNE'), disabled=check)
        # dimension = st.slider(
        # 'Select number of dimension:', 2, 3, 2, disabled=check)
        selectD = st.select_slider(
        'Select number of dimension', options=['2D', '3D'], disabled=check)

        if selectD == '3D':
            dimension = 3
        else:
            dimension = 2
    
        
    with col3:
        if check:
            method = {
            'encode' : encode,
            'scale' : scale,
            'extraction' : False,
            'dimension' : False
            }
        else:
            method = {
            'encode' : encode,
            'scale' : scale,
            'extraction' : extract,
            'dimension' : dimension
            }
        st.text('Data preparation info')
        st.write(method)


    st.markdown('### ')
    st.markdown('### Data preparation')
    run = st.button('Run')

    if run:
        try:
            with st.spinner('Wait for it...'):
                if method['extraction'] != False:
                    dp = DataPreparation(method, data)
                    result, timeExe = dp.executeWithFE()
                    st.session_state['dataPreparation'] = result
                    st.session_state['dpMethod'] = method
                    st.session_state['dpTimeProcessing'] = timeExe
                                    
                    viewDetailDpWithFE(timeExe, method, result)

                else:                    
                    dp = DataPreparation(method, data)

                    result, timeExe = dp.executeWithoutFe()
                    st.session_state['dataPreparation'] = result
                    st.session_state['dpMethod'] = method
                    st.session_state['dpTimeProcessing'] = timeExe

                    viewDetailDpWithoutFE(timeExe, method, result)
                st.success('Done!')

        except:
            st.error('Something wrong!')

else:
    st.subheader('Empty data')
    st.text("Please run previous step first.")
