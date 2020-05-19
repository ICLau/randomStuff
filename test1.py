
# a = [1,2,3,4,5,1,6,5]

# repeat = {}

# for n in a:
#   if (n in repeat):
#     repeat[n] += 1
#   else:
#     repeat[n] = 1

# print (repeat)

# switch (op) {
#   case Operations.ADD:
#     #do ADD operations
#     break;

#   case Operations.SUBTRACT:
#     #do subtract operations
#     break;

# }

'''
class Operations(Enum):
    ADD = 0
    SUBTRACT = 1
    SET = 2
    ROUND_TO_CLOSEST_MULTIPLE_OF_FIVE = 3
    REPEAT_LAST_OPERATION = 4

class Calculator:
    def __init__(self):
        self.total = 0
        self.lastOP = None

    def performOperation(self, op, value):
        # Write your code here
        if op != Operations.REPEAT_LAST_OPERATION:
            self.lastOP = op
        
        if op == Operations.ADD:   
            self.total =  self.total + value;
        elif op == Operations.SUBTRACT:
            self.total -= value;
        elif op == Operations.SET:  
            self.total = value;
        elif op == Operations.ROUND_TO_CLOSEST_MULTIPLE_OF_FIVE:  
            self.total = 5 * round(value/5);
        elif op == Operations.REPEAT_LAST_OPERATION:
            self.performOperation(self.lastOP, value);        
        return self.total

'''
###
### extracting & assigning to vars from tuple
###
# tuples = tuple ([1,2,3,4])
# print (tuples)

## extract individual elements into separate vars
## # of vars MUST match # of elements in tuple
# a,b,c,d = tuples

## or we can only unpack a,b and throw the rest into dontCare
# a,b, *dontCare = tuples

## or we can extract the 1st AND last elements from the tuple
# a, *dontCare, b = tuples

# print (f'len of tuples={len(tuples)}, a={a}, b={b}')

# def result (x, y):
#   return x*y

# print (result (10, 100))
# z = (9, 20)
# print (*z)
# print (result(*z))

'''
###
### comparing tuples
###
tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida')
tup2 = (1,2,3,4,5,6,7)
tup3 = (1,2,3)
print(tup1[0])
print(tup2[1:4])

if (tup2 > tup3):
  print ('tup2 is > tup3')
else:
  print ('tup2 is < tup3')
'''

'''
###
### composite key for dict
###
first = "Robert"
last = "Gayle"
number = "123-4567"
directory = {}
directory[last, first] = number
print (directory)

first = 'Peter'
last = 'Adam'
number = '222-2222'
directory[last, first] = number
print (directory)

first = 'Jeff'
last = 'Boyd'
number = '333-3333'
directory[last, first] = number
print (directory)

print (directory['Adam', 'Peter'])

b = list (directory.items())
print (b)

b = list(directory.keys())
print (b)
for item in b:
  print (f'Lastname: {item[0]}, Firstname: {item[1]}')
'''

###
### namedtuple
###
from collections import namedtuple
Features = namedtuple('myFeatures', ['age', 'gender', 'name'])
print (Features)
row = Features(age=22, gender='male', name='Alex')
row = Features(age=18, gender='female', name='Betty')
row = Features(age=55, gender='male', name='Charles')
print (f'\nFeatures:', Features)
print(row.age)

###
EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "r"))):
    print(emp.name, emp.title, emp.age, emp.paygrade)

### Below is the same as the above [very compacted] code
###
csvFile = open ('employees.csv', 'rt')
dataReaderIter = csv.reader(csvFile)
print (2*'\n')
# for line in dataReaderIter:
#     print (line)
myMappedData = map(EmployeeRecord._make, dataReaderIter)
for item in myMappedData:
    print (item)
    print (item.name, item.age, item.title, item.department, item.paygrade)

csvFile.close()

###
### collections.Counter
###
from collections import Counter
ages = [22, 22, 25, 25, 30, 24, 26, 24, 35, 45, 52, 22, 22, 22, 25, 16, 11, 15, 40, 30]
value_counts = Counter(ages)
print(value_counts.most_common(4))  # the most 4 common (highest count) elements
print(value_counts.most_common())   # all elements sorted by count
n = 4   # the nth's least common elements
print(value_counts.most_common()[:-n-1:-1])
print(value_counts.most_common()[-1::-1])   # returns the reversed of most_common()