import pandas as pd
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

# @st.cache
class Extraction:
    def __init__(self, d, r):
        self.data = pd.DataFrame(d.copy())
        self.reduction = r


    def _attributeName(self, name):
        column = []
        for x in range(self.reduction):
            value = str(name + str(x))
            column.append(value)

        return column
    
    
    def pcaExtraction(self):
        column = self._attributeName('PCA')
        pca = PCA(n_components=self.reduction)
        pca_x = pca.fit_transform(self.data)
        data = pd.DataFrame(data=pca_x, columns=column)

        return data


    def tsneExtraction(self):
        column = self._attributeName('T-SNE')
        tsne = TSNE(n_components=self.reduction)
        tsne_x = tsne.fit_transform(self.data)
        data = pd.DataFrame(data=tsne_x, columns=column)

        return data
    

    