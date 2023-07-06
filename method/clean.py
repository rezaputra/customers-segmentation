import pandas as pd

class Clean:

    def cleanDf(self,d):
        data = pd.DataFrame(d)
        data = data.dropna(how='any',axis=0)
        data = data.drop_duplicates()

        return data
    

