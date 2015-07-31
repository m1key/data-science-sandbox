import pandas as pd

data = {'Mike': {2015: {'weight': 75, 'strength': 80}, 2014: {'weight': 65, 'strength': 60}, 2013: {'weight': 85, 'strength': 100}}, 'Kartik': {2015: {'weight': 70, 'strength': 85}, 2014: {'weight': 69, 'strength': 84}, 2013: {'weight': 68, 'strength': 83}}}
frame = pd.Panel.from_dict(data).to_frame()

print frame
print frame.ix['strength']
print frame.ix['strength'].max()
print frame['Kartik'].ix['weight'] # frame['Kartik']['weight']
frame.columns.names = ['names']
frame.index.names = ['feature', 'year']
print frame.sum(level = 'feature')

frame4 = pd.DataFrame({'strength': [10, 20, 30, 40], 'weight': [80,70,60,90], 'year': [2015,2015,2014,2014], 'name': ['Mike', 'Kartik', 'Mike', 'Kartik']})
print frame4.groupby('name').max()

