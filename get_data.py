# Sun-Woong KIM

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelBinarizer
from util import categorize_kda


class PrepareData(object):
    """
    Prepare data for training.
    
    Args:
        data: raw data with features and labels
        
    Attributes:
        prepare_data: return data and labels (x, y).
            data: float features + one-hot encoded feature (kda range)
            labels: binarized labels (0/1)
    """
    def __init__(self, data):
        self.data = data.copy()

    def _padding_inf(self):
        max_kda = max(self.data.loc[self.data['kda'] != np.inf]['kda'])
        idx = self.data['kda'] == np.inf
        self.data.loc[idx, 'kda'] = max_kda
        return self.data

    def _categorize_kda(self):
        self.data['kda_range'] = self.data['kda'].apply(categorize_kda)
        return self.data

    def _label_binarize(self):
        lb = LabelBinarizer()
        result_binarized = lb.fit_transform(self.data['result'])
        self.data['result'] = result_binarized
        return self.data

    def prepare_data(self):
        self.data = self._padding_inf()
        self.data = self._categorize_kda()
        self.data = self._label_binarize()
        self.data = pd.get_dummies(self.data, columns=['kda_range'])

        X = self.data.iloc[:, 1:]
        y = self.data['result']
        return X, y
