import os
import shutil
import urllib.request
import pandas as pd


class DataLoader:
    url: str = ''
    directory_name: str = ''
    zip_file_name: str = ''
    DATA_DIRECTORY: str = '/app/data'
    files: list[str] = []

    def load(self):
        raise NotImplementedError('not imple...')

    def buildFilePath(self, file_name):
        return f'{self.DATA_DIRECTORY}/{self.directory_name}/{file_name}'

    def zip_file_path(self):
        return f'{self.DATA_DIRECTORY}/{self.directory_name}/{self.zip_file_name}'

    def exists(self):
        for file in self.files:
            if os.path.isfile(f'{self.buildFilePath(file)}'):
                return True
        return False

    def download(self):
        os.makedirs(f'{self.DATA_DIRECTORY}/{self.directory_name}', exist_ok=True)

        data = urllib.request.urlopen(self.url).read()
        with open(self.zip_file_path(), mode='wb') as f:
            f.write(data)

    def decompress(self):
        decompress_path = f'{self.DATA_DIRECTORY}/{self.directory_name}'
        a = shutil.unpack_archive(self.zip_file_path(), decompress_path)


class MovieLens25MDataLoader(DataLoader):
    def __init__(self):
        self.url = 'https://files.grouplens.org/datasets/movielens/ml-25m.zip'
        self.directory_name = 'ml-25m'
        self.zip_file_name = 'ml-25m.zip'
        self.files = [
            'genome-scores.csv', 'genome-tags.csv', 'links.csv',
            'movies.csv', 'ratings.csv', 'tags.csv'
        ]

    def buildFilePath(self, file_name):
        return f'{self.DATA_DIRECTORY}/{self.directory_name}/ml-25m/{file_name}'

    def load(self):

        if not self.exists():
            print('file is not found. downloading...')
            self.download()
            self.decompress()
        else:
            print('file is found. loading...')

        data = {}
        for file in self.files:
            file_path = self.buildFilePath(file)
            key = file.split('.csv')[0]
            data.update({
                key: pd.read_csv(file_path)
            })
        return data

class MovieLens20MDataLoader(DataLoader):
    def __init__(self):
        self.url = 'https://files.grouplens.org/datasets/movielens/ml-20m.zip'
        self.directory_name = 'ml-20m'
        self.zip_file_name = 'ml-20m.zip'
        self.files = [
            'genome-scores.csv', 'genome-tags.csv', 'links.csv',
            'movies.csv', 'ratings.csv', 'tags.csv'
        ]

    def buildFilePath(self, file_name):
        return f'{self.DATA_DIRECTORY}/{self.directory_name}/ml-20m/{file_name}'

    def load(self):

        if not self.exists():
            print('file is not found. downloading...')
            self.download()
            print('downloaded.')
            self.decompress()
            print('decompressed.')
        else:
            print('file is found. loading...')

        data = {}
        for file in self.files:
            file_path = self.buildFilePath(file)
            key = file.split('.csv')[0]
            data.update({
                key: pd.read_csv(file_path)
            })
        return data