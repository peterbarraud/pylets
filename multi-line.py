#!c:/Users/barraud/AppData/Local/Programs/Python/Python35/python.exe
from string import Template

# define simple multi-line string
string = ("first line\n"
          "\tsecond line with tab\n"
          "last line")
print(string)

# but simple multi-line strings done work with variables
# enter the Template

# $first - basic variable declaration
# $second - use the curly bracket syntax in case there's no space between the variable and the next/previous char
# $$third - say you wanted to enter $$third as a literal, use extra $ to escape the $ syntax

template = Template("$first line\n"
                    "${second} line\n"
                    "$$third line")
second_var = "2nd"

print(template.substitute(first="first", second=second_var))

# use save_substitute if you don't want to replace all variables. else Python throws an error
print(template.safe_substitute(second=second_var))

# you can also use a dictionary
d = {}
d['first'] = 'first'
d['second'] = second_var
print(template.substitute(d))
