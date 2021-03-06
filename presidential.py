# http://www.fec.gov/disclosurep/PDownload.do
# Using the all file from above.
# P00000001-ALL.zip -> P00000001-ALL.csv

import pandas as pd

states = pd.read_csv('state_table.csv', usecols = ['name', 'abbreviation'])

fec = pd.read_csv('P00000001-ALL.csv', index_col = False)
#fec = pd.read_csv('P00000001-ALL.cleansed.csv')
#fec = pd.read_csv('../pydata-book/ch09/P00000001-ALL.csv')
fec.info()

fec = pd.merge(fec, states, left_on = 'contbr_st', right_on = 'abbreviation')

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

by_occupation_teacher = by_occupation[by_occupation.index.map(lambda x: 'TEACHER' in x)]
print by_occupation_teacher
print by_occupation_teacher.sum()
print 'XXXXXXXXXXXXXXXXXXXXX'

by_occupation_it_manager = by_occupation[by_occupation.index.map(lambda x: 'IT' in x and 'MANAGER' in x)]
print by_occupation_it_manager

print by_occupation[by_occupation.index.map(lambda x: 'POLICE' in x)]

print by_occupation[by_occupation.index.map(lambda x: 'SOLDIER' in x)]

above2m = by_occupation[by_occupation.sum(1) > 2000000]
print above2m

def get_top_amounts(group, key, n=5):
	totals = group.groupby(key)['contb_receipt_amt'].sum()
	return totals.order(ascending=False)[:n]

grouped = fec.groupby('cand_nm')
print grouped.apply(get_top_amounts, 'contbr_occupation', n=7)
print grouped.apply(get_top_amounts, 'contbr_employer', n=10)

# Slow
# grouped = fec.groupby('contbr_employer')
# print grouped.apply(get_top_amounts, 'cand_nm', n=10).order(ascending=False)[:20]

print fec.pivot_table('contb_receipt_amt', index = 'contbr_employer', columns = 'party', aggfunc = 'sum', fill_value = 0).sort(['Democrat'])

pivot_by_st = fec.pivot_table('contb_receipt_amt', index = 'contbr_st', columns = 'party', aggfunc = 'sum', fill_value = 0)
print pivot_by_st.sort(['Republican'])
print pivot_by_st.sort(['Democrat'])
print pivot_by_st[pivot_by_st.index.map(lambda x: x == 'NH')]
print pivot_by_st[pivot_by_st.index == 'NH'] # Shorter, still works.

pivot_by_st['difference'] = abs(pivot_by_st['Republican'] - pivot_by_st['Democrat'])
print pivot_by_st.sort(['difference'])

by_contbr_name = fec.pivot_table('contb_receipt_amt', index = 'contbr_nm', columns = 'party', aggfunc = 'sum')
by_contbr_name_hassan = by_contbr_name[by_contbr_name.index.map(lambda x: 'HASSAN' in x)]
print by_contbr_name_hassan

by_contbr_name_patel = by_contbr_name[by_contbr_name.index.map(lambda x: 'PATEL' in x)]
print by_contbr_name_patel.sum()

print by_contbr_name[by_contbr_name.index.map(lambda x: 'RIVERA' in x)]
print by_contbr_name[by_contbr_name.index.map(lambda x: 'RIVERA' in x)].sum()
print by_contbr_name[by_contbr_name.index.map(lambda x: 'RIVERA' in x)].count()

print fec.sort(['contb_receipt_amt'])[:2]
