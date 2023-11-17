import os
path=input()
try:
   os.rmdir(path)
   print('Path is being removed')
except FileNotFoundError:
   print('cannot find the path')

