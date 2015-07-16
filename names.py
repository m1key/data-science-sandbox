import pandas as pd
import numpy as np

years = range(1880, 2015)

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
subset = total_births[['Michael', 'Mike', 'Michal', 'Denis', 'Dennis', 'Martin', 'Ammar', 'Aymar', 'Kartik', 'Karthik']].fillna(0)
subset.plot(title = 'Number of births per year, USA, logarithmic', grid = True, figsize=(28,20), xticks=range(1880, 2020, 5), logy = True).get_figure().savefig('output2.png', bbox_inches = 'tight')

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
