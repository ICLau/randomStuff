###
### ref URL: https://docs.python.org/3/library/collections.html#collections.OrderedDict
### new in v3.1
### OrderedDict is NOT available by default, it needs to be imported from collections
###
### Very strange, it does NOT work.
### The OrderedDict does NOT keep the insertion order
### in the LRUCache.__setitem__() method, the 'oldest' we got is NOT the FIFO from the
### left of the OrderedDict
#################################################################
from collections import OrderedDict

class LRUCache (OrderedDict):
  'Limit size, evicting the least recently looked-up key when full'

  def __init__ (self, maxsize=10, /, *args, **kwds):
    super().__init__(*args, **kwds)
    self.maxsize = maxsize

  def __getitem__ (self, key):
    value = super().__getitem__(key)
    # what if key does not exist?? then we get None back
    # and what will self.move_to_end(None) do??
    self.move_to_end (key)
    return value

  def __setitem__ (self, key, value):
    super().__setitem__(key, value)
    if len(self) > self.maxsize:
      print (f'iter(self): {list(iter(self))}')
      oldest = next(iter(self))
      del self[oldest]
      # k, v = self.popitem(last=False)
      # print (f'removing key:{k}, value:{v}')



#################################################################
### Test codes

def _main_ ():
  myLRUCache = LRUCache(5)
  print (f'myLRUCache size ={len(myLRUCache)}')
  print (myLRUCache)

  myLRUCache['key8'] = 'value8'
  myLRUCache['key1'] = 'value1'
  myLRUCache['key12'] = 'value12' 
  myLRUCache['key2'] = 'value2'

  myLRUCache['key3'] = 'value3'
  myLRUCache['key4'] = 'value4'
  myLRUCache['key10'] = 'value10'
  myLRUCache['key5'] = 'value5'
  myLRUCache['key11'] = 'value11' 
  myLRUCache['key6'] = 'value6'
  myLRUCache['key7'] = 'value7'
  myLRUCache['key9'] = 'value9'

  for k,v in list(myLRUCache.items()):
    print (f'key = {k}, value={v}')


#################################################################
if __name__ == "__main__":
  _main_()


