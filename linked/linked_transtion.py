#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：linked_transtion.py
@Author  ：mrProtein
@Date    ：2022/7/6
@Desc    : 
"""


class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


if __name__ == '__main__':
    head = Node(10)
    p = head
    import random
    for i in range(10):
        p.next = Node(random.randint(1, 100))
        p = p.next

    h1 = head
    l = []
    while h1:
        l.append(h1.val)
        h1 = h1.next
    print(l)

    h2 = head




