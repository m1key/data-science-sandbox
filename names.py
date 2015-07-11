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

print np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1)

def get_top1000(group):
	return group.sort_index(by = 'births', ascending = False)[:1000]
grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
top1000.index = np.arange(len(top1000))

print top1000

