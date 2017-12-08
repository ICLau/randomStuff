# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 23:07:29 2017

@author: Isaac
"""
import numpy as np
import pandas as pd

# =============================================================================
# left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
# right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
# merged = pd.merge(left, right, on='key')
# print(left,'\n')
# print(right,'\n')
# print (merged)
# 
# print ('-'*80)
# 
# left1 = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
# right1 = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
# merged1 = pd.merge(left1, right1, on='key')
# print(left1,'\n')
# print(right1,'\n')
# print (merged1)
# 
# =============================================================================

# random testing..Pythagorean triples
p = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]


key1 = ['amy','beth','charles','dennis','emily']
value1 = [3, 4, np.NaN, 6, 7]

key2   = ['amy', 'charles', 'frank', 'beth', 'google', 'heather', 'tommy']
value2 = [1001,  101,       102,     1036,   104,      1405,      106]

f = lambda x: -111 if(x is np.nan(float(x))) else x   # I think the namespace messed things up and it won't work
a = value1.copy()  # make a copy of the list to play with... assignment operator will just be "reference"
b = list(map((lambda x: (0) if x is np.nan or x!=x else x), value1))
c = list(map((lambda x: (0) if x is np.nan or x!=x else x), value2))


# =============================================================================
# # creates a DataFrame, turn it into an iterable (i.e. list), then add a custom index to it
# # merge won't work with multi-level keys as index
# df1 = pd.concat([pd.DataFrame(value1, index=key1, columns=['meValue' ])], keys=['v1'])
# df2 = pd.concat([pd.DataFrame(value2, index=key2, columns=['valueMe2'])], keys=['v2'])
# merged = pd.merge(df1, df2, how='outer', left_index=True, right_index=True, indicator=True )
# #result = pd.concat([merged], keys=['v1','v2'])
# =============================================================================
# create a DataFrame and set cols & colTitle with default indices
df3 = pd.DataFrame({'myKey': key1,
                    'myValue': value1})



df1 = pd.DataFrame(value1, index=key1, columns=['v1'])
df2 = pd.DataFrame(value2, index=key2, columns=['v2'])
dfMerged = pd.merge(df1, df2, how='outer', left_index=True, right_index=True, indicator=True)
dfMerged2 = pd.merge (pd.DataFrame(b, index=key1, columns=['vv1']), 
                      pd.DataFrame(c, index=key2, columns=['vv2']),
                      how='outer',
                      left_index=True,
                      right_index=True)
## The following won't work because of the "indicator" column being a "category" col
#dfMerged.fillna(0, inplace=True)

dfMerged2.fillna(-222, inplace=True)

#df1 = pd.DataFrame (key1, columns=['name']) # initialize with ONE col
#df1['myValue'] = value1                     # just append a Col


#df2.columns = ['myValue2']
#df2.sort_values()

# Test reference implications when doing assignment...
df3.iloc[2,0] = 'nobody zzz...'     # this works
df3.loc[3,('myValue')] = 100        # this seems to work too