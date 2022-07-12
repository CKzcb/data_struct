#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：heap_min.py
@Author  ：mrProtein
@Date    ：2022/7/4
@Desc    :
小根堆
"""


class MinHeap(object):

    def __init__(self, max_size: int = 0):
        self.heap: list = []
        self.max_size: int = max_size
        self.size: int = 0

    def push(self, value: int) -> bool:
        if self.max_size <= len(self.heap):
            return False
        self.heap.append(value)
        self._adjust(self.size)
        self.size += 1

    def _swap(self, i1, i2):
        temp = self.heap[i1]
        self.heap[i1] = self.heap[i2]
        self.heap[i2] = temp

    def _adjust(self, i):
        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            self._swap(i, (i - 1) // 2)
            i = (i - 1) // 2

    def printf(self):
        print(self.heap)

    def pop(self):
        if self.size <= 0:
            return None
        t = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.heap.pop(-1)

        i = 0
        li = 0
        while i * 2 + 1 < self.size and i * 2 + 2 < self.size and (
                self.heap[i * 2 + 1] < self.heap[i] or self.heap[i * 2 + 2] < self.heap[i]):
            if self.heap[i * 2 + 1] < self.heap[i * 2 + 2]:
                self._swap(i, i * 2 + 1)
                i = i * 2 + 1
            else:
                self._swap(i, i * 2 + 2)
                i = i * 2 + 2
        if i *2 + 1 < self.size:
            if self.heap[i] > self.heap[i*2+1]:
                self._swap(i, i*2+1)
        return t


if __name__ == '__main__':
    m = MinHeap(10)
    m.push(1)
    m.push(7)
    m.printf()
    m.push(5)
    m.push(4)
    m.push(10)
    m.printf()
    print(m.pop())
    m.printf()
