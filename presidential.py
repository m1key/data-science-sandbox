# http://www.fec.gov/disclosurep/PDownload.do
# Using the all file from above.
# P00000001-ALL.zip -> P00000001-ALL.csv

import pandas as pd

fec = pd.read_csv('P00000001-ALL.cleansed.csv')
#fec = pd.read_csv('../pydata-book/ch09/P00000001-ALL.csv')
fec.info()
print fec.ix[123456]
unique_cands = fec.cand_nm.unique()
print unique_cands

