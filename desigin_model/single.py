#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：single.py
@Author  ：mrProtein
@Date    ：2022/7/7
@Desc    : 
"""


class SingleCall(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance


class SingleNew(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super(SingleNew, cls).__new__(cls, *args, **kwargs)
        return cls.instance


class A(SingleNew):
    pass


class B(metaclass=SingleCall):
    pass


if __name__ == '__main__':
    a1 = A()
    a2 = A()
    print(id(a1))
    print(id(a2))
    print(a1 is a2)

    a1 = B()
    a2 = B()
    print(id(a1))
    print(id(a2))
    print(a1 is a2)
