import pandas as pd
# import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

sns.set_style('whitegrid')
# sns.set(palette='Paired')





            

        # create another class just for the chart alone
        
# class OutcomeChart:
#     def __init__(self, chess):
#         self.outcome_data = chess.groupby(['victory_status'])[['id']].count()
        
#     def create_stats(self):
#         outcome = self.outcome_data.sort_values('id')
#         outcome.rename(columns={'id': 'Total'}, inplace = True)
#         outcome.loc["SUM"] = outcome["Total"].sum()
        
        
#         outcome['percentage'] = (outcome['Total'] / outcome.loc['SUM']['Total'])*100
#         outcome['percentage'] = outcome['percentage'].map(lambda perc: round(perc, 2))
#         outcome_chart = outcome.iloc[:-1].reset_index()
        
#         return outcome_chart
    
    
#     def piechart(self, filename):
#         outcome_chart = self.create_stats()
#         outcome_chart.plot(kind='pie', y = 'Total', autopct='%1.2f%%',
#                            startangle=0, shadow=False,
#                            labels=outcome_chart['victory_status'],
#                            legend = False, fontsize=20, figsize=(10,10))
#         plt.savefig(filename)
#         plt.close()


# ----------------------------------------------------------


# class CategoryStats:
#     def __init__(self, uhs):
#         self.current_uhs = uhs[uhs.date_end >= 2022]

#     def create_stats(self):
#         category_stats = self.current_uhs.groupby('category', as_index=False).size()
#         category_stats['percentage'] = (category_stats['size'] / len(self.current_uhs)) * 100
#         category_stats['percentage'] = category_stats['percentage'].map(lambda perc: round(perc, 2))

#         return category_stats

#     def to_csv(self, filename):
#         category_stats = self.create_stats()
#         category_stats.to_csv(filename, index=False)

#     def barchart(self, filename):
#         sns.countplot(x='category', data=self.current_uhs)
#         plt.savefig(filename)
#         plt.close()

# ----------------------------------------------------------

class OutcomeStats:
    def __init__(self, chess):
        self.outcome_data = chess.groupby(['victory_status'])[['id']].count()
        
    def create_stats(self):
        outcome = self.outcome_data.sort_values('id')
        outcome.rename(columns={'id': 'Total'}, inplace = True)
        outcome.loc["SUM"] = outcome["Total"].sum()
        
        
        outcome['percentage'] = (outcome['Total'] / outcome.loc['SUM']['Total'])*100
        outcome['percentage'] = outcome['percentage'].map(lambda perc: round(perc, 2))
        
        return outcome

    def to_csv(self, filename):
        outcome = self.create_stats()
        outcome.to_csv(filename, index=True)

    def piechart(self, filename):
        outcome_chart = self.create_stats()
        outcome_chart = outcome_chart.iloc[:-1].reset_index()
        outcome_chart.plot(kind='pie', y = 'Total', autopct='%1.2f%%',
                           startangle=0, shadow=False,
                           labels=outcome_chart['victory_status'],
                           legend = False, fontsize=20, figsize=(10,10))
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()


# ----------------------------------------------------------


class WinnerColour:
    def __init__(self, chess):
        self.winner_data = chess.groupby(['winner'])[['id']].count()
    
    def create_stats(self):
        winner_colour = self.winner_data.sort_values('id')
        winner_colour.rename(columns={'id': 'Number of Victories'}, inplace = True)
        winner_colour['Percentage of Victories'] = (winner_colour['Number of Victories'] / winner_colour['Number of Victories'].sum())*100
        winner_colour['Percentage of Victories']=winner_colour['Percentage of Victories'].map(lambda perc: round(perc, 2))
        
        return winner_colour
    
    def to_csv(self, filename):
        winner_colour = self.create_stats()
        winner_colour.to_csv(filename, index=True)
        
    def barchart(self, filename):
        winner = self.create_stats()
        # sns.set(rc={'figure.figsize':(10,7)})
        winner.reset_index(inplace=True)
        ax = sns.barplot(y = 'Number of Victories', x = 'winner',  data = winner, palette=[ "#FFD700" , "#000000",'#F5F5F5'])
        ax.bar_label(ax.containers[0])
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()    
        
# ----------------------------------------------------------        

class OpeningNames:
    def __init__(self, chess):
        self.opening_data  = chess.groupby(['opening_name'])[['id']].count()
   
    def create_stats(self):
        opening_names = self.opening_data.sort_values('id', ascending = False)
        opening_names.rename(columns = {'id':'count'}, inplace= True)
        opening_names.reset_index(inplace = True)
        return opening_names
    
    
    def to_csv(self, filename):
        opening_names = self.create_stats()
        opening_names.to_csv(filename)
        # , index=False)

    def figure(self, filename):
        top20opening = self.create_stats()
        top20opening = top20opening.iloc[:20]
        ax = top20opening.plot.barh(x = 'opening_name', y = 'count')
        ax.bar_label(ax.containers[0])
        plt.title('Top 20 Opening Names')
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()         

# ----------------------------------------------------------

class TopOpeningOutcome:
    def __init__(self, chess):
        self.opening_name_outcome_data  = chess.groupby(['opening_name','victory_status'])[['id']].count()
        self.opening_data  = chess.groupby(['opening_name'])[['id']].count()
        
    def create_stats(self):
        opening_name_outcome = self.opening_name_outcome_data.sort_values('opening_name', ascending = True)
        opening_name_outcome.rename(columns = {'id':'count'}, inplace= True)
        
        top_opening_6 = self.opening_data.sort_values('id', ascending = False).reset_index()     
        top_opening_6 = top_opening_6.iloc[:6]
        
        aggregate_opening_outcome =  opening_name_outcome.loc[top_opening_6['opening_name'].to_numpy()]
        aggregate_opening_outcome = aggregate_opening_outcome.sort_values(by = ["victory_status", "count"], ascending =  False)
        
        return aggregate_opening_outcome
    
    
    def to_csv(self, filename):
        aggregate_opening_outcome  = self.create_stats()
        aggregate_opening_outcome.to_csv(filename, index=True)
        
        
    def figure1(self, filename):
        aggregate_opening_outcome = self.create_stats()
        ax = aggregate_opening_outcome.plot.barh(rot=0)
        ax.bar_label(ax.containers[0])
        plt.title('Top 6 Opening Names: Aggregate Outcomes I')
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
    
    
    def figure2(self, filename):
        aggregate_opening_outcome = self.create_stats()
        aggregate_opening_outcome.reset_index(inplace = True)
        ax2 = aggregate_opening_outcome.pivot(index ='opening_name', columns = 'victory_status' , values='count').plot(kind='barh')
        ax2.bar_label(ax2.containers[0])
        ax2.bar_label(ax2.containers[1])
        ax2.bar_label(ax2.containers[2])
        ax2.bar_label(ax2.containers[3])
        plt.title('Top 6 Opening Names: Aggregate Outcomes II - Separated Opening Moves')
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()

    def figure3(self, filename):
        aggregate_opening_outcome = self.create_stats()
        aggregate_opening_outcome.reset_index(inplace = True)
        ax2 = aggregate_opening_outcome.pivot(index ='victory_status', columns = 'opening_name' , values='count').plot(kind='barh')
        for container in ax2.containers:
            ax2.bar_label(container)
        plt.title('Top 6 Opening Names: Aggregate Outcomes III - Separated Match Outcomes')
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()


# ----------------------------------------------------------   

class TopOpeningColourPieceWinner:
    def __init__(self, chess):
        self.opening_name_winner_data  = chess.groupby(['opening_name','winner'])[['id']].count()
        self.opening_data  = chess.groupby(['opening_name'])[['id']].count()
        
    def create_stats(self):
        opening_name_winner = self.opening_name_winner_data.sort_values('opening_name', ascending = True)
        opening_name_winner.rename(columns = {'id':'count'}, inplace= True)
        
        top_opening_6 = self.opening_data.sort_values('id', ascending = False).reset_index()     
        top_opening_6 = top_opening_6.iloc[:6]
        
        aggregate_opening_name_winner =  opening_name_winner.loc[top_opening_6['opening_name'].to_numpy()]
        aggregate_opening_name_winner = aggregate_opening_name_winner.sort_values(by = ["winner", "count"], ascending =  False)
        
        return aggregate_opening_name_winner
    
    
    def to_csv(self, filename):
        aggregate_opening_name_winner  = self.create_stats()
        aggregate_opening_name_winner.to_csv(filename, index=True)
        
        
    def figure1(self, filename):
        aggregate_opening_name_winner = self.create_stats()
        ax = aggregate_opening_name_winner.plot.barh(rot=0)
        ax.bar_label(ax.containers[0])
        plt.title('Top 6 Opening Names: Aggregate Outcomes I')
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
    
    
    def figure2(self, filename):
        aggregate_opening_name_winner = self.create_stats()
        aggregate_opening_name_winner.reset_index(inplace = True)
        ax2 = aggregate_opening_name_winner.pivot(index ='opening_name', columns = 'winner' , values='count').plot(kind='barh')
        for container in ax2.containers:
            ax2.bar_label(container)
        plt.title('Top 6 Opening Names: Aggregate Outcomes by Chess Piece Colour  II \n - Opening Moves')
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()

    def figure3(self, filename):
        aggregate_opening_name_winner = self.create_stats()
        aggregate_opening_name_winner.reset_index(inplace = True)
        ax2 = aggregate_opening_name_winner.pivot(index ='winner', columns = 'opening_name' , values='count').plot(kind='barh')
        for container in ax2.containers:
            ax2.bar_label(container)
        plt.title('Top 6 Opening Names: Aggregate Outcomes by Chess Piece Colour III')
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()

# ----------------------------------------------------------        



class FrequentPlayers:
    def __init__(self, chess):
        self.white_data  = list(chess['white_id'].to_numpy())
        self.black_data  = list(chess['black_id'].to_numpy())
    
    
    def create_frame(self):
        players = self.white_data + self.black_data
        players =  pd.Series(players).value_counts()
        players = players.to_frame().reset_index()
        players.rename(columns = { 0:'matches played','index':'Player ID'}, inplace=True)
        
        return players
    
    
    def to_csv(self, filename):
        players  = self.create_frame()
        players.to_csv(filename, index=True)
        
        
    def figure(self, filename):
        freq20players = self.create_frame()
        freq20players = freq20players.iloc[:20]
        ax = freq20players.plot.barh(x = 'Player ID', y = 'matches played')
        ax.bar_label(ax.containers[0])
        plt.title('Top 20 Frequent  Game Player')
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()         


# ----------------------------------------------------------        

class TopPlayers:
    def __init__(self, chess):
        self.topWhitePlayers_data  = chess['white_id'][chess['winner'] == 'white'].value_counts()
        self.topBlackPlayers_data   =  chess['black_id'][chess['winner'] == 'black'].value_counts()
    
    
    def create_frame(self):
        stars = pd.DataFrame(self.topWhitePlayers_data.append(self.topBlackPlayers_data), columns = ['Matches_Won'])
        stars.sort_values(by = ['Matches_Won'], ascending = False, inplace = True)
        stars['Player ID'] = stars.index
        
        top_players = stars.groupby('Player ID').sum().reset_index()
        top_players.sort_values('Matches_Won', ascending=False, inplace = True)
        
        return top_players
    
    
    def to_csv(self, filename):
        top_players  = self.create_frame()
        top_players.to_csv(filename, index=True)
        
        
    def figure(self, filename):
        top10_players = self.create_frame()
        top10_players = top10_players.iloc[:10]      
        ax = sns.barplot(y = 'Player ID', x = 'Matches_Won', data = top10_players, palette='Set3' )
        ax.bar_label(ax.containers[0])    
        plt.title('Top 10 Game Players - Most Wins')
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()         


# ----------------------------------------------------------      

class PlayersRating:
    def __init__(self, chess):
        self.white_rating  = chess['white_rating']
        self.black_rating = chess['black_rating']
    
    # def create_stats(self):
    #     abc = self.
        
    #     return abc
    
    
    # def to_csv(self, filename):
    #       = self.create_stats()
    #     .to_csv(filename, index=True)
        
        
    def figure(self, filename):
        dims = (10, 7.5)
        fig, ax = plt.subplots(1,2,figsize=dims)
        #Distribution of white's rating
        sns.histplot(self.white_rating, bins = 20, ax = ax[0], kde=True)
        #Distribution of black's rating
        sns.histplot(self.black_rating, bins = 20, ax = ax[1], kde=True)

        ax_attr = ax[0].set(title = "Distribution of White's Rating")
        ax_attr = ax[1].set(title = "Distribution of Black's Rating")
        # sns.set(rc={'figure.figsize':(10,7)})
        # sns.countplot(x='winner', data=self.chess, palette=['#F5F5F5',"#000000", "#FFD700"])         
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()    

# ----------------------------------------------------------    


#########-----------------------------------------#####################################################        
# class xyz:
#     def __init__(self, chess):
#         self.  = chess.
    
    
#     def create_stats(self):
#         abc = self.
        
#         return abc
    
    
#     def to_csv(self, filename):
#          = self.create_stats()
#         .to_csv(filename, index=True)
        
        
    # def figure(self, filename):
    #     sns.set(rc={'figure.figsize':(10,7)})
    #     sns.countplot(x='winner', data=self.chess, palette=['#F5F5F5',"#000000", "#FFD700"])         
    #     plt.tight_layout()
    #     plt.savefig(filename)
    #     plt.close()    
#########-----------------------------------------#####################################################        