#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：t_t.py
@Author  ：mrProtein
@Date    ：2022/7/12
@Desc    : 
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


if __name__ == '__main__':
    head = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    head.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    # while node:
    #     print(node.val)
    #     node = node.next
    cur = head
    next_node = head.next
    while next_node:
        next_next = next_node.next
        next_node.next = cur
        cur = next_node
        next_node = next_next

    head.next = None
    head = cur
    node = head
    while node:
        print(node.val)
        node = node.next




