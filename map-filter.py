#!C:/Users/barraud/AppData/Local/Programs/Python/Python35/python.exe

# Use "map" to do one (and the same) thing to eash element in a list
def squareall(alist):
    retval = map (lambda x : x**2,alist)
    # retval is a map object. this is a iteratable object so if you just want to iterate over the contents, use "for in"
    # however, if you do need to get the list out of this just use list (map)
    for item in retval :
        print (item)
    for item in retval :
        print (ite)
    return list(retval)
# Use "filter" to filter the list down by the given criteria
def even_list (alist):
    retval = filter (lambda x : x % 2 == 0,alist)
    # retval is a filer object. this is a iteratable object so if you just want to iterate over the contents, use "for in"
    # however, if you do need to get the list out of this just use list (filter)
    for item in retval :
        print (item)
    return list(retval)

alist = [3,4,5]

# a lambda is an anonymous single-line function.
# if you want to do more than can be fitted into a single line, you can pass a function pointer to the map or filter
# like
# map (functiondef,list)
squaredLlist = squareall(alist)

even_list(alist)

