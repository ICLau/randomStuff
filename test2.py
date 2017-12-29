# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 17:04:45 2017

@author: Isaac
"""

#uses test2.csv to plot a histogram

from datetime import datetime as dt
from datetime import time as tm
import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def timeSlot (timeObj):
    # given a time obj and assume we have 4 slots in an hour
    # returns the slot # (integer)
    return ( int (timeObj.minute/15) )

def grab_data (filename='test3.csv'):
    df = pd.read_csv(filename, delimiter = ',', parse_dates=True)
    
    return df

def timePart (strDateTime):
    tempDT = dt.strptime (strDateTime, '%Y-%m-%d %H:%M')
    return tm(tempDT.hour, tempDT.minute, tempDT.second)

# =============================================================================
def formatLabel (tSlot, sInOneHr):  # usually it is 4 slots in an hour (15min)
    tH = int(tSlot / sInOneHr)
    tM = int(tSlot % sInOneHr) * (int(60/sInOneHr))
    
    isAM = True
    if (tH == 12 and tM == 0):
        return "noon"
    elif tH > 12:
            tH -= 12
            isAM = False
    
    return "{0}:{1:02}{2}".format(tH, tM, "am" if isAM else "pm")
            
# =============================================================================


if (__name__ == '__main__'):
    df_raw = grab_data ('test2.csv')
    
    print (len(df_raw), df_raw.shape)
    
    username = df_raw.iat[0,1].strip()
    
    # just grab the times
    tIn  = df_raw[ df_raw['action'].isin(['Access Granted']) ]['datestamp']
    tOut = df_raw[ df_raw['action'].isin(['Exit Granted'  ]) ]['datestamp']
    
#    del dfIn["action"], dfOut["action"]

    # grabs the column labels into a list
    colNames = (df_raw.columns.values).tolist()
    
    # assigning the column labels is far easier... just assign a labelled list to dataframe's.columns

    # bucket the times into slots
    # one bucket for each hour in the day = 24 buckets
    # 4 slots in each bucket (i.e. 4x(15-min) slots per hour)
    newIn = list(map(timePart, tIn))
    df_raw['TimePart'] = list (map(timePart, df_raw['datestamp']))
    
    buckets = 24
    slotsPerBucket = 4 
    df_raw['Bucket'] = list(map(lambda h: h.hour, df_raw['TimePart']))
    df_raw['Slot'] = list(map(timeSlot, df_raw['TimePart']))
    
    t = df_raw['Bucket'] * slotsPerBucket + df_raw['Slot']
    df_raw['BucketSlot'] = df_raw['Bucket'] * slotsPerBucket + df_raw['Slot']
    
    tIn2  = df_raw[ df_raw['action'].isin(['Access Granted']) ]['BucketSlot']
    tOut2 = df_raw[ df_raw['action'].isin(['Exit Granted'  ]) ]['BucketSlot']

    tIn3 = (tIn2 - tIn2.mean()) / tIn2.std()
    tOut3 = (tOut2-tOut2.mean()) / tOut2.std()
    
    fig, ax = plt.subplots()
#    n, bins, patches = ax.hist(tIn2, buckets*slotsPerBucket, normed=1)
#    n, bins, patches = ax.hist(tIn2, buckets*slotsPerBucket)
    nIn , binsIn , patchesIn  = ax.hist(tIn2 , buckets*slotsPerBucket, label='In')
    nOut, binsOut, patchesOut = ax.hist(tOut2, buckets*slotsPerBucket, label='Out')

    #best fits
    myBinsIn = np.arange(20, 80, 30/96)
    
    # vCounts is used to "scale" up the npd curves
    vCounts = (tIn2.value_counts()).iat[0]
    if vCounts < (tOut2.value_counts()).iat[0]:
        vCounts = (tOut2.value_counts()).iat[0]
#    yIn = mlab.normpdf(binsIn, tIn2.mean(), tIn2.std())
#    ax.plot(binsIn, yIn*vCounts*10, '--')
    yIn = mlab.normpdf(myBinsIn, tIn2.mean(), tIn2.std())
    ax.plot(myBinsIn, yIn*vCounts*10, '--')
    
#    yOut = mlab.normpdf(binsOut, tOut2.mean(), tOut2.std())
#    ax.plot(binsOut, yOut*vCounts*10,'--')
    yOut = mlab.normpdf(myBinsIn, tOut2.mean(), tOut2.std())
    ax.plot(myBinsIn, yOut*vCounts*10,'--')



    xmin = 20
    xmax = 80
    xTickAt = 4
    numXTicks = int((xmax - xmin)/xTickAt) + 1
    plt.xlim (xmin, xmax)
    ind = np.arange(xmin,xmax+xTickAt,xTickAt )
#    xlabels = list( map(lambda l: "{0}:{1:02}".format(int(l/4), int(l%4)*15), ind) )
    # just to prove the point --> we can do this using map with 2 input args
    xiterSlots = [slotsPerBucket]*len(ind)
    xlabels = list( map(formatLabel, ind, xiterSlots) )
    ax.set_xticks(ind)
    ax.set_xticklabels(xlabels)
    for xTickLabel in ax.xaxis.get_ticklabels():
        xTickLabel.set_rotation (85)

    ax.legend()

    fig.tight_layout()
    plt.show()


# =============================================================================
#     # Create your DataFrame
#     products = pd.DataFrame({'category': ['Cleaning', 'Cleaning', 'Entertainment', 'Entertainment', 'Tech', 'Tech'],
#             'store': ['Walmart', 'Dia', 'Walmart', 'Fnac', 'Dia','Walmart'],
#             'price':[11.42, 23.50, 19.99, 15.95, 55.75, 111.55],
#             'testscore': [4, 3, 5, 7, 5, 8]})
#     
#     # Use `pivot()` to pivot the DataFrame
#     pivot_products = products.pivot(index='category', columns='store', values='price')
#     pivot_products2 = products.pivot(index='testscore', columns='store', values='price')
#     pivot_products3 = products.pivot(index='category', columns='store')
#     
#     # Check out the result
#     print(pivot_products)
# 
#     people = pd.DataFrame({'FirstName' : ['John', 'Jane'],
#                            'LastName' : ['Doe', 'Austen'],
#                            'BloodType' : ['A-', 'B+'],
#                            'Weight' : [90, 64]})
# 
#     for index, row in people.iterrows() :
#         print("index = {0}... row is:\n{1}".format(index, row))
# =============================================================================
