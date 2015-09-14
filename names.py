import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

years = range(1950, 2015)

pieces = []
columns = ['name', 'sex', 'births']

for year in years:
	path = 'names/yob%d.txt' % year
	frame = pd.read_csv(path, names = columns)
	
	frame['year'] = year
	pieces.append(frame)

names = pd.concat(pieces, ignore_index = True)

total_births = names.pivot_table('births', index = 'year', columns = 'sex', aggfunc = sum)

total_births.plot(title = 'Total births by sex and year').get_figure().savefig('output.png', bbox_inches = 'tight')

def add_prop(group):
	births = group.births.astype(float) # type of births is Series
	group['prop'] = births / births.sum()
	return group

names = names.groupby(['year', 'sex']).apply(add_prop)

# print np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)

def get_top1000(group):
	return group.sort_index(by = 'births', ascending = False)[:1000]
grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
top1000.index = np.arange(len(top1000))

# print top1000

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

total_births = names.pivot_table('births', index = 'year', columns = 'name', aggfunc = sum)
subset = total_births[['Bianca']].fillna(0)
subset.plot(title = 'Number of births per year, USA, logarithmic', grid = True, figsize=(28,20), xticks=range(1950, 2020, 5)).get_figure().savefig('output2.png', bbox_inches = 'tight')

df = boys[boys.year == 2010]
prop_cumsum = df.sort_index(by = 'prop', ascending = False).prop.cumsum()
print prop_cumsum.values.searchsorted(0.5)

def get_quantile_count(group, q = 0.5):
	group = group.sort_index(by = 'prop', ascending = False)
	return group.prop.cumsum().values.searchsorted(q) + 1

diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
diversity.plot(title = 'Number of popular names in top 50%').get_figure().savefig('output3.png', bbox_inches = 'tight')

get_last_letter = lambda x: x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'

table = names.pivot_table('births', index=last_letters, columns = ['sex', 'year'], aggfunc = sum)
subtable = table.reindex(columns = [1910, 1960, 2010], level = 'year')
print subtable.head()

letter_prop = subtable / subtable.sum().astype(float)
fig, axes = plt.subplots(2, 1, figsize = (10, 8))
letter_prop['M'].plot(kind = 'bar', rot = 0, ax = axes[0], title = 'Male').get_figure().savefig('output4.png', bbox_inches = 'tight')
letter_prop['F'].plot(kind = 'bar', rot = 0, ax = axes[1], title = 'Female', legend = False).get_figure().savefig('output5.png', bbox_inches = 'tight')

letter_prop = table / table.sum().astype(float)
dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T
dny_ts.plot().get_figure().savefig('output6.png', bbox_inches = 'tight')

all_names = names.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]
print lesley_like
filtered = names[names.name.isin(lesley_like)]
filtered.groupby('name').births.sum()
table = filtered.pivot_table('births', index = 'year', columns = 'sex', aggfunc = 'sum')
table = table.div(table.sum(1), axis = 0)
table.plot(style = {'M': 'k-', 'F': 'k--'}).get_figure().savefig('output7.png', bbox_inches = 'tight')


