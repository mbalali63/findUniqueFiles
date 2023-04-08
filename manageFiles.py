# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 15:34:50 2023

The program get the address of a folder, which contain pdf files.
Then walk through them and find a unique copy of each file in a 
folder called repository, inside the main folder.
Finally, it will creates a log file, that informs which of the files have 
been successfully copied and which were ignored, because of the 
file name format problems.


@author: Mahdi Balali
"""

import pathlib


p = pathlib.Path(r'C:\Files\Books') 

if p.exists():
    print("The pass exists.")
else:    
    print("The mentioed address does not exists.")
    


repository = p / 'repository'
if not repository.exists():
    repository.mkdir(parents = False, exist_ok = False)

listOfFiles = p.rglob('*.pdf')
ignoredFileCount = 0;
logFilePath = p / "log.txt"
logFile = open(logFilePath,"w",encoding="utf-8")
for file in listOfFiles:
    try:
        fname = file.name
        print(fname)
        newFile = repository / fname
        newFile.write_bytes(file.read_bytes())
        logFile.write("{} \t {}\n".format(file,"OK"))        
    except:
        print("\n\nThe file {} was ignored because of the wrong format\n\n".format(file))
        ignoredFileCount += 1;
        logFile.write("{} \t {}\n".format(file,"ignored"))
        pass
logFile.close()
print("Finished. But {} files were ignored because of wrong format.".format(ignoredFileCount))





