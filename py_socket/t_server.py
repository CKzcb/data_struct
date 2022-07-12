#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_server.py
@Author  ：mrProtein
@Date    ：2022/7/8
@Desc    : 
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 5555))
s.listen(5)
while True:
    c, addr = s.accept()
    print("connection...", c, addr)
    c.send("hi~".encode())





