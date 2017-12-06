import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import HourLocator
from matplotlib.dates import date2num

df = pd.DataFrame(data=dict(a=pd.date_range('1/1/2011',periods=1440000,freq='1min')))
print (df.head())
print (df.tail())
print ('size =', len(df))
print ('*'*15)
#df = df.iloc[np.arange(0,1440*100,1440)+np.random.randint(1,300,100)]
df = df.iloc[np.arange(0,1440*10,1440)+np.random.randint(1,300,10)]

print (df.head())
print (df.tail())
print ('size =', len(df))
print ('*'*15)



# =============================================================================
# plt.plot(df.index,df['a'].dt.time)
# plt.show()
# =============================================================================


fruits = ['coconut','banana','kiwi','apple','tangerine','fire dragen fruit','durian','orange','jack fruit','papaya']

y = df['a'].apply(lambda x: x.replace(year=2000, month=12, day=30)).tolist()
x = np.arange(len(y))
print (y)
print ('size =', len(y))
print ('*'*15)

ax = plt.subplot()
print('~')
###ax.plot(df.index, y)
ax.plot(x, y, marker='o', linestyle='', markersize=10)
#ax.bar(x, date2num(y), 0,6)
#ax.bar (x, y, 0.6)
print('~'*2)

#This must be called before the locator/formatter
ax.yaxis_date()

ax.yaxis.set_major_locator(HourLocator())
print('~'*3)
ax.yaxis.set_major_formatter(DateFormatter('%H:%M'))
print('~'*4)


plt.xticks(x,fruits)
for xTickLabel in ax.xaxis.get_ticklabels():
    xTickLabel.set_rotation (75)
plt.show()