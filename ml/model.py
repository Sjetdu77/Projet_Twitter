import pandas as pd, numpy as np
from datetime import datetime
from sklearn.model_selection import train_test_split as tts

class DataHandler:
    """Get data from sources"""

    def __init__(self):
        #self.csvfile1 = pd.read_csv('./data/labels.csv')
        #self.csvfile2 = None
        #self.grouped_data = self.csvfile1(self.csvfile2)

        self.grouped_data = pd.read_csv('./data/labels.csv')

class FeatureRecipe:
    """Feature processing class"""

    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.continuous = []
        self.categorical = []
        self.discrete = []
        self.datetime = []

        categories()

        self.all = [
            self.continuous,
            self.categorical,
            self.discrete,
            self.datetime
        ]

    def categories():
        for i in data:
            if data[i].dtype == 'float64':
                self.continuous.append(True)
                self.categorical.append(False)
                self.discrete.append(False)
            else:
                self.continuous.append(False)
                self.categorical.append(True)
                self.discrete.append(True)

            self.datetime.append(False)

class FeatureExtractor:
    """Feature Extractor class"""

    def __init__(self, data: pd.DataFrame, flist: list):
        """ Input : pandas.DataFrame, feature list to drop
            Output : X_train, X_test, y_train, y_test according to sklearn.model_selection.train_test_split"""
        y = None
        if 'class' in data: y = data['class']
        x = data['tweet']
        self.train_test = tts(x, y)


class ModelBuilder:
    """Class for train and print results of ml model"""

    def __init__(self, model_path: str = None, save: bool = None):
        pass

    def __repr__(self):
        pass

    def train(self, X, Y):
        pass

    def predict_test(self, X) -> np.ndarray:
        pass

    def predict_from_dump(self, X) -> np.ndarray:
        pass

    def save_model(self, path: str):
        #with the format : ‘model_{}_{}’.format(date)
        pass

    def print_accuracy(self):
        pass

    def load_model(self):
        try:
            #load model
            pass
        except:
            pass
