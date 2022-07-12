#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：map_node.py
@Author  ：mrProtein
@Date    ：2022/7/11
@Desc    : 
"""


class Node(object):
    """"""

    def __init__(self, value):
        self.value = value
        self.in_node: int = 0  # 入度
        self.out_node: int = 0  # 出度
        self.edges_list: list = []  # 发散出去的边
        self.node_list: list = []


class Edge(object):
    """边"""

    def __init__(self, weight, from_node, to_node):
        self.weight = weight
        self.from_node: Node = from_node
        self.to_node: Node = to_node



def tran_map(array):
    new_map = dict()
    new_edge_list = []
    for arr in array:
        from_node = arr[0]
        to_node = arr[1]
        weight = arr[2]
        if from_node not in new_map:
            new_map[from_node] = Node(from_node)
        if to_node not in new_map:
            new_map[to_node] = Node(to_node)
        from_node = new_map.get(from_node)
        to_node = new_map.get(to_node)
        edge = Edge(weight, from_node, to_node)
        from_node.node_list.append(to_node)
        from_node.out_node += 1
        to_node.in_node += 1
        from_node.edges_list.append(edge)
        new_edge_list.append(edge)
    return new_map, new_edge_list




