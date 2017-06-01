import socket
import thread
from datetime import datetime

HOST = ''
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connected by', addr
data = ''

f = open('hookingValue.txt','a')
DateTime = str(datetime.today())

def pr_msg():
    while 1:
        data = conn.recv(1024)
        if data:
            f.write("\n"+DateTime+data)
            print("!!!" + data)
    f.close()

def main():
    pr_msg()
    conn.close()

if __name__ == "__main__":
    main()
