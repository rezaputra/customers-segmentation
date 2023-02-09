import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OneHotEncoder

def oneHotEncoding(d):
    data = pd.DataFrame(d)
    ctg = (data.dtypes == "object")
    ctg_cols = list(ctg[ctg].index)
    num = data.drop(ctg_cols,axis=1)

    enc = OneHotEncoder()
    encoded = pd.DataFrame(enc.fit_transform(data[ctg_cols]).toarray(), columns=enc.get_feature_names_out())
    data = pd.concat([num, encoded], axis=1, join='inner')

    return data

def labelEncoding(d):
    data = pd.DataFrame(d)
    data = data.apply(LabelEncoder().fit_transform)

    return data

def ordinalEncoding(d):
    data = pd.DataFrame(d)
    ctg = (data.dtypes == "object")
    ctg_cols = list(ctg[ctg].index)
    num = data.drop(ctg_cols,axis=1)
    oe = OneHotEncoder()

    encoded = pd.DataFrame(oe.fit_transform(data[ctg_cols]).toarray(), columns=oe.get_feature_names_out())
    data = pd.concat([num, encoded], axis=1, join='inner')


    return data