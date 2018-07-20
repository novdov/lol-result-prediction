import os
import pandas as pd
from sklearn.model_selection import train_test_split

PATH = 'data'
file_name = 'game_results_tier.csv'


class DataSplit:
    def __init__(self, path, file_name):
        self.path = path
        self.file_name = file_name
        self.data = pd.read_csv(os.path.join(self.path, self.file_name))

    def data_split(self):
        train, test = train_test_split(self.data)
        return train, test


def main():
    ds = DataSplit(PATH, file_name)
    train, test = ds.data_split()
    train.to_csv(os.path.join(PATH, 'train_tier.csv'), index=False)
    test.to_csv(os.path.join(PATH, 'test_tier.csv'), index=False)


if __name__ == '__main__':
    main()
