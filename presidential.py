# http://www.fec.gov/disclosurep/PDownload.do
# Using the all file from above.
# P00000001-ALL.zip -> P00000001-ALL.csv

import pandas as pd

fec = pd.read_csv('P00000001-ALL.cleansed.csv', index_col = False)
#fec = pd.read_csv('P00000001-ALL.cleansed.csv')
#fec = pd.read_csv('../pydata-book/ch09/P00000001-ALL.csv')
fec.info()
print fec.ix[123456]
unique_cands = fec.cand_nm.unique()
print unique_cands

parties = {'Rubio, Marco': 'Republican',
	'Santorum, Richard J.': 'Republican',
	'Perry, James R. (Rick)': 'Republican',
	'Carson, Benjamin S.': 'Republican',
	"Cruz, Rafael Edward 'Ted'": 'Republican',
	'Paul, Rand': 'Republican',
	'Clinton, Hillary Rodham': 'Democrat',
	'Sanders, Bernard': 'Democrat',
	'Fiorina, Carly': 'Republican',
	'Huckabee, Mike': 'Republican',
	'Pataki, George E.': 'Republican',
	"O'Malley, Martin Joseph": 'Democrat',
	'Graham, Lindsey O.': 'Republican',
	'Bush, Jeb': 'Republican',
	'Jindal, Bobby': 'Republican'}

fec['party'] = fec.cand_nm.map(parties)

print fec['party'].value_counts()

# Ignore negative contirbution amount.
fec = fec[fec.contb_receipt_amt > 0]

