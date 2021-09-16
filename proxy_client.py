#!/usr/bin/env python3
import socket
import time

# define address & buffer size
HOST = ""  # localhost
PORT = 8001
BUFFER_SIZE = 1024

payload = f'GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n'

def connect(addr):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        full_data = s.recv(BUFFER_SIZE)
        print(full_data)

    except Exception as e:
        print(e)
    finally:
        s.close()

def main():
    connect((HOST, PORT))


if __name__ == '__main__':
    main()