#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_client.py
@Author  ：mrProtein
@Date    ：2022/7/8
@Desc    : 
"""

import socket

c = socket.create_connection(("127.0.0.1", 6666))
print(c.recv(1024))



