#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_consumer_poll.py
@Author  ：mrProtein
@Date    ：2022/7/10
@Desc    : 
"""


from kafka import KafkaConsumer
import time


def do_t(i):
    print("c_{}_start ... ".format(i))
    kc = KafkaConsumer(
        group_id="test1",
        bootstrap_servers=["49.233.27.128:9092", "49.233.27.128:9093", "49.233.27.128:9094"])
    kc.subscribe("kak1")
    c = 0
    while True:
        results = kc.poll(max_records=10)
        print(c, type(results), len(results), results)
        time.sleep(60)

if __name__ == '__main__':
    do_t(1)