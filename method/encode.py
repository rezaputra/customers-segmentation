import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OneHotEncoder

class Encode:
    def __init__(self, d):
        self.data = pd.DataFrame(d)
        self.ctg = (self.data.dtypes == "object")
        self.ctg_cols = list(self.ctg[self.ctg].index)
        self.num = self.data.drop(self.ctg_cols,axis=1)

    def labelEncoding(self):
        data = self.data.apply(LabelEncoder().fit_transform)

        return data

    def oneHotEncoding(self):
        enc = OneHotEncoder()
        encoded = pd.DataFrame(enc.fit_transform(self.data[self.ctg_cols]).toarray(), columns=enc.get_feature_names_out())
        data = pd.concat([self.num, encoded], axis=1, join='inner')

        return data

    def ordinalEncoding(self):
        oe = OneHotEncoder()
        encoded = pd.DataFrame(oe.fit_transform(self.data[self.ctg_cols]).toarray(), columns=oe.get_feature_names_out())
        data = pd.concat([self.num, encoded], axis=1, join='inner')

        return 
    

    