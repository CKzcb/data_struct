#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_consumer.py
@Author  ：mrProtein
@Date    ：2022/7/10
@Desc    : 
"""
from kafka import KafkaConsumer
from threading import Thread


def do_t(i):
    print("c_{}_start ... ".format(i))
    kc = KafkaConsumer(
        group_id="test1",
        bootstrap_servers=["49.233.27.128:9092", "49.233.27.128:9093", "49.233.27.128:9094"])
    kc.subscribe("kak1")
    kc.poll()
    for msg in kc:
        print("c_{}: ".format(i), msg)

    kc.commit()


if __name__ == '__main__':
    t_l = []
    for i in range(3):
        t_l.append(Thread(target=do_t, args=(i,)))

    for t in t_l:
        t.start()

    for t in t_l:
        t.join()



