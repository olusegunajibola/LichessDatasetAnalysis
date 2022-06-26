# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 23:58:08 2022

@author: Mido & Olu
"""

import pandas as pd
# import os

# os.makedirs("results")
# os.makedirs("data")


def cleaning_valuse(chess):
    chess ['id'] = chess.id .astype('str')
    chess ['white_id'] = chess.white_id.astype('str')  
    chess ['black_id'] = chess.black_id.astype('str')  
    chess ['opening_name'] =chess.opening_name.astype('str')   
    
    
def cleaning_columns(chess):
    cols_to_eliminate = ['moves','opening_eco','last_move_at','created_at']
    chess.drop(labels=cols_to_eliminate, axis='columns', inplace=True)
    col_to_rename = {'opening_ply':'Number of moves in the opening phase'}
    chess.rename (columns = col_to_rename, inplace = True)
    
    
def preprocess(chess):
    cleaning_valuse(chess)    
    cleaning_columns(chess)
    

if __name__ == "__main__":
    chess = pd.read_csv('games.csv')
    preprocess(chess)
    chess.to_csv ('data/chess_cleandata.csv', index = False)    