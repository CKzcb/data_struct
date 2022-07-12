#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：test_sort.py
@Author  ：mrProtein
@Date    ：2022/7/7
@Desc    :

排序

"""



def bubbling_sort(array: list):
    """
    冒泡排序
    因为越小的元素会经由交换以升序或降序的方式慢慢浮到数列的顶端，就如同碳酸饮料中二氧化碳的气泡最终会上浮到顶端一样，故名冒泡排序。
    时间复杂度：O(n^2) O(n^2) O(n)
    空间复杂度：O(1)
    稳定排序
    :param array:
    :return:
    """
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def select_sort(array: list):
    """
    选择，每次把大的选择放到最后
    :param array:
    :return:
    """
    n = len(array)
    for i in range(n):
        max_i = 0
        for j in range(n - i):
            if array[max_i] < array[j]:
                max_i = j
        array[max_i], array[n - i - 1] = array[n - i - 1], array[max_i]


def insert_sort(array: list):
    """
    插入排序
    :param array:
    :return:
    """
    for i in range(1, len(array)):
        while i >= 1 and array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1


def bucket_sort(array: list):
    """
    桶排序
    :param array:
    :return:
    """
    bucket_list = [0 for _ in range(10)]
    for i in array:
        bucket_list[i] += 1
    array.clear()
    for num, count in enumerate(bucket_list):
        while count > 0:
            array.append(num)
            count -= 1


def shell_sort(array: list):
    """
    希尔排序
    希尔排序又称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。

    希尔排序是非稳定排序算法，在对几乎已经排好序的数据操作时，效率极高，即可以达到线性排序的效率。
    先将整个待排序的记录序列分组，对若干子序列分别进行直接插入排序，
    随着增量逐渐减少即整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。
    :param array:
    :return:
    """
    n = len(array)
    gap = n // 2
    while gap:
        for i in range(gap, n):
            temp = array[i]
            while i >= gap and array[i - gap] > temp:
                array[i] = array[i - gap]
                i -= gap
            array[i] = temp
        gap = gap // 2


def merge_sort(array: list):
    """
    归并排序
    :param array:
    :return:
    """
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left: list, right: list):
    """
    合并
    :param left:
    :param right:
    :return:
    """
    result = []
    while left and right:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result




def heap_sort(array: list):
    """
    堆排序
    :param array:
    :return:
    """
    pass


def quick_sort_1(array: list):

    def partition(start, end):
        # 分区操做，返回基准线下标
        pivot = array[start]
        while start < end:
            while start < end and array[end] >= pivot:
                end -= 1
            array[start] = array[end]
            while start < end and array[start] <= pivot:
                start += 1
            array[end] = array[start]
        # 此时start = end
        array[start] = pivot
        return start

    stack = []
    stack.append(len(array) - 1)
    stack.append(0)

    while stack:
        l = stack.pop()
        r = stack.pop()
        index = partition(l, r)
        if l < index - 1:
            stack.append(index - 1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)


def quick_sort(array: list, start: int, end: int):
    """
    快速排序
    :param array:
    :param start:
    :param end:
    :return:
    """
    if start >= end:
        return
    left = start
    right = end
    mid = array[left]

    while left < right:
        while left < right and array[right] >= mid:
            right -= 1
        array[left] = array[right]

        while left < right and array[left] <= mid:
            left += 1
        array[right] = array[left]

    array[left] = mid
    quick_sort(array, start, left - 1)
    quick_sort(array, left + 1, end)




def binary_search(array: list, item: int) ->bool:
    """
    二分查找
    先排序
    :param array:
    :param item:
    :return:
    """
    n = len(array)
    if n < 10:
        sort = bucket_sort
    elif n < 50:
        sort = insert_sort
    else:
        sort = quick_sort
    sort(array)
    # 查找
    left = 0
    right = n - 1
    if array[left] > item or array[right] < item:
        return False
    while left <= right:
        middle = left + (right - left) // 2
        if array[middle] == item:
            return True
        elif array[left] <= item < array[middle]:
            right = middle
        else:
            left = middle

    return False


if __name__ == '__main__':
    a = [8, 2, 3, 1, 7, 6, 9, 5, 4]
    # print(binary_search(a, 10))
    # print(binary_search(a, 1))
    # bubbling_sort(a)
    # select_sort(a)
    # insert_sort(a)
    # bucket_sort(a)
    # shell_sort(a)
    # a = merge_sort(a)
    # quick_sort(a, 0, len(a) - 1)
    quick_sort_1(a)
    print(a)
