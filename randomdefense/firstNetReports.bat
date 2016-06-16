
set usedDefinedPath=YOU TYPE PATH THEY GO HERE
dism /online /get-features >> %usedDefinedPath%\featuresreport.txt
echo Features Report Compiled
netsh advfirewall firewall show rule name=all > %usedDefinedPath%\firewallreport.txt
echo --Port Information Below-- >> %usedDefinedPath%\firewallreport.txt
netstat -ano >> %usedDefinedPath%\firewallreport.txt
dir /r /s C:\*.* | findstr /v "AM" | findstr /v "PM" | findstr /v "File(s)" | findstr /v "Dir(s)" | findstr /v "Directory of" | findstr /v "Zone.Identifier" > basedads.txt