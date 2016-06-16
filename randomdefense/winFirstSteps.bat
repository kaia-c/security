After we eleminate threats, goto UserAccountsProcess.txt
When you find something, kill it and call me. 
If you have all the reports done and sysinternals windows up and u don't know what ur looking @, call me. 


Start downloads: sysinternals suite, malwarebytes


make unlikely path to store backups for now, so say enter cmds 
	mkdir C:\Drivers\storage\TNC9K\data
	mkdir C:\Drivers\storage\TNC9K\WIN
	mkdir C:\Drivers\storage\TNC9K\production
	mkdir C:\Drivers\storage\TNC9K\58r15
	mkdir C:\Drivers\storage\TNC9K\tmp
	mkdir C:\Drivers\storage\TNC9K\tmp\reports
	
	Let's actually put stuff in tmp.

reports:
	Enter path to reports in ProcessToPort.ps1. last line, copy to admin powershell.
	Fill in your userDefinedPath as C:\Drivers\storage\TNC9K\tmp\reports in firstSysReports.bat & firstNEtReports.bat
	Run them admin
	look at reports generated for  fires to put out. 
Notes for fires:
	net session \\<computer_name> /delete 					#get computer_name off shared folder/drivers\etc\hosts
	net group <group_name> <user> /delete /domain 			#delete user from group
	net localgroup <group name> <user> /delete 				#or localgroup
	net user <username> | findstr active 					#is user active?
	net user <username> /active:NO							#make user inactive
	wmic useraccount where name=<username> rename ndafuipafib	#mess with user
	Taskkill /PID <pid> /F									#kill processes
	Taskkill /IM <process name> /F
	Hopefully you have AccessEnum and ShareEnum by now, use them to fix and better visualize file/folder permissions.
	Or if it's all wrong, do a
	cd /
	icalcs * /T /Q /C /RESET
	and then set up your differences from default.

cmd (admin) from directory you downloaded sysinternals to:
logonsessions.exe -p
logonsessions.exe -p > C:\Drivers\storage\TNC9K\tmp\reports\logonsessions.txt
Run sysinternals Process Monitor to start monitering changes by proceses
then AutoRuns to work on sched tasks
Then TCPView & ProcessExplorer to give more clarity on process/process port reports 
If you haven't found the bleeding when its done downloading, run malwarebytes 


Run auditpols.bat

hosts file: check nothing added or nothing out of network. 
	type C:\Windows\System32\drivers\etc\hosts
	if there is notepad C:\Windows\System32\drivers\etc\hosts and fix.
	
Registry hardening.
	Go to regedit, click Computer in left-tree, right-click, choose 'Export'. Save to C:\Drivers\storage\TNC9K\tmp\reg1.reg
	Run regharden.bat.
	Export a reg2.reg
	type cmd: 
	fc C:\Drivers\storage\TNC9K\tmp\reg1.reg C:\Drivers\storage\TNC9K\tmp\reg2.reg > C:\Drivers\storage\TNC9K\tmp\reports\regchanges.txt
	Assuming no issues, now go to gpedit.msc,User Configuration>Administrative Templates>System. right panel "Prevent access to registry editing tools" and prevent changes to reg for all but system nt authorihy.
 
	
Patch this stuff:
	XP/2003 -
	MS08-067
	http://goo.gl/0C4DLl

	2000/XP/2003-
	MS06-040
	http://goo.gl/6LqrHH

	XP/2003/7/Vista/2008/2008 R2-
	MS12-020
	http://goo.gl/dxpsgd

	NT/XP/2000/2003-
	MS03-026
	http://goo.gl/7E1jFV

	Vista/7/2008-
	MS09-050
	http://goo.gl/YweHS5
	
