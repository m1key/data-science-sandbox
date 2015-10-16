import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Abortion_Demographics__1995-2012.csv')
data = data[data['YEAR'].str.contains("Age")]
data.set_index('YEAR')

fig, ax = plt.subplots()

data.pivot_table(columns = 'YEAR').plot(ax = ax)

handles, labels = ax.get_legend_handles_labels()
lgd = ax.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5,-0.1))
ax.grid('on')

fig.savefig('output9.png', bbox_extra_artists=(lgd,), bbox_inches = 'tight')
