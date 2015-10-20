import pandas as pd

def p2f(x):
	return 0 if x == "" else float(x.strip('%'))

rel = pd.read_csv('religions.csv', converters={'Other/UnSpecified': p2f, 'None': p2f})
rel.fillna(0)
rel['Non-religious'] = rel['Other/UnSpecified'] + rel['None']

def printNonReligious(country):
	print rel[rel['Country'].str.contains(country, na = False)][['Country', 'Other/UnSpecified', 'None', 'Non-religious']]

printNonReligious('Poland')
printNonReligious('United Kingdom')
printNonReligious('Netherlands')

