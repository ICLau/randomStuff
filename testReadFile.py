'''
Test reading text file
content structure:
FirstName, LastName, email, salary
- CSV
'''

import csv

peopleList = []
peopleDict = {}

'''
with open('testReadFile.txt', 'r') as inFile:
  # csv_data = csv.DictReader(inFile)   # this reader breaks up the "salary" field into multiple non-key fields with comma
                                      # and is not trimming the header field text
  # csv_data = csv.reader(inFile)

  fieldNames = [colName.strip() for colName in inFile.readline().split(',')]
  print (f'fieldNames: {fieldNames}')

  csv_data = csv.DictReader (inFile, fieldnames=fieldNames)

  for line in csv_data:
    print (line)
    # print ('*{}*'.format(line['email'].strip()))
    # peopleList.append(line)
    peopleDict.clear()
    peopleDict[fieldNames[0]] = line[fieldNames[0]].strip()
    peopleDict[fieldNames[1]] = line[fieldNames[1]].strip()
    peopleDict[fieldNames[2]] = line[fieldNames[2]].strip()
    peopleDict[fieldNames[3]] = float(line[fieldNames[3]].strip())

    # print(peopleDict)
    peopleList.append(dict(peopleDict))

    

inFile.close()
print(f'There are {len(peopleList)} records read from file.')
for person in peopleList:
  print(person)
  print(' {} is: ${:.2f}'.format(fieldNames[3], person[fieldNames[3]]))
  print(f'*{fieldNames[3]} is: ${person[fieldNames[3]]:.2f}')

print (2*'\n')

print (f'30//7 is {30//7}')

print (f'divmod(30, 7) is {divmod(30,7)}')
d, m = divmod(30, 7)
print (f'd={d}, m={m}')

cNum = complex(4,-5)
print (f'cNum = {cNum}, its conjugate = {cNum.conjugate()}')

print (2*'\n')
'''

with open('testReadFile.txt','r') as inFile:
  # read header line
  colNames = [colName.strip() for colName in inFile.readline().split(',')]
  numCols = len(colNames)
  print (f'{numCols} columns, colNames: {colNames}')

  csv_data = csv.reader (inFile)
  for line in csv_data:
    print (line)
    peopleDict.clear()
    for i in range(numCols-1):
      peopleDict[colNames[i]] = line[i].strip()

    # get the salary
    peopleDict[colNames[numCols-1]] = float(line[numCols-1].strip())

    print (peopleDict)
    peopleList.append(dict(peopleDict))

  inFile.close()
  print (f'Final PeopleList has {len(peopleList)} elements.')
  for thisGuy in peopleList:
    # for each person dump out the details
    fullName = f'{thisGuy[colNames[1]]} {thisGuy[colNames[0]]}'
    print (f'FullName: {fullName}')
    print (f'**{colNames[2]}: {thisGuy[colNames[2]]}')
    print (f'**{colNames[3]}: ${thisGuy[colNames[3]]:.2f}')