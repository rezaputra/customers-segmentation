import pandas as pd

def cleanDf(d):
    df = pd.DataFrame(d)
    df = d.dropna(how='any',axis=0)
    df = df.drop_duplicates()

    # num = (df.dtypes != "object")
    # num_cols = list(num[num].index)

    # ctg = (df.dtypes == "object")
    # ctg_cols = list(ctg[ctg].index)

    # numData = df[num_cols]
    # ctgData = df[ctg_cols]

    # data = {'num' : numData,
    #     'cat' : ctgData}

    return df