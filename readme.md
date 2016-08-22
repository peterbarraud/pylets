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
2. <b>import statement</b> There must be a blank line between the first line and the
3. <b>def statement</b> There must be at least two blank lines before a def statement
4. There must be no space between a function call and the opening bracket: ```print('something')```
5. <b>Function call</b>: There must be a single space after a comma: ```print('something, 'something else')```
6. <b>Function names</b>: use underscore instead of camel case for variable/function names: ```add_num``` instead of ```addNum``` or even ```addnum```
7. <b>Semi colon for flow statements</b>: There must be no space before the semi colon in flow statments: ```if condition:``` instead of ```if condition :```
8. The last line of a file must be a blank line. But only one blank line

See also: [Intermezzo: Coding Style](https://docs.python.org/2/tutorial/controlflow.html#intermezzo-coding-style)

# Other useful libraries
[Config parser](https://docs.python.org/3/library/configparser.html)

[godaddy Django hosting](https://in.godaddy.com/pro/one-click-installation/django)

[Eclipse setup](http://www.vogella.com/tutorials/Python/article.html)

[List comprehensions](http://www.secnetix.de/olli/Python/list_comprehensions.hawk)

[Collections library](https://docs.python.org/2/library/collections.html)
