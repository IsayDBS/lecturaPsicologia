import pandas as pd

df = pd.read_excel('../files/13428_2015_684_MOESM1_ESM.xlsx')
new_dict = df.to_dict()
print(df.columns)
#print(df.dtypes)
'''
Los strings los cuenta como  object
enteros son int64
flotantes son float64
'''