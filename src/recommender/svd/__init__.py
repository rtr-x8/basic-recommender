import pandas as pd
import scipy
from scipy.sparse.linalg import svds
import numpy as np


class SVDRecommender:
    """
    user_item_matrixは、indexにuserID、columnsにitemIDが入っているものとし、それぞれ重複がない
    """
    P = None
    S = None
    Qt = None
    pred = None

    def __init__(self,
                 user_item_matrix: pd.DataFrame):

        SVDRecommender.data_check(user_item_matrix)

        self.user_item_matrix: pd.DataFrame = user_item_matrix.to_numpy()
        self.user_id_index_map: dict[int: int] = dict(zip(user_item_matrix.index,
                                                          range(len(user_item_matrix.index))))
        self.item_id_index_map: dict[int: int] = dict(zip(user_item_matrix.columns,
                                                          range(len(user_item_matrix.columns))))

    @staticmethod
    def data_check(user_item_matrix: pd.DataFrame) -> bool:
        shape = user_item_matrix.shape
        user_unique = user_item_matrix.index.unique().tolist()
        movie_unique = user_item_matrix.columns.unique().tolist()
        if (len(user_unique), len(movie_unique)) != shape:
            raise ValueError(f'shape is difference: {shape}, {len(user_unique)}, {len(movie_unique)}')
        if user_item_matrix.isna().sum().sum() > 0:
            raise ValueError('na value exists')
        return True

    def __user_index_2_id(self, index: int) -> int:
        for k, v in self.user_id_index_map.items():
            if index == v:
                return k
        raise ValueError('not found key')

    def __movie_index_2_id(self, index: int) -> int:
        for k, v in self.item_id_index_map.items():
            if index == v:
                return
        raise ValueError('not found key')

    def __user_id_2_index(self, id: int) -> int:
        return self.user_id_index_map.get(id)

    def __user_index_2_id(self, id: int) -> int:
        return self.item_id_index_map.get(id)

    def fit(self, k: int = 5):
        self.P, self.S, self.Qt = svds(self.user_item_matrix, k=k)
        self.pred = np.dot(np.dot(self.P, np.diag(self.S)), self.Qt)

    def recommend(self, recommend_user_id: int) -> pd.DataFrame:
        user_index = self.__user_id_2_index(recommend_user_id)
        result = pd.DataFrame(
            self.pred[user_index],
            columns=["score"],
            index=self.item_id_index_map.keys()
        )
        result.index.name = "itemId"
        result = result.sort_values(by="score", ascending=False)
        return result
