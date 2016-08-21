#!c:/Users/barraud/AppData/Local/Programs/Python/Python35/python.exe

import re

# check if a string has a pattern
string = "val=123"
if re.search("\w+?=\d+?", string):
    print("found")

# use groups to get a value
match = re.search("\w+?=(\d+?)$", string)
if match:
    print(match.group(1))

# regex replace

subs = re.sub("\d+?$", "456", string)
print(subs)

# or use lambda in the repl. the arg is the group object
subs = re.sub("(\=)(\d+?)$", lambda x : x.group(1) + "eq", string)
print(subs)
# and wherever a lambda works, you can also use a function pointer

# if you're going to run the same pattern multiple times, then compile the pattern and use it
pattern = re.compile("\w+?=(\d+?)$")
if pattern.search(string):
    print("found")
# and for replace
pattern = re.compile("\d+?$")
subs = pattern.sub("456", string)
print(subs)