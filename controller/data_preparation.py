import pandas as pd
from method.clean import *
from method.encode import *
from method.scale import *
from method.reduction import *


# @st.cache
def dataEncode(m, d):
    method = m
    data = pd.DataFrame(d)
    cleanResult = cleanDf(data)

    match method['encode']:
        case 'One Hot Encoding':
            oheResult = oneHotEncoding(cleanResult)
            return oheResult

        case 'Label Encoding':
            leResult = labelEncoding(cleanResult)
            return leResult

        case 'Ordinal Encoding':
            teResult = ordinalEncoding(cleanResult)
            return teResult
        
        case _:
            return 'failed'
        

def dataScale(m, d):
    method = m
    data = pd.DataFrame(d) 

    match method['scale']:
        case 'Standard Scaler':
            ssResult = standardScaler(data)
            return ssResult

        case 'Min Max Scaler':
            mmsResult = minMaxScaler(data)
            return mmsResult
        
        case 'Max Abs Scaler':
            masResult = maxAbsScaler(data)
            return masResult

        case 'Robust Scaler':
            rsResult = robustScaler(data)
            return rsResult
        
        case _:
            return 'failed'
        
def dimensionReduction(m, d):
    method = m
    reduction = m['dimension']
    data = pd.DataFrame(d) 

    match method['extraction']:
        case 'PCA':
            pcaResult = pcaReduction(data, reduction)
            return pcaResult

        case 'UMAP':
            umapsResult = umapReduction(data, reduction)
            return umapsResult
        
        case _:
            return 'failed'

    




