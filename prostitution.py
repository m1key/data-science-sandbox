import pandas as pd
import numpy as np

pro = pd.read_csv('prostitution.csv')
pop = pd.read_csv('population.csv')
# Comma issue:
gdp = pd.read_csv('ny.gdp.pcap.pp.cd_Indicator_en_csv_v2.csv', index_col = False)#, usecols = ['Country Name', '2014'])

mapping = {
	'Korea, Rep.': 'South Korea',
	'Taiwan, China': 'Taiwan'
}
f= lambda x: mapping.get(x, x)
#pop_recent.loc['Country Name'] = pop_recent.loc['Country Name'].map(f)
pop['Country Name'] = pop['Country Name'].map(f)
pop.loc[len(pop)] = ['Taiwan', 'TWN', 2014, 23461708]
pop_recent = pop[pop['Year'] == 2014]
# sk = pop_recent['Country Name']
#p_recent.loc[mask, 'Country Name'] = pop_recent.loc[mask, 'Country Name'].map(f)


gdp['Country Name'] = gdp['Country Name'].map(f)

gdp.ix[gdp['Country Name'] == 'Taiwan', '2014'] = 22083


data = pd.merge(pro, pop_recent, left_on = 'country', right_on = 'Country Name', how = 'left')
data = pd.merge(data, gdp, left_on = 'country', right_on = 'Country Name', how = 'left')

data.rename(columns = {'number': 'prostitutes', 'Value': 'population', '2014': 'GDP per capita 2014', '2013': 'GDP per capita 2013', '2012': 'GDP per capita 2012'}, inplace = True)

data['GDP per capita 2014'] = np.where(np.isnan(data['GDP per capita 2014']), data['GDP per capita 2013'], data['GDP per capita 2014'])

data['per100000'] = 10000 / (data['population'] / data['prostitutes'])

# Subset of columns:
print data[['country', 'population', 'per100000', 'GDP per capita 2014']].sort(['GDP per capita 2014'], ascending = False).reset_index(drop = True)

