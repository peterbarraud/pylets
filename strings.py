#!c:/Users/barraud/AppData/Local/Programs/Python/Python35/python.exe

string = "poker john"

# a string is like a zero-indexed char array

# to get the first char out of the string

print (string[0])

# to get the first 3 chars
print (string[:3])

# to get the last
print (string[-1])

# to get from the 2nd to the 5th char
print (string[2:5])

# remove the trailing newline from a string (like Perl's chomp)
print (string.rstrip())
# or remove any trailing char
print (string.rstrip('n'))
