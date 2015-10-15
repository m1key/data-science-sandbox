import pandas as pd

data = pd.read_csv('Infectious_Disease_Cases_by_County__Year__and_Sex__2001-2014.csv')
by_gender = data.groupby(['Disease', 'Sex']).sum().reset_index().pivot_table('Count', index='Disease', columns='Sex')
print by_gender[by_gender.index.map(lambda x: 'Malaria' in x)]
by_gender['Difference'] = by_gender['Male'] - by_gender['Female']
print by_gender.sort('Difference', ascending = False)
print by_gender[by_gender['Difference'] > 0 ].size
print by_gender[by_gender['Difference'] < 0 ].size
print by_gender[by_gender['Difference'] == 0 ].size


