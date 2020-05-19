###
### https://www.youtube.com/watch?v=FsAPt_9Bf3U&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=37
###
### Adds a timer decorator
###

def myTimer (original_func):
  import time

  def wrapper (*args, **kwargs):
    # t1 = time.time()
    t1 = time.perf_counter()
    result = original_func(*args, **kwargs)
    # t2 = time.time()
    t2 = time.perf_counter()
    print (f'{original_func.__name__}{args}{kwargs} - ran in {(t2-t1)} sec')
    # print (f'{original_func.__name__} - ran in {(t2-t1)} sec', *args, kwargs)
    return result

  return wrapper

#------------------------------------------
import time

@myTimer  # same as replacing the line after @@@ below with: myDisplay = myTimer(myDisplay)
def myDisplay (username, age, name):
  time.sleep(1)
  print (f'Username is {username}, and his/her age is: {age}, name is {name}')

# @@@
myDisplay ('Andy', 30, name='Coco')
print()
myDisplay ('Bobby', 60, "noName")
print()

# we can use the same decorator to decorate another function
import math
@myTimer
def createList (numElements):
  result = []
  for i in range(1,numElements):
    result.append(math.pow(i,2))

  return result

myList = createList(3000000)
