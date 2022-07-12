#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：traverse.py
@Author  ：mrProtein
@Date    ：2022/7/11
@Desc    : 
"""
import queue
from .map_node import Node
from typing import List


def bfs(node: Node):
    """
    广度优先，用队列
    宽度遍历，队列处理数据
    set集合判断是否处理过
    :param node:
    :return:
    """
    if not node:
        return
    q = queue.Queue()
    q.put(node)
    s = set()
    s.add(node)
    while not q.empty():
        cur: Node = q.get()
        print(cur.value)
        for node in cur.node_list:
            if node not in s:
                s.add(node)
                q.put(node)


def dfs(node: Node):
    """
    深度遍历，用栈
    :param node:
    :return:
    """
    stack = []
    s = set()
    stack.append(node)
    s.add(node)
    print(node.value)
    while stack:
        cur = stack.pop()
        for node in cur.node_list:
            if node not in s:
                stack.append(cur)
                stack.append(node)
                s.add(node)
                print(node.value)
                break


def s(node_list: List[Node]):
    """
    拓扑排序，获取所有点，先取出入度为0的点，遍历，遍历后将遍历过得删除
    :param node_list:
    :return:
    """
    zero_que = queue.Queue()
    node_map = {}
    for node in node_list:
        node_map[node.value] = node.in_node
        if not node.in_node:
            zero_que.put(node)
    result = []
    while not zero_que.empty():
        cur: Node = zero_que.get()
        result.append(cur)
        for node in cur.node_list:
            node_map[node.value] -= 1
            if not node_map[node.value]:
                zero_que.put(node)


