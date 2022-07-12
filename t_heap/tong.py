#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：tong.py
@Author  ：mrProtein
@Date    ：2022/7/5
@Desc    : 
"""


def get_d(array: list):
    m = max(array)
    r = 0
    while m > 0:
        r += 1
        m //= 10
    return r


def so(array: list):
    for i in range(get_d(array)):
        b = [[] for _ in range(10)]
        base = i * 10
        for n in array:
            m = n // base if base else n
            b[m % 10].append(n)
        # print(b)
        array = []
        for l in b:
            array += l

    return array


if __name__ == '__main__':
    print(so([2, 300, 12, 4, 75, 5]))
