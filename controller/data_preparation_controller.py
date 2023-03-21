from method.clean import *
from method.encode import *
from method.scale import *
from method.extraction import Extraction
import time
import streamlit as st


@st.cache
class DataPreparation:

    def __init__(self, m, d):
        self.method = m
        self.data = d

    @st.cache(allow_output_mutation=True)
    def executeWithFE(self):
        startClean = time.time()
        cResult= self.__dataClean()
        timeClean = time.time() - startClean

        startEncode = time.time()
        eResult= self.__dataEncode(cResult)
        timeEncode = time.time() - startEncode

        startScale = time.time()
        sResult = self.__dataScale(eResult)
        timeScale = time.time() - startScale

        startFE = time.time()
        feResult = self.__featuresExtraction(sResult)
        timeFE =  time.time() - startFE

        total = timeClean + timeEncode + timeScale + timeFE

        timeExecute = {
            'Clean' : timeClean,
            'encode' : timeEncode,
            'scale' : timeScale,
            'extraction' : timeFE,
            'total' : total
        }

        return feResult, timeExecute
    
    @st.cache
    def executeWithoutFe(self):
        startClean = time.time()
        cResult= self.__dataClean()
        timeClean = time.time() - startClean

        startEncode = time.time()
        eResult= self.__dataEncode(cResult)
        timeEncode = time.time() - startEncode

        startScale = time.time()
        sResult = self.__dataScale(eResult)
        timeScale = time.time() - startScale

        total = timeClean + timeEncode + timeScale

        timeExecute = {
            'Clean' : timeClean,
            'encode' : timeEncode,
            'scale' : timeScale,
            'extraction' : False,
            'total' : total
        }

        return sResult, timeExecute
        
    def __dataClean(self):
        clean = Clean()
        result = clean.cleanDf(self.data)
        column_headers = list(result.columns.values)

        id = result[st.session_state['idName']].copy()

        if st.session_state['idName'] in column_headers:
            result.pop(st.session_state['idName'])

        st.session_state['datasetId'] = id

        return result
    

    def __dataEncode(self, c):
        data = c
        encode = Encode(data)

        match self.method['encode']:
            case 'One Hot Encoding':
                oheResult = encode.oneHotEncoding()
                return oheResult

            case 'Label Encoding':
                leResult = encode.labelEncoding()
                return leResult

            case 'Ordinal Encoding':
                teResult = encode.ordinalEncoding()
                return teResult
            
            case _:
                return 'failed'
        

    def __dataScale(self, er):
        data = er
        scale = Scale(data)

        match self.method['scale']:
            case 'Standard Scaler':
                ssResult = scale.standardScaler()
                return ssResult

            case 'Min Max Scaler':
                mmsResult = scale.minMaxScaler()
                return mmsResult
            
            case 'Max Abs Scaler':
                masResult = scale.maxAbsScaler()
                return masResult

            case 'Robust Scaler':
                rsResult = scale.robustScaler()
                return rsResult
            
            case _:
                return 'failed'
        

    def __featuresExtraction(self, sr):
        data = sr
        reduction = self.method['dimension']
        extract = Extraction(data, reduction)

        match self.method['extraction']:
            case 'PCA':
                pcaResult = extract.pcaExtraction()
                return pcaResult

            case 'T-SNE':
                tsnesResult = extract.tsneExtraction()
                return tsnesResult
            
            case _:
                return 'failed'
