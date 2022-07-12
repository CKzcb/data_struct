#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_tcp_server_not_block.py
@Author  ：mrProtein
@Date    ：2022/7/8
@Desc    : 
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 6666))

s.setblocking(False)
s.listen(5)
count = 1
while True:
    try:
        c, addr = s.accept()
        print(c, addr)
    except BlockingIOError as e:
        # print("in error ", count)
        # count += 1
        continue


