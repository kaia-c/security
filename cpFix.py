#!/usr/bin/env python
#Script to recurse starting at given dir, looking in public_html's and all subfolders for security vulns.
#Can:
#write default index.html to dirs without a default page
#chmod to 750 for public_html, 755 for subdirs, 644 for files
#find risky files being displayed and gives user choice to move them to non-public location after reviewing in browser
#records all changes made

import os
import sys
import errno
import time

defaults=["index.html", "index.htm", "index.shtml", "index.php", "index.php5", "index.php4", "index.php3", "index.cgi", "default.html", "default.htm", "home.html", "home.htm", "Index.html", "Index.htm", "Index.shtml", "Index.php", "Index.cgi", "Default.html", "Default.htm", "Home.html", "Home.htm", "placeholder.html"]
indexDefault="""<!DOCTYPE html>
<html>
<head>
<title>Error</title>
</head>
<body>
<div>Nothing to See Here. . .</div>
</body>
</html>
"""
startDir="/home/anger/"#TEST pass -d to change
accountDomains={}
movedFiles=[]
indexWrittenTo=[]
changedPerms={}
changedOwn={}
crawledFiles=[]
hitwww=True
currentAccount=""
verbose=False
storeDir = "/usr/local/cpFix/"

def setAccountDomains():
    try:
        os.chdir('/var/cpanel/users')
        stdout=os.popen('ls | xargs grep DNS').read()
        for i in stdout.split('\n'):
            try:
                arr=i.split(':')
                domain=arr[1].split('=')[1]
                try:
                    accountDomains[arr[0]].append(domain)
                except:
                    accountDomains[arr[0]]=[ domain ]
            except:
                pass
        return (len(accountDomains)>0)
    except:
        return False

def subdirs(path):
    return filter(os.path.isdir, [os.path.join(path,f) for f in os.listdir(path)])

def files(path):
    return [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

def defaultInDir(directory):
    return (len([i for i in files(directory) if i in defaults])>0)

def mkdir(account=""):
    if account == "":
        try:
            os.system("mkdir /usr/local/cpFix 2>/dev/null")
            return True
        except:
            return False
    else:
        try:
            os.system("mkdir "+storeDir+account+" 2>/dev/null")
            return True
        except:
            return False

def writeNoClobber(fileName, directory="", file=indexDefault):
    if directory == ".":
        directory=""
    elif len(directory) > 0 and not directory.endswith('/'):
        directory=directory+'/'
    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
    try:
        file_handle = os.open(directory+fileName, flags)
    except OSError as e:
        if e.errno == errno.EEXIST:
            return False
        else:
            print(e)
            return False
    else:
        with os.fdopen(file_handle, 'w') as file_obj:
            file_obj.write(file)
            return True

def writeIndexIfNotExists(directory):
    if(not defaultInDir(directory)):
        stdin=yorn("A default index page was not found in "+directory+". \nWrite one now?") if verbose else True
        if stdin:
            status=writeNoClobber("index.html", directory)
            if status:
                os.system("chown "+currentAccount+":"+currentAccount+" "+directory+"/index.html")
                os.system("chmod 644 "+directory+"/index.html")
            return status
    return False

def parseDirectory(directory):
    try:
        arr=directory.split('public_html')
        webpart=arr[1][1:]
        account=arr[0].split('/')[-2] if arr[0].find('/') > -1 else arr[0]
        return account, webpart, 'public_html'
    except:
        try:
            arr=directory.split('www')
            webpart=arr[1][1:]
            account=arr[0].split('/')[-2] if arr[0].find('/') > -1 else arr[0]
            return account, webpart, 'www'
        except:
            pass
        return False, False, False

def yorn(question):
    answer="2"
    while answer != True and answer != False:
        tmp=raw_input(question+"\nAnswer Yes or No:  ")
        tmp=tmp[:1].upper()
        if tmp == "Y":
            answer=True
        elif tmp == "N":
            answer = False
        else:
            print("Please answer 'Yes' or 'No'\n")
    return answer

def handleDirectory(directory, webpart):
    global currentAccount
    global changedPerms
    global changedOwn
    global storeDir
    global crawledFiles
    try:
        for i in files(directory):
            moved=False
            if verbose:
                crawledFiles.append(directory+"/"+i)
            if not i.lower().endswith((".ftpquota",".htaccess",".tng",".cur", ".ani", ".otf", ".woff2", ".eot", ".ttf", ".woff", ".svg", ".html", ".php", ".htm", ".xml", ".json", ".css", ".js", ".jpg", ".ico", ".png", ".mp4", ".gif", ".xcf")):
                page=(accountDomains[currentAccount][0]+("/"+webpart+"/" if len(webpart)>0 else "/")+i)
                mvFile=yorn("Review "+page+" in your browser for information disclosure. Should I move this file to a non-public location?")
                if mvFile:
                    try:
                        fileWithPath=directory+"/"+i
                        syscall = "mv "+fileWithPath+" "+storeDir+currentAccount+"/"+(fileWithPath.replace("/", "_")[1:])
                        os.system(syscall)
                        movedFiles.append(page+" moved with "+syscall)
                        moved=True
                    except Exception as e:
                        print(e.message+" "+e.__doc__)
            if any(j in i.lower() for j in ["readme", "read-me", "read_me", "test", "phpinfo", "changelog"]):
                page=(accountDomains[currentAccount][0]+("/"+webpart+"/" if len(webpart)>0 else "/")+i)
                mv=yorn("Review "+page+" in your browser for information disclosure. Should I move this file to a non-public location?")
                if mv:
                    try:
                        fileWithPath=directory+"/"+i
                        syscall = "mv "+fileWithPath+" "+storeDir+currentAccount+"/"+(fileWithPath.replace("/", "_")[1:])
                        os.system(syscall)
                        movedFiles.append(page+" moved with "+syscall)
                        moved = True
                    except Exception as e:
                        print(e.message+" "+e.__doc__)
            if not moved:
                stdout=os.popen("ls -la "+directory+"/"+i).read()
                columns=stdout.split(' ')
                if not (stdout.startswith("-rw-r--r--") or columns[0].endswith("------")):
                    change = False
                    if verbose:
                        change=yorn("Current permissions for "+directory+"/"+i+" are set to:\n"+columns[0]+"\nChange to 644?")
                    if (not verbose) or change:
                        os.system("chmod 644 "+directory+"/"+i)
                        changedPerms[directory+"/"+i]={columns[0]:"-rw-r--r--"}
                    if currentAccount != columns[2] and currentAccount != columns[3]:
                        change = False
                        if verbose:
                            change = yorn("Current owner for "+directory+"/"+i+" are: "+columns[2]+":"+columns[3]+". Change to "+currentAccount+":"+currentAccount+" ?")
                        if (not verbose) or change:
                            os.system("chown "+currentAccount+":"+currentAccount+" "+directory+"/"+i)
                            changedOwn[directory+"/"+i]={columns[2]+":"+columns[3]:currentAccount+":"+currentAccount}
        stdout=os.popen("ls -la "+directory+" | head -n 2 | tail -n -1").read()
        columns=' '.join(stdout.split()).split()
        if not directory.endswith("public_html"):
            goPerms=columns[0][4:]
            if "w" in goPerms:
                change = False
                if verbose:
                    change = yorn("Current permissions for "+directory+" are set to: "+columns[0]+"\nChange to 755?")
                if (not verbose) or change:
                    os.system("chmod 755 "+directory)
                    changedPerms[directory]={columns[0]:"drwxr-xr-x"}
            if currentAccount != columns[2] or currentAccount != columns[3]:
                change = False
                if verbose:
                    change = yorn("Current owner for "+directory+" are: "+columns[2]+":"+columns[3]+". Change to "+currentAccount+":"+currentAccount+" ?")
                if (not verbose) or change:
                    os.system("chown "+currentAccount+":"+currentAccount+" "+directory)
                    changedOwn[directory]={columns[2]+":"+columns[3]:currentAccount+":"+currentAccount}
        if directory.endswith("public_html"):
            if not (stdout.startswith("drwxr-x---")):
                change = False
                if verbose:
                    change = yorn("Current permissions for "+directory+" are set to: "+columns[0]+"\nChange to 750?")
                if (not verbose) or change:
                    os.system("chmod 750 "+directory)
                    changedPerms[directory]={columns[0]:"drwxr-x---"}
            if currentAccount != columns[2] or "nobody" != columns[3]:
                change = False
                if verbose:
                    change = yorn("Current owner for "+directory+" are: "+columns[2]+":"+columns[3]+". Change to "+currentAccount+":nobody ?")
                if (not verbose) or change:
                    os.system("chown "+currentAccount+":nobody "+directory)
                    changedOwn[directory]={columns[2]+":"+columns[3]:currentAccount+":nobody"}
        wroteIndex=writeIndexIfNotExists(directory)
        if(wroteIndex):
            indexWrittenTo.append(directory)
    except Exception as e:
        print(e.message, e.__doc__)
    #print("calling recurse("+directory+")")#TEST
    recurse(directory)

def recurse(directory):
    for i in subdirs(directory):
        drive(i)

def drive(directory):
    global hitwww
    global currentAccount
    account, webpart, webroot=parseDirectory(directory)
    if currentAccount!=account:
        mkdir(account)
        hitwww=True
        currentAccount=account
    if webroot:
        if "public_html" in webroot:
            hitwww=False
            #print("calling handleDirectory("+directory+","+webpart+")")#TEST
            handleDirectory(directory, webpart)
        if webroot == "www" and hitwww==True:
            handleDirectory(directory, webpart)
    elif hitwww:
        recurse(directory)

def usage():
    print("""TO DO""")

def setOpts():
    global verbose
    global startDir
    global defaultIndex
    if "-h" in sys.argv or "--help" in sys.argv:
        usage()
    else:
        pos = -1
        if "-d" in sys.argv or "--directory" in sys.argv:
            try:
                pos=sys.argv.index("-d")
            except:
                try:
                    pos=sys.argv.index("--directory")
                except:
                    pass
            if pos > 0:
                startDir=os.path.abspath(sys.argv[pos+1])
                pos = -1
        if "-i" in sys.argv or "--index" in sys.argv:
            try:
                pos=sys.argv.index("-i")
            except:
                try:
                    pos=sys.argv.index("--index")
                except:
                    pass
            if pos > 0:
                defaultIndex=sys.argv[pos+1]
                pos = -1
        if "-v" in sys.argv or "--verbose" in sys.argv:
            try:
                pos=sys.argv.index("-v")
            except:
                try:
                    pos=sys.argv.index("--verbose")
                except:
                    pass
            if pos > 0:
                verbose=True
                pos = -1
        if "-f" in sys.argv or "--index-file" in sys.argv:
            pass
            "TO DO"
        if "-r" in sys.argv or "--index-resource" in sys.argv:
            pass
            """TO DO"""


def printResults():
    global movedFiles
    global indexWrittenTo
    global changedPerms
    global changedOwn
    global storeDir
    global crawledFiles
    string=""
    string2=""
    if len(movedFiles)>0:
        string+=("\n\t-------------\nThe following files were moved under "+storeDir+":\n")
    for i in movedFiles:
        string+=(i+"\n")
    if len(indexWrittenTo)>0:
        string+=("\n\t-------------\nThe following directories had an index.html file written to them:\n")
    for i in indexWrittenTo:
        string+=(i+"\n")
    if len(changedPerms.keys())>0:
        string+=("\n\t-------------\nThe following had permissions changed:\n")
    for i,j in changedPerms.iteritems():
        string+=(i +" was changed from "+ j.keys()[0] +" to " + j[j.keys()[0]] + "\n")
    if len(changedOwn.keys())>0:
        string+=("\n\t-------------\nThe following had ownership changed:\n")
    for i,j in changedOwn.iteritems():
        string+=(i +" was changed from "+ j.keys()[0] +" to " + j[j.keys()[0]]+ "\n")
    if len(crawledFiles)>0:
        string2+="The following files were crawled:\n"
        for i in crawledFiles:
            string2+=(i+"\n")
    mkdir("results")
    print(string)
    print("\n\nReview these results at:"+storeDir)
    f=open(storeDir+"results/result"+time.strftime("%Y-%m-%d_%H:%M")+".txt", "a+")
    f.write(string2)
    f.write(string)
    f.close()
    exit(0)

try:
    setOpts()
    if setAccountDomains():
        mkdir()
        drive(startDir)
        printResults()
    else:
        print("This doesn't look like a cPanel server.\nGoodbye\n")
        exit(1)
except KeyboardInterrupt:
    printResults()
    exit(2)
except Exception as e:
    printResults()
    print(e.message, e.__doc__)
    exit(1)
