#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_lock.py
@Author  ：mrProtein
@Date    ：2022/7/9
@Desc    : 
"""
from kazoo.client import KazooClient


zk = KazooClient(hosts="49.233.27.128:2185")

zk.Lock()

zk.ReadLock()

