import pandas as pd

directory = 'ml-1m/'

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table(directory + 'users.dat', sep='::', header=None, names=unames, engine='python')

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(directory + 'users.dat', sep='::', header=None, names=rnames, engine='python')

