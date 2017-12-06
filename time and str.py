import pandas as pd
from datetime import datetime as dt

def convToDateTimeObj (strDateT):
    return dt.strptime (strDateT, '%Y-%m-%d %H:%M:%S')

strDateTime = '2017-10-19 11:24:40'
oDateTime = dt.strptime (strDateTime, '%Y-%m-%d %H:%M:%S')
print ('strDateTime = \'', strDateTime, '\'')
print ('oDateTime = ', oDateTime)


userName = 'User: Zihurain Jaigirdar, card: Zihurain Jaigrdar'
print (userName)
print ('find \'user:\'', userName.find ('user:'))
print ('find \'User:\'', userName.find ('User:'))

strPrefix = 'User: '
strSuffix = ', card:'
strNewName = userName[userName.find(strPrefix)+len(strPrefix) : 
                            userName.find(strSuffix)]

strFormattedNewName = '\'' + strNewName + '\''    
print ('extracted name:', strFormattedNewName)


strDates = ['2017-10-19 10:19:10', '2018-01-22 01:22:01', '2019-07-11 07:11:07']
### oDates = dt.strptime (strDates, '%Y-%m-%d %H:%M:%S')

DateObj = []

for eachDate in strDates :
    DateObj.append (convToDateTimeObj (eachDate))
    print ('len (DateObj =)', len(DateObj))
    print ('   DateObj list contains:')
    print (DateObj)


# using this syntax seems to add the cols in reversed order listed here
df_DT = pd.DataFrame ({'strDates' : strDates,
                       'ObjDates' : DateObj})    
    
df_DT2 = pd.DataFrame ({'strDates' : strDates})
df_DT2 ['ObjDates'] = DateObj

