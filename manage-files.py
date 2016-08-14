#!c:/Users/barraud/AppData/Local/Programs/Python/Python35/python.exe

import os

# make windows path for py
def manageWindowsPath(folderpath):
    folderpath = folderpath.replace("\\","/")
    if folderpath.endswith("/") == False :
        folderpath = folderpath + "/"
    return folderpath


folderpath = manageWindowsPath(input ("Enter folder path: "))

if os.path.isdir (folderpath):
    print (folderpath)
else :
    print ("Invalid folder Path")
