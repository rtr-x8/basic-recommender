from typing import Any
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class ContentBasedFilter:

    """
    items:
    indexにitem idを指定しておくこと
    """
    def __init__(self,
                 items: pd.DataFrame,
                 features: list[str]):
        ContentBasedFilter.data_check(items, features)
        self.items: pd.DataFrame = items
        self.features: list[str] = features
        self.item_matrix: pd.DataFrame = None

    @staticmethod
    def data_check(items: pd.DataFrame,
                   features: list[str]):
        data_columns = items.columns
        if len(set(data_columns).intersection(set(features))) != len(features):
            raise ValueError("items dont have feature row.")

        unique_list = items.index.unique()
        if len(items) != len(unique_list):
            raise ValueError('index has dupplicates')

        return True

    def fit(self):
        self.item_matrix = self.__create_similarity_matrix()

    def recommend(self, item_id: Any, top_k: int = 10) -> pd.DataFrame:
        _matrix = self.item_matrix.copy()

        return _matrix[item_id].sort_values(ascending=False).head(top_k)

    def __create_similarity_matrix(self):
        _items = self.items.copy()[self.features]
        _item_ids = _items.index.tolist()

        return pd.DataFrame(
            cosine_similarity(
                self.items[self.features],
                self.items[self.features]
            ),
            columns = self.items.index, index = self.items.index
        )
