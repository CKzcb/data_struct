#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_tcp_poll_server.py
@Author  ：mrProtein
@Date    ：2022/7/8
@Desc    : 
"""
import socket
import select


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 6666))
s.setblocking(False)
s.listen()

connections = {}

poll = select.poll()

poll.register(s.fileno(), select.POLLIN)
print("waiting ... ")

while True:
    try:
        events = poll.poll(timeout=1)
    except KeyboardInterrupt:
        break
    for fd, flag in events:
        print(fd, flag)
        if fd == s.fileno():
            c, addr = s.accept()
            print("connect ... ", c, addr)
            c.setblocking(False)
            poll.register(c.fileno(), select.POLLIN)
            connections[c.fileno()] = c
        elif flag & select.POLLIN:
            sock = connections[fd]
            try:
                print(sock.recv(1024))
            except:
                pass




