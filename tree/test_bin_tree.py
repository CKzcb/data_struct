#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：test_bin_tree.py
@Author  ：mrProtein
@Date    ：2022/7/6
@Desc    :

先序遍历：中左右
中序遍历：左中右
后序遍历：左右中

非递归遍历：压栈

"""

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BTree(object):

    def __init__(self):
        self.head: Node = None

    def insert(self, val):
        if not self.head:
            self.head = Node(val)
            return
        h = self.head
        while h:
            if h.val < val:
                if h.right:
                    h = h.right
                else:
                    h.right = Node(val)
                    break
            else:
                if h.left:
                    h = h.left
                else:
                    h.left = Node(val)
                    break


    def f(self, node: Node):
        if not node:
            return
        self.f(node.left)
        print(node.val)
        self.f(node.right)

    def f2(self, node: Node):
        l = []
        l.append(node)
        while l:
            while node.left:
                node = node.left
                l.append(node)
            node = l.pop()
            print(node.val)
            if node.right:
                node = node.right
                l.append(node)

    def f3(self, node: Node):
        l = []
        # l.append(node)
        p = None
        while l or node:
            while node:
                l.append(node)
                node = node.left

            node = l[-1]
            if not node.right or node.right == p:
                print(node.val)
                l.pop()
                p = node
                node = None
            else:
                node = node.right



    def f1(self, node: Node):
        if not node:
            return
        l = []
        l.append(node)
        while len(l) > 0:
            n = l.pop()
            print(n.val)
            if n.right:
                l.append(n.right)
            if n.left:
                l.append(n.left)


    def f4(self, node: Node):
        l = []
        l.append(node)
        while l:
            node = l.pop()
            print(node.val)
            if node.right:
                l.append(node.right)
            if node.left:
                l.append(node.left)

    def f5(self, node: Node):
        l = [node]
        while l:
            while node and node.left:
                node = node.left
                l.append(node)
            node = l.pop()
            print(node.val)
            if node.right:
                l.append(node.right)
                node = node.right
            else:
                node = None

    def f6(self, node: Node):
        l = [node]
        pre = None
        while l:
            while node and node.left:
                node = node.left
                l.append(node)
            node = l[-1]
            if node.right and pre != node.right:
                node = node.right
                l.append(node)
            else:
                print(node.val)
                pre = node
                l.pop()
                node = None

    def f_z(self, node: Node):
        """
        非递归中序遍历，
        又右值的话把右值压入栈
        :param node:
        :return:
        """
        stack = [node]
        while stack:
            # 开始把所有的左节点node压入栈
            while node and node.left:
                node = node.left
                stack.append(node)
            node = stack.pop()
            # 没有左子树，打印
            print(node.val)
            if node.right:
                node = node.right
                stack.append(node)
            else:
                node = None

    def f_x(self, node: Node):
        """
        先序遍历，先打印出信息，然后将右压栈
        :param node:
        :return:
        """
        stack = [node]
        while stack:
            node = stack.pop()
            print(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def f_h(self, node: Node):
        """
        后续遍历，将左压栈，然后出战，看中间是否存在右子树，存在压栈，遍历上移的时候需要记录右，因为左右的顺序中右最后
        只要右存在则必定需要记录
        :param node:
        :return:
        """
        stack: list = [node]
        pre_right = None
        while stack:
            while node and node.left:
                node = node.left
                stack.append(node)
            node = stack[-1]
            if node.right and node.right != pre_right:
                node = node.right
                stack.append(node)
            else:
                print(node.val)
                pre_right = node
                stack.pop()
                node = None




if __name__ == '__main__':
    b = BTree()
    b.insert(100)
    b.insert(54)
    b.insert(99)
    b.insert(125)
    b.insert(41)
    b.insert(20)
    b.insert(120)
    b.insert(130)
    b.f_h(b.head)








