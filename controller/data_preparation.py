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

    @st.cache
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

        timeExecute = {
            'Clean' : timeClean,
            'encode' : timeEncode,
            'scale' : timeScale,
            'extraction' : timeFE
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

        timeExecute = {
            'Clean' : timeClean,
            'encode' : timeEncode,
            'scale' : timeScale,
            'extraction' : False
        }

        return sResult, timeExecute
        
    def __dataClean(self):
        clean = Clean()
        data = clean.cleanDf(self.data)

        return data
    

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

    




