#!C:/Users/barraud/AppData/Local/Programs/Python/Python35/python.exe
import os

# get the currently logged in user for this computer
print(os.getlogin())

# os.path has some very useful functions like
# check if file exists
# notice above also the use of r (raw string)
print(os.path.isfile(r"C:\Users\barraud\Documents\work\python\pylets\multi-line.py.log"))
