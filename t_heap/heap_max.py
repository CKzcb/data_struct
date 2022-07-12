#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：heap_max.py
@Author  ：mrProtein
@Date    ：2022/7/5
@Desc    : 
"""


class MaxHeap(object):
    """"""

    def __init__(self, max_size: int):
        self.max_size: int = max_size
        self.heap: list = []
        self.size: int = 0

    def push(self, value: int) -> bool:
        if self.size >= self.max_size or value is None:
            return False
        self.heap.append(value)
        self._adjust_insert(self.size)
        self.size += 1
        return True

    def _adjust_insert(self, i: int):
        while i > 0:
            if self.heap[(i - 1) // 2] < self.heap[i]:
                self._swap(i, (i - 1) // 2)
                i = (i - 1) // 2

    def _swap(self, i: int, j: int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def printf(self):
        print(self.heap)

    @staticmethod
    def _adjust(array: list):
        n = len(array)
        for i in range(n//2):
            left = i * 2 + 1
            while left < n:
                m = left + 1 if left + 1 < n and array[left+1] > array[left] else left
                m = m if array[m] > array[i] else i
                if m == i:
                    break
                array[m], array[i] = array[i], array[m]
                i = m
                left = 2 * i + 1
            #


        print(array)
        # 将最大的换到最小
        for i in range(n-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            # 调整
            j = 0
            while j * 2 + 1 < i:
                m = j
                if array[j*2+1] > array[j]:
                    m = j * 2 + 1
                if j * 2 + 2 < i and array[j*2+2] > array[m]:
                    m = j * 2 + 2
                if m == j:
                    break
                array[m], array[j] = array[j], array[m]
                j = m
            print(i, j, array)


if __name__ == '__main__':
    # mp = MaxHeap(10)
    # mp.push(2)
    # mp.push(4)
    # mp.printf()
    # mp.push(6)
    # mp.printf()
    arr = [2,3, 1, 4, 7, 5]
    MaxHeap._adjust(arr)
    print(arr)

