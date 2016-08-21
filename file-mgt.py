#!c:/Users/barraud/AppData/Local/Programs/Python/Python35/python.exe


def read_by_line():
    with open("files-list.log", "r") as f:
        for line in iter(f):
            print(line.rstrip())


# using maps and list comprehensions
# remember, in 3.x maps return iterables (not lists)
# list comprehensions are, of course, lists
def read_all_lines():
    with open("files-list.log", "r") as f:
        # using list comprehensions
        lines = [line.rstrip() for line in f]
        # using map and lambda
        lines = map(lambda x: x.rstrip(), f)

        # get lines but with the trailing \n
        lines = f.read()
        print(lines)


# open file to write (w)
def write_file():
    with open("xyz.log", "w") as f:
        f.write('first line')
        f.write("\n")
        f.write("last line")
