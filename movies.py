import pandas as pd

directory = 'ml-1m/'

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table(directory + 'users.dat', sep='::', header=None, names=unames, engine='python')

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(directory + 'ratings.dat', sep='::', header=None, names=rnames, engine='python')

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table(directory + 'movies.dat', sep='::', header=None, names=mnames, engine='python')

data = pd.merge(pd.merge(ratings, users), movies)

mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')

mean_ratings['difference'] = abs(mean_ratings['F'] - mean_ratings['M'])
mean_ratings.sort(['difference'], ascending=False, inplace=True)
print mean_ratings[:5]
