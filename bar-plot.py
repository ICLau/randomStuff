# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 21:46:51 2017

@author: Isaac
"""
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import time as tm
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from matplotlib.dates import HourLocator

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        print('h=',height)
        ax.text(rect.get_x() + rect.get_width()/2., 
                1.03*height,
                '%d' % int(height),
                ha='center', 
                va='bottom',
                rotation='vertical')


x  = ['Tommy',  'Alice', 'Henry',   'Jennifer', 'Bobby',   'IBM',    'Google',  'BlockChain']
y  = [tm(8,33), np.NaN,  tm(9,15),  np.NaN,     tm(8,55),  tm(9,33), tm(10,10), np.NaN]
y2 = [np.NaN,   np.NaN,  tm(17,15), tm(16,55),  tm(17,45), np.NaN,   tm(16,22), tm(18,1)]

# find a better way to replace NaN from list object
y = [labmda x: ]

myDay = datetime.date (2017,1,1)
yDt = [datetime.datetime.combine(myDay, t) for t in y]
y2Dt = [datetime.datetime.combine(myDay, t) for t in y2]

# try matplotlib "numeric" dates
ymDt = [mdates.date2num(d) for d in yDt]
y2mDt = [mdates.date2num(d) for d in y2Dt]

N = len(x)
ind = np.arange(N)  # the x locations for the groups
width = 0.15        # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar (ind, ymDt, width, color='r', label="Time In")
rects2 = ax.bar (ind + width, y2mDt, width, color='b', label="Time Out")

# add some text for labels, title and axes ticks
ax.set_ylabel('Time')
ax.set_title('Median Time In & Out')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(x)
for xTickLabel in ax.xaxis.get_ticklabels():
    xTickLabel.set_rotation (75)

ax.legend()
#This must be called before the locator/formatter
ax.yaxis_date()
ax.yaxis.set_major_locator(HourLocator())
ax.yaxis.set_major_formatter(DateFormatter('%H:%M'))


#autolabel(rects1)
#autolabel(rects2)

minYTime = datetime.datetime.combine (myDay, tm(0,0,0))
maxYTime = datetime.datetime.combine (myDay, tm(23,59))
plt.ylim (minYTime, maxYTime)

myYTicks = []
yTickHrApart = 2
for eachTick in range(int(24/yTickHrApart)):
      myYTicks.append(datetime.datetime.combine(myDay,tm(eachTick*yTickHrApart,0,0)))
myYTicks.append(datetime.datetime.combine(myDay,tm(23,59)))
plt.yticks (myYTicks)


plt.subplots_adjust (top=0.926,
                     bottom=0.167,
                     left=0.131,
                     right=0.971,
                     hspace=0.2,
                     wspace=0.2)
plt.show()