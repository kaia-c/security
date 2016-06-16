@echo off
set usedDefinedPath=YOU TYPE PATH THEY GO HERE
dir /b /s "C:\Program Files\" > %usedDefinedPath%/programfiles.flashed
dir /b /s "C:\Program Files (x86)\" >> %usedDefinedPath%/programfiles.flashed
dir /b /s "C:\Users\" > %usedDefinedPath%/users.flashed
dir /b /s "C:\Documents and Settings" >> %usedDefinedPath%/users.flashed
dir /b /s "C:\" > %usedDefinedPath%/c.flashed


#can use like 
#	findstr "nmap" path/programfiles.flashed
#or define new usrPath2 and run and then do
#	fc usrpath2/users.flashed usrpath1/users.flashed
#to see changes. 