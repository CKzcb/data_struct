#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：top_k.py
@Author  ：mrProtein
@Date    ：2022/6/9
"""


def get_top_k_1(k: int, source_list: list) -> list:
    """
    获取top k，暴力解决，先进行排序
    :param k:
    :param source_list:
    :return:
    """
    if not k:
        return []
    # 逆序排序
    source_list.sort(reverse=True)
    return source_list[0:k]


def get_top_k_2(k: int, source_list: list) -> list:
    """
    获取top k，预留k的长度，将每个数据插入
    :param k:
    :param source_list:
    :return:
    """
    if not k:
        return []
    if k > len(source_list):
        return source_list
    # 预留返回数组为k
    ret_list = source_list[:k]
    ret_list.sort()
    # 插入
    for i in source_list[k:]:
        if ret_list[0] > i:
            continue
        # 大于最小的数，插入
        ret_list[0] = i
        ret_list.sort()

    return ret_list


if __name__ == '__main__':
    source_list = [12, 3, 5, 1, 9, 8, 4, 2]
    print(get_top_k_1(3, source_list))
    print(get_top_k_2(3, source_list))
