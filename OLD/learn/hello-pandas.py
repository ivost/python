#
# http://pandas.pydata.org/pandas-docs/stable/10min.html
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
#print s

dates = pd.date_range('20160917', periods=6)
#print dates

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print df

df2 = pd.DataFrame({ 'A' : 1.,
    'B' : pd.Timestamp('20130102'),
    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
    'D' : np.array([3] * 4,dtype='int32'),
    'E' : pd.Categorical(["test","train","test","train"]),
    'F' : 'foo' })
#print df2
#%%
df.index
df.columns
df.values
#%%
df.describe()
#%%

# transpose
df.T

#df.sort_index(axis=1, ascending=False)        
df.sort_values(by='A')        
