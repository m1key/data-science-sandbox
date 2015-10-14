import pandas as pd
import matplotlib.pylab as plt

def p2f(x):
    return float(x.strip('%'))

data = pd.read_csv('Smoking_Prevalence_in_Adults__1984-2013.csv', converters={'Percentage of  Current Smokers':p2f})

data.pivot_table('Percentage of  Current Smokers', index = 'Year', columns = 'Gender').plot().get_figure().savefig('output8.png', bbox_inches = 'tight')
