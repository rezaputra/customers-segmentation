import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler


class Scale:
    def __init__(self, d):
        self.data = pd.DataFrame(d)

    def standardScaler(self):
        scaler = StandardScaler()
        data = scaler.fit_transform(self.data)
        # scaled_data = pd.DataFrame(scaler.fit_transform(data), columns=scaler.get_feature_names_out())
        
        return data

    def minMaxScaler(self):
        scaler = MinMaxScaler()
        data = scaler.fit_transform(self.data)

        return data

    def maxAbsScaler(self):
        scaler = MaxAbsScaler()
        data = scaler.fit_transform(self.data)
        
        return data

    def robustScaler(self):
        scaler = RobustScaler()
        data = scaler.fit_transform(self.data)
        
        return data