import dataclasses

import numpy as np
import pandas as pd
from typing import Union
from abc import abstractmethod

class BaseRecommender:
    @abstractmethod
    def fit(self, data: pd.DataFrame, **keywords) -> void:
        raise NotImplementedError('not impl...')

    @abstractmethod
    def recommend(self, user_id: Union[int, str]) -> RecommendResult:
        raise NotImplementedError('not impl...')

    @abstractmethod
    def data_check(data: pd.DataFrame) -> bool:
        raise NotImplementedError('not impl...')

@dataclasses.dataclass(frozen=True)
class RecommendResult:
    def __init__(self, item_ids: list[Union[int, str]], scores: list[float]):
        RecommendResult.data_check()
        self.item_ids = item_ids
        self.scores = scores

    staticmethod
    def data_check(self, item_ids: list[Union[int, str]], scores: list[float]):
        if len(item_ids) != len(scores):
            raise ValueError('data shape missed')

        return True

    def to_np(self):
        return np.array([self.item_ids, self.scores])

    def to_df(self, sort = True):
        df = pd.DataFrame([self.scores], index=self.item_ids, columns=["score"])
        if sort:
            return df.sort_values(by="score", ascending=False)
        return

class Metrics:
    pass