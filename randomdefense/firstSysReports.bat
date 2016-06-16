set usedDefinedPath=YOU TYPE PATH THEY GO HERE
tasklist /svc >> %usedDefinedPath%\tasksreport.txt
echo. >> %usedDefinedPath%\tasksreport.txt
tasklist /v >> %usedDefinedPath%\tasksreport.txt
schtasks >> %usedDefinedPath%\scheduledtasksreport.txt
net users > %usedDefinedPath%\usersreport.txt
(
  for /F %%h in (%usedDefinedPath%\usersreport.txt) do (
    net user %%h >NUL
	if %errorlevel%==0 net user %%h >> %usedDefinedPath%\usersreport.txt 
  )
)
echo. >> %usedDefinedPath%\usersreport.txt
echo Below is the administrators group: >> %usedDefinedPath%\usersreport.txt
net localgroup Administrators >> %usedDefinedPath%\usersreport.txt
echo. >> %usedDefinedPath%\usersreport.txt
echo Below is the account lockout policy
net accounts >> %usedDefinedPath%\usersreport.txt
echo Users Report Compiled
net share >> %usedDefinedPath%\sharesreport.txt
echo Shares Report Compiled