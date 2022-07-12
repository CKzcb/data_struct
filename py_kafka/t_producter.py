#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_producter.py
@Author  ：mrProtein
@Date    ：2022/7/10
@Desc    : 
"""
from kafka import KafkaProducer
import json


kp = KafkaProducer(bootstrap_servers=["49.233.27.128:9092", "49.233.27.128:9093", "49.233.27.128:9094"],
                   value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                   key_serializer=lambda v: json.dumps(v).encode('utf-8'))


def on_success(r):
    print(r.get())


while True:
    a = input()
    k = input()
    if not a:
        break
    print(kp.send("kak1", {"msg": a}, key=k))


print("stop ... ")





