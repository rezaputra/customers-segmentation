import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler

def standardScaler(d):
    data = pd.DataFrame(d)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    # scaled_data = pd.DataFrame(scaler.fit_transform(data), columns=scaler.get_feature_names_out())
    
    return scaled_data

def minMaxScaler(d):
    data = pd.DataFrame(d)
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)

    return scaled_data

def maxAbsScaler(d):
    data = pd.DataFrame(d)
    scaler = MaxAbsScaler()
    scaled_data = scaler.fit_transform(data)
    
    return scaled_data

def robustScaler(d):
    data = pd.DataFrame(d)
    scaler = RobustScaler()
    scaled_data = scaler.fit_transform(data)
    
    return scaled_data