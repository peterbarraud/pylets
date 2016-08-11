#!c:/Users/barraud/AppData/Local/Programs/Python/Python35/python.exe

# Open file to read (r)
with open("files-list.log","r") as f:
	for line in iter(f):
		print (line.rstrip())
	# print (data)

#open file to write (w)
with open ("xyz.txt","w") as f :
	f.write('first line')
	f.write("\n")
	f.write("last line")

print ("all done")
