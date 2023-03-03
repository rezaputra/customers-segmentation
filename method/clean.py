
import pandas as pd
import streamlit as st

class Clean:

    def cleanDf(self,d):
        data = pd.DataFrame(d)
        data = data.dropna(how='any',axis=0)
        data = data.drop_duplicates()

        return data