#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：simultaneously_coroutine.py
@Author  ：mrProtein
@Date    ：2022/6/9
@Desc    :

并发
1、多机器
2、多线程： Thread(threading)
    优点：相比进程，更轻量级，占用资源少
    缺点：相比进程，多线程只能并发执行，不能利用多核cpu（GIL）
          相比协程，启动数目有限制，占用系统资源，有线程切换开销
    适用于：IO密集型运算，同时运行的任务数目要求不多

3、多进程： Process(multiprocessing)
    优点：可以利用多核cpu并行计算
    缺点：占用资源最多、可启动数目比线程少
    适用于：CPU密集型运算

4、协程: coroutine(asyncio)
    优点：内存开销最少，启动协程数量少
    缺点：支持的库少
    适用于：IO密集型运算，需要超多任务进行

io密集型
计算密集型

选择：
    1、CPU密集型：多进程
    2、IO密集型：任务量大？协程：线程

GIL（全程解释器锁）：同步线程的一种机制，即使多核同一时间也只能执行一个线程
    当线程执行时会获取GIL，当遇到IO时释放GIL

    存在GIL的原因：为了解决多线程之间数据完整性和状态同步的问题：python对象的引用计数


协程：微线程，是一种用户态内的上下文切换技术，



"""

import asyncio


async def f1():
    print(1)
    await asyncio.sleep(3)
    print(2)


async def f2():
    print(3)
    await asyncio.sleep(3)
    print(4)


if __name__ == '__main__':
    tasks = [
        asyncio.ensure_future(f1()),
        asyncio.ensure_future(f2()),
    ]

    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.wait(tasks))







