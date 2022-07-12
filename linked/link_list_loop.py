#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：link_list_loop.py
@Author  ：mrProtein
@Date    ：2022/7/6
@Desc    :

判断链表是否有环: 1.快慢指针，2.额外空间 hash表

获取入环的节点：1.快慢指针相遇之后，快指针从头部开始走一步一步走，慢指针一步一步走，相遇则是

判断两个链表是否有交集：1.先判断有无相交，当相交的时候判断两个长度，快慢指针先走差值，最后在交点处


两个链表有环三种情况（见图片）
1.各自成环不想交
2.相交与成环之前一点
3.相交与环上，两点

"""

class Node(object):

    def __init__(self, val: int):
        self.val = val
        self.next = None

def is_intersect(head: Node):
    """"""
    # 两个链表遍历，记录最后节点




def is_loop(head: Node) -> bool:
    """
    判断是否有环
    :param head:
    :return:
    """
    ptr1 = head
    ptr2 = head
    is_l = False

    while ptr2 and ptr1:
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next if ptr2.next else ptr2.next
        # print(ptr1.val, ptr2.val)
        if ptr1 and ptr2 and ptr1 == ptr2:
            is_l = True
            break

    if is_l:
        ptr2 = head
        while ptr2 != ptr1:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        print(ptr2.val)

    return is_l


if __name__ == '__main__':
    head = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)
    head.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = n9
    # n9.next = None
    n9.next = n6

    print(is_loop(head))



