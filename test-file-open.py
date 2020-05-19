from contextlib import contextmanager

@contextmanager
def open_file (file, mode):
  try:
    g = open(file, mode)
    yield g
  finally:
    g.close()

with open_file('sample.txt', 'w') as f:
  f.write ('lorem ipsum')
  f.write ('\n')
  f.write ('line 2')

print (f.closed)

# using contextmanager to switch directories
import os

print(2*'\n')
@contextmanager
def change_dir(destination):
  try:
    # save the current working dir, so we can restore it at teardown
    cwd = os.getcwd()
    os.chdir(destination)
    yield
  finally:
    os.chdir(cwd)

with change_dir('.'):
  print ('list of files in current dir')
  # print(os.listdir())
  for fname in os.listdir():
    print (fname)

with change_dir('.git'):
  print ('\nList of files in .git dir')
  for fname in os.listdir():
    print (fname)