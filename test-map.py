'''
 Test map function
'''

def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')  # for new line

def directPassThru (a, b):
  return a, b


# print ('Test map funtion')
# list_num = [1,2,3,4]
# tuple_num = (5,6,7,8)
# set_num = {5,6,7,8}

# print ('dpt', directPassThru(1,4))

# mapIter1 = map(lambda x: x**2,list_num)
# print ('mapIter1: ')
# print_iterator(mapIter1)

# # taking in 2 iterables and returning 2 items in each round
# mapIter2 = map(lambda x,y: directPassThru(x,y*2) , list_num, tuple_num)
# print ('mapIter2')
# print_iterator(mapIter2)

# mapIter3 = map(lambda x,y: directPassThru(x,y*2) , list_num, set_num)
# print ('mapIter3')
# print_iterator(mapIter3)

set2 = {1,3,'apple',5,7,2,4,6,8,1,1,'apple'}
print ('set2: ', set2)

import json

dictTest = {
  "john": 20,
  'peter': 2,
  'mary': 56
}

print ('dictTest: ', dictTest, '\n')

jsonTest = json.dumps(dictTest)
print('jsonTest: ', jsonTest, '\n')