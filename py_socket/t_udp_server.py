#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_udp_server.py
@Author  ：mrProtein
@Date    ：2022/7/8
@Desc    : 
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 6666))

print(s.recvfrom(1024))

