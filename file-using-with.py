#!c:/Users/barraud/AppData/Local/Programs/Python/Python35/python.exe


def readbyline ():
	with open("files-list.log","r") as f:
		for line in iter(f):
			print (line.rstrip())

def readalllines() :
	with open("files-list.log","r") as f:
		lines = f.read()
		print (lines)

def writefile() :
	#open file to write (w)
	with open ("xyz.log","w") as f :
		f.write('first line')
		f.write("\n")
		f.write("last line")


writefile()

print ("all done")
