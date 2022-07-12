#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_tcp_select_server.py
@Author  ：mrProtein
@Date    ：2022/7/8
@Desc    : 
"""

import select
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 6666))
s.listen(5)
r = [s]
w = []
while True:
    r1, _, _ = select.select(r, w, [])
    if r1:
        for c in r1:
            if c != s:
                print(c.recv(1024))
            else:
                b, addr= s.accept()
                r.append(b)
                print(b, addr)



