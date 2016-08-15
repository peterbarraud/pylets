#!c:/Users/barraud/AppData/Local/Programs/Python/Python35/python.exe

import os

# make windows path for py
def manageWindowsPath(folderpath):
    if os.path.isdir (folderpath):
        folderpath = folderpath.replace("\\","/")
        if folderpath.endswith("/") == False :
            folderpath = folderpath + "/"
        return folderpath
    else :
        raise Exception ("Invalid folder Path")


try :
    folderpath = manageWindowsPath(input ("Enter folder path: "))
except Exception as ex :
    print (ex)
