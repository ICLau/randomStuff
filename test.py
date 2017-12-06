#matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

def printSeparationLine ():
    print ('*' * 80)
    

def writeRec (dttm, user, action):
    # Need to check if the record already exists...
    sqlStatement = str.format("SELECT datestamp, user FROM AccessLog WHERE datestamp = '{0}' AND user = '{1}'", dttm, user)
#    print ('sqlStatement =', sqlStatement)
    dbCur.execute (sqlStatement)

#    data = dbCur.fetchall()
#    print ('data =', data)
#    if (not data):
    rowWritten = 0
    if (len(dbCur.fetchall()) <= 0):
#        print ('*', dttm, user, action)
        dbCur.execute ("INSERT INTO AccessLog (datestamp, user, action) VALUES (?, ?, ?) ",
                   (dttm, user, action))
        conn.commit()
        rowWritten = 1
#    else:
#        print ('*** data already exists in db -- skipped (not added)')

    return rowWritten


logFile = 'BasicEventReport.csv'
delim = ','
df = pd.read_csv(logFile, delimiter = delim)

#print ('top 10 rows')
#print (df.head(10))

#printSeparationLine()
#print ('bottom 10 rows')
#print(df.tail (10))

#printSeparationLine()
#print (df.describe ())

#printSeparationLine()
#print (df.shape) # dimension of the table

#fetch the column names
cols = df.columns

#create a new table with less columns
#we are only interested in columns 5,6,7
df2 = df [[cols[5], cols[6], cols[7]]]

#printSeparationLine()
#print ('new table shape: ', df2.shape)

fltrBadgedIn = 'Access Granted'
fltrBadgeOut = 'Exit Granted'
df3 = df2[df2[cols[7]].isin([fltrBadgedIn, fltrBadgeOut])]

#printSeparationLine()
#print ('filtered dimension: ', df3.shape)
#
#
#print ('df3.column[0].head() is: ')
#print ( df3[df3.columns[0]].head(10))   # list out first 10 elements of this column (DateTime)
#print ( df3[df3.columns[0]][3:6])       # list elements index 3 to, but not including 6

# rename columns
newCols = ['DateTime', 'User', 'Action']
df3.columns = newCols
#print ('New df3 column names:')
#print (df3.columns)


"""
# next test: convert a Unix date/time string into Datetime object
"""

"""
Extract and shorten the name
DON'T do this more than ONCE...
"""
strPrefix = 'User: '
strSuffix = ', card:'

df3[df3.columns[1]] = df3[df3.columns[1]].map ( lambda x: x[x.find(strPrefix)+len(strPrefix) : x.find(strSuffix)] )
print (df3[df3.columns[1]].head())    
#strNewName = userName[userName.find(strPrefix)+len(strPrefix) : 
#                            userName.find(strSuffix)]

"""
# use SQLite3 to 
## create a db table
## writes to it
## read back into a new DataFrame
"""
doorDB = 'DoorAccess.db'

"""
## Opens the named db & obtains the db cursor
"""    
conn = sqlite3.connect (doorDB)
dbCur = conn.cursor()


"""
# opens the table - create if not exists
"""
dbCur.execute ("CREATE TABLE IF NOT EXISTS AccessLog (datestamp TEXT, user TEXT, action TEXT, PRIMARY KEY (user, datestamp))")

"""
# write them out to our own db!
"""
print ('Writing recs to db...')
rowsWritten = 0
maxRow = len (df3)
for i in range(maxRow):
    rowsWritten += writeRec (df3.iloc[i][0], 
              df3.iloc[i][1],
              df3.iloc[i][2])

print ('Finished writing to db!')
print ('===> rows written/rows in CSV:', rowsWritten, '/', maxRow)




"""
# close cursor and connection
"""
dbCur.close()
conn.close()

