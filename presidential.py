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

occ_mapping = {
	'INFORMATION REQUESTED PER BEST EFFORTS': 'NOT PROVIDED',
	'INFORMATION REQUESTED': 'NOT PROVIDED',
	'INFORMATION REQUESTED (BEST EFFORTS)': 'NOT PROVIDED',
	'C.E.O.': 'CEO'}

# If no mapping provided, return x:
f = lambda x: occ_mapping.get(x, x)
fec.contbr_occupation = fec.contbr_occupation.map(f)

emp_mapping = {
	'INFORMATION REQUESTED PER BEST EFFORTS': 'NOT PROVIDED',
	'INFORMATION REQUESTED': 'NOT PROVIDED',
	'SELF': 'SELF-EMPLOYED',
	'SELF EMPLOYED': 'SELF-EMPLOYED'}
f = lambda x: occ_mapping.get(x, x)
fec.contbr_employer = fec.contbr_employer.map(f)

print fec.contbr_occupation.value_counts()[:10]

by_occupation = fec.pivot_table('contb_receipt_amt', index = 'contbr_occupation', columns = 'party', aggfunc = 'sum')
print by_occupation

print by_occupation.ix
by_occupation_veteran = by_occupation[by_occupation.index.map(lambda x: 'VETERAN' in x)]
print by_occupation_veteran

above2m = by_occupation[by_occupation.sum(1) > 2000000]
print above2m

