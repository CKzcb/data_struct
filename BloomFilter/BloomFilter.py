#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：BloomFilter.py
@Author  ：mrProtein
@Date    ：2022/7/5
@Desc    : 
布隆过滤器，在大量的数据中，判断某个数据是否存在时经常使用，有非常高效的空间效率与查询效率
缺点：存在一定的误判率
n:数据规模 p:要求的误判率
二进制数据位数 m=-n*lnp/(ln2)^2
哈希函数个数 k=m/n*ln2
"""
import ctypes
import math


class BloomFilter(object):
    def __init__(self, n: int, p: float):
        """
        :param n:数据规模
        :param p:误判率
        """
        # 计算二进制数组规模与hash函数数量
        self.bit_size = int(-n * math.log(p) / math.pow(math.log(2), 2))
        self.hash_func_size = int(self.bit_size * math.log(2) / n)
        self.bit_array = [0] * (int((self.bit_size + 32 - 1) / 32))

    def put(self, value):
        """
        :param value:存入的数据
        """
        self.value_check(value)
        # 哈希值的设置参考google布隆过滤器源码
        hash1 = value.__hash__()
        hash2 = self.unsigned_right_shift(hash1, 16)
        for i in range(self.hash_func_size):
            combined_hash = hash1 + i * hash2
            if combined_hash < 0:
                combined_hash = ~combined_hash
            combined_hash = combined_hash % self.bit_size
            index = int(combined_hash / 32)  # 位于第index个int元素
            position = combined_hash - index * 32  # 在int中的位置
            self.bit_array[index] = self.bit_array[index] | (1 << position)

    def contains(self, value):
        """
        :param value:判断是否存在的数据
        :return:True or False
        """
        self.value_check(value)
        hash1 = value.__hash__()
        hash2 = self.unsigned_right_shift(hash1, 16)
        for i in range(self.hash_func_size):
            combinedHash = hash1 + i * hash2
            if combinedHash < 0:
                combinedHash = ~combinedHash
            combinedHash = combinedHash % self.bit_size
            index = int(combinedHash / 32)  # 位于第index个int元素
            position = combinedHash - index * 32  # 在int中的位置
            result = self.bit_array[index] & (1 << position)
            if result == 0:
                return False
        return True

    @staticmethod
    def value_check(value):
        if value is None:
            print('value can\'t be None')

    @staticmethod
    def int_over_flow(val):
        maxint = 2147483647
        if not -maxint - 1 <= val <= maxint:
            val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
        return val

    # 无符号右移
    def unsigned_right_shift(self, n, i):
        # 数字小于0，则转为32位无符号uint
        if n < 0:
            n = ctypes.c_uint32(n).value
        # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
        if i < 0:
            return -self.int_over_flow(n << abs(i))
        # print(n)
        return self.int_over_flow(n >> i)


if __name__ == '__main__':
    n = 100000000
    p = 0.01
    bf = BloomFilter(n, p)
    total_size = 10000000
    error_count = 0
    for i in range(total_size):
        bf.put(i)

    for i in range(total_size):
        if not bf.contains(i):
            error_count += 1
    print('error rate :', float(error_count / total_size) if error_count > 0 else 0)
