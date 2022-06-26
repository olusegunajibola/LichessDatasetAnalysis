# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 07:18:17 2022

@author: Olu
"""

import pandas as pd

from preprocessing_chess import preprocess
from analysis_chess import analyze

if __name__ == "__main__":
    chess = pd.read_csv('games.csv')
    preprocess(chess)
    analyze(chess)