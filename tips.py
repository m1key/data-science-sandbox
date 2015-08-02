import pandas as pd

tips = pd.read_csv('tips.csv')

tips['tip_pct'] = tips['tip'] / tips['total_bill']

grouped = tips.groupby(['sex', 'smoker'])
grouped_pct = grouped['tip_pct']
print grouped_pct.agg('mean') # == print grouped_pct.mean()
print grouped_pct.agg(['mean', 'std'])

