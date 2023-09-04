import pandas as pd
from matplotlib import pyplot as plt 
import datetime 

movies = pd.read_csv('data.csv')

#movies['date_x'] = pd.to_datetime(movies['date_x'])

#filtering_data = movies.loc[:,['budget_x', 'score', 'date_x']]
#filtering_data = filtering_data.loc[(movies['date_x'] > datetime.datetime(2020,1, 1))]

def menu():
  while True:
    choice = input('1, 2 or 3: ')
    try:
      choice = int(choice)
    except:
      print('The input must be a number between 1 and 3')
      continue

    if (choice >= 1 and choice <= 3):
      if (choice == 1):
        calc_profit()
        break
      elif (choice == 2):
        highest_scores()
        break
      elif (choice == 3):
        graph()
        break
    else:
      continue




def calc_profit():
  print('calc profit')
  movies['profit'] = movies['revenue'] - movies['budget_x']
  print(movies.loc[:,['names', 'profit']].head(5))
  profit = movies['profit'].head(5)
  names = movies['names'].head(5)
  plt.bar(names, profit)
  plt.show()
  

def highest_scores():
    while True:
      min_score = input('What is the minimum score that you want (0-100): ')
      try:
        min_score = int(min_score)
      except:
        print('please make sure the score is an integer')
        continue
      if min_score > 0 and min_score <= 100:
        break
      else:
        print('Please make sure that the number is between 1-100')
        continue
  
    print('highest_scores')
  
    scores = movies.loc[(movies['score'] > min_score)]
    scores = scores.loc[:,['names', 'score']]
    scores = scores.sort_values(['score'], ascending = False)
    scores = scores.reset_index()
    print(scores.head())
  

def graph():
  filt = movies.groupby('genre').budget_x.agg(['max', 'min', 'mean']).head()
  print(filt)
  #filt1 = filt.loc[:,['max','min','mean']]
  #filt2 = filt.loc[:,['genre']]
  #plt.bar(filt2, filt1)
  #plt.show()
  
    
  
    
menu()

#print(movies.loc[movies['genre'] == 'Horror'])
filt = movies.loc[:,['names', 'score', 'genre']]
#print(filt.sort_values(['score', filt['genre'] == 'Horror'], ascending = False).head(10))