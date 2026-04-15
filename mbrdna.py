#!/bin/python3

import math
import os
import random
import re
import sys

import numpy as np
import pandas as pd
import itertools
from sklearn.utils import shuffle
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


def select_k_best(data, target, k):
    """
    Return list of k best featues

    Parameters:
    -----------
    data: 2D_FLOAT_ARRAY
        2D Numpy array representing the data

    target: 1D_INTEGER_ARRAY
        1D Numpy array representing the labels

    k: int
        Number of features to return

    Returns:
    -------
    python-list of indices representing the best features
    """
    x = data.iloc[:, 0:30]
    y = target.iloc[:, -1]
    # k = 5

    bestfeatures = SelectKBest(score_func=chi2, k=5)
    fit = bestfeatures.fit(x, y)
    dfscores = pd.DataFrame(fit.scores_)
    dfcolumns = pd.DataFrame(x.columns)