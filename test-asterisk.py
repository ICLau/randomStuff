#
# https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/
#


"""
what = [1,2,3,4,5]
print (f'*what:', *what)
print (f'what:', what)

lol = [[1,4,7,11], [2,5,8,], [3,6,9,]]
ziplol = zip(*lol)
print (f'lol: {lol}')
print (f'*lol:->', *lol)
print (f'ziplol: {ziplol}')
for i in ziplol:
  print (f'i={i}')

ziplol2 = zip(lol)
print (f'ziplol2: {ziplol2}')
for i in ziplol2:
  print (f'i2={i}')

"""

###
# resequence collection using "*" unpacking
# - moves the first element in the collection to the end
###
fruits = ["pears", "apples", "oranges", "bananas", "strawberries"]
"""
first_fruit, *rest = fruits
rearranged_tuple = *rest, first_fruit
rearranged_list = [*rest, first_fruit]

print (f'fruits: ', fruits)
print (f'first_fruit: ', first_fruit)
print (f'rest: ', rest)
print (f'*rest: ', *rest)
print (f'rearranged_tuple: ', rearranged_tuple)
print (f'rearranged_list: ', rearranged_list)

# rotate 1st element to the end
rotated_fruits = [*fruits[1:], fruits[0]]
print (f'rotated_fruits: ', rotated_fruits)
"""

###
# a function to reverse the argument list passed in
###
def show_reversed(*args):
  print(*args[::-1])

show_reversed(1,2,3)
show_reversed(*fruits)