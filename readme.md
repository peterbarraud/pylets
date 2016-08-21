# Create new py

Open the git bash and type `where python`

Copy the output line and paste it at the top of your script (very first line) preceeded by a hash (#)

For example:
```
#!c:/Users/barraud/AppData/Local/Programs/Python/Python35/python.exe
```
Open the git bash at the py location

To compile the py, enter

```
chmod +x <name>.py
```

To run the script, enter

```
./<name>.py
```

# Code conventions
1. The #! statement must be at the very first line
2. ```import statement``` There must be a blank line between the first line and the
3. ```def statement``` There must be at least two blank lines before a def statement
4. There must be no space between a function call and the opening bracket: ```print('something')```
5. In a function call, there must be a single space after a comma: ```print('something, 'something else')```
6. <b>Function names</b>: use underscore instead of camel case for variable/function names: ```add_num``` instead of ```addNum``` or even ```addnum```


# Other useful libraries
[Config parser](https://docs.python.org/3/library/configparser.html)

[godaddy Django hosting](https://in.godaddy.com/pro/one-click-installation/django)

[Eclipse setup](http://www.vogella.com/tutorials/Python/article.html)

[List comprehensions](http://www.secnetix.de/olli/Python/list_comprehensions.hawk)

[Collections library](https://docs.python.org/2/library/collections.html)
