# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 23:40:45 2022

@author: Olu
"""

import pandas as pd

# from util_chess import OutcomeStats, WinnerColour, OpeningNames, TopOpeningOutcome, TopOpeningColourPieceOutcome

from util_chess import *

def analyze_desc(chess):
    desc = Description(chess)
    desc.to_csv('results/desc.csv')

def analyze_outcome(chess):
    outcome = OutcomeStats(chess)
    outcome.to_csv('results/outcome.csv')  
    outcome.piechart('results/outcome_piechart.pdf')
    outcome.piechart('results/outcome_piechart.png')


def analyze_winner_colour(chess):
    winner_colour = WinnerColour(chess)
    winner_colour.to_csv('results/winner_colour.csv')
    winner_colour.barchart('results/winner_colour.pdf')
    winner_colour.barchart('results/winner_colour.png')


def analyze_opening_names(chess):
    opening_names = OpeningNames(chess)
    opening_names.to_csv('results/opening_names.csv')
    opening_names.figure('results/opening_names.pdf')
    opening_names.figure('results/opening_names.png')

def analyze_aggregate_opening_outcome(chess):
    aggregate_opening_outcome = TopOpeningOutcome(chess)
    aggregate_opening_outcome.to_csv('results/aggregate_opening_outcome.csv')
    aggregate_opening_outcome.figure1('results/aggregate_opening_outcome.pdf')
    aggregate_opening_outcome.figure1('results/aggregate_opening_outcome.png')
    aggregate_opening_outcome.figure2('results/aggregate_opening_outcome2.pdf')
    aggregate_opening_outcome.figure2('results/aggregate_opening_outcome2.png')
    aggregate_opening_outcome.figure3('results/aggregate_opening_outcome3.pdf')
    aggregate_opening_outcome.figure3('results/aggregate_opening_outcome3.png')


def analyze_opening_name_winner(chess):
    opening_name_winner = TopOpeningColourPieceWinner(chess)
    opening_name_winner.to_csv('results/opening_name_winner.csv')
    opening_name_winner.figure1('results/opening_name_winner1.pdf')
    opening_name_winner.figure1('results/opening_name_winner1.png')
    opening_name_winner.figure2('results/opening_name_winner2.pdf')
    opening_name_winner.figure2('results/opening_name_winner2.png')
    opening_name_winner.figure3('results/opening_name_winner3.pdf')
    opening_name_winner.figure3('results/opening_name_winner3.png')

def analyze_frequent_players(chess):
    frequent_players = FrequentPlayers(chess)
    frequent_players.to_csv('results/frequent_players.csv')
    frequent_players.figure('results/frequent_players.pdf')
    frequent_players.figure('results/frequent_players.png')

def analyze_top_players(chess):
    top_players = TopPlayers(chess)
    top_players.to_csv('results/top_players.csv')
    top_players.figure('results/top10_players.pdf')
    top_players.figure('results/top10_players.png')      
 

def analyze_players_rating(chess):
    players_rating = PlayersRating(chess)
    players_rating.figure('results/players_rating.pdf')
    players_rating.figure('results/players_rating.png')   


def analyze(chess):
    analyze_outcome(chess)
    analyze_winner_colour(chess)
    analyze_opening_names(chess)
    analyze_aggregate_opening_outcome(chess)
    analyze_opening_name_winner(chess)
    analyze_frequent_players(chess)
    analyze_top_players(chess)
    analyze_players_rating(chess)
    analyze_desc(chess)
   
    
    
    
if __name__ == "__main__":
    chess = pd.read_csv('data/chess_cleandata.csv')
    analyze(chess)
    