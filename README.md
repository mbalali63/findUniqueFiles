# findUniqueFiles
## General Idea
The code was developed to solve the problem of searching and finding duplicate files, and archiving a **unique** of each file, 
which could a very time consuming work for human. So I just tried to simply automate it.
The currently uploaded version is set for pdf files, but it could be generalized.
For file operation, the python pathlib was utilized.
The code will generate a log file, which described succession or failor of generating unique copy of each file.
There may be some problem in file name formats, that the current version could not handle them. So it will 
ignore and log such files.

