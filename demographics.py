import pandas as pd
import matplotlib.pylab as plt

data = pd.read_csv('DEMOGRAPHICS.csv')

data = data[data['Poverty'] >= 0]

# Mean poverty in state
poverty_state = data.groupby(['CHSI_State_Name'])['Poverty'].mean().reset_index()

# Mean white people in state
white_state = data.groupby(['CHSI_State_Name'])['White'].mean().reset_index()

# Mean black people in state
black_state = data.groupby(['CHSI_State_Name'])['Black'].mean().reset_index()

# Mean native American in state
native_state = data.groupby(['CHSI_State_Name'])['Native_American'].mean().reset_index()

# Mean Asian in states
asian_state = data.groupby(['CHSI_State_Name'])['Asian'].mean().reset_index()

# Mean Hispanic in states
hispanic_state = data.groupby(['CHSI_State_Name'])['Hispanic'].mean().reset_index()

poverty = pd.merge(poverty_state, white_state).merge(black_state).merge(native_state).merge(asian_state).merge(hispanic_state)
poverty = poverty.set_index('CHSI_State_Name')

print poverty

fig, ax = plt.subplots()

poverty.plot(ax = ax, figsize = (16, 10), alpha = 0.7, label = '', legend = True, linewidth = 2, title = 'Poverty and ethnicity in the USA')
ax.set_xticklabels(poverty.index, rotation = 90)
ax.set_xticks(range(len(poverty.index)))

ax.set_title(ax.get_title(), fontsize = 26, alpha = 0.7, ha='left')
plt.subplots_adjust(top=0.9)
plt.subplots_adjust(bottom=0.25)
ax.title.set_position((0.2, 1.04))

#locs, labels = plt.xticks()
#plt.setp(labels, rotation=90)

# Remove grid lines (dotted lines inside plot)
ax.grid(False)
# Remove plot frame
ax.set_frame_on(False)

ax.lines[0].set_linewidth(4)

ax.yaxis.set_ticks_position('none')
ax.xaxis.set_ticks_position('none')

ax.tick_params(axis='x', which='major', pad = 20)

ax.set_xlabel('State')

fig.savefig('output7.png', aspect=0.6)#, xbbox_inches = 'tight')

