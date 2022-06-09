#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：simultaneously_porcess.py
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


进程：
    import multiprocessing

    底层机制：
        设置模式
        multiprocessing.set_start_method("fork"), 默认fork
        1、fork，拷贝所有资源，支持文件对象，线程锁等传参；unix，任意位置开始
        2、spawn，run参数传必备资源，不支持文件对象，线程锁等传参；Unix。win，main代码开始
            不会拷贝主进程的数据，只能通过参数传递
        3、forkserver，run参数传必备资源，不支持文件对象，线程锁等传参；Unix；main代码开始

    常见方法：
        p = multiprocessing.Process()
        p.start() 开始
        p.join() 等待当前进程的任务执行完成
        p.daemon = True
        p.name = "name" 设置名字

        os.getpid()

    python内置的进程间数据共享： 四种方式

        1、shared memory
            通过value和array，通过和c语言进行配合，

        2、Manager

        3、Queue

        4、pipes


    进程锁：多个进程共享同一个资源





"""

import multiprocessing

from multiprocessing import Process, Array, Value
from multiprocessing import Manager


def task():
    print(name)


def task_spawn(name):
    print(name)


def shared_memory_set(n: Value, a:Value):
    n.value = 20


def manager_set(d: dict, l: list):
    d["a"] = 2222
    l.append(44)


def queue_set(q: multiprocessing.Queue):
    q.put(1)
    q.put(12)
    q.put(13)
    q.put(14)


def pipes_set(p):
    p.send("adf")
    print(p.recv())



if __name__ == '__main__':
    name = []

    # fork
    # multiprocessing.set_start_method("fork")
    # p = multiprocessing.Process(target=task)
    # p.start()

    # spawn
    # multiprocessing.set_start_method("spawn")
    # p = multiprocessing.Process(target=task_spawn, args=(name, ))
    # p.start()

    # forkserver
    # multiprocessing.set_start_method("forkserver")
    # p = multiprocessing.Process(target=task_spawn, args=(name, ))
    # p.start()

    # cpu个数
    print(multiprocessing.cpu_count())

    # share memory
    # n = Value("i", 1)
    # a = Value("c")
    #
    # p = Process(target=shared_memory_set, args=(n, a))
    # p.start()
    # p.join()
    # print(n.value)

    # manager
    # with Manager() as manager:
    #     l = manager.list()
    #     d = manager.dict()
    #
    #     p = Process(target=manager_set, args=(d, l))
    #     p.start()
    #     p.join()
    #
    #     print(d)
    #     print(l)

    # queue
    # queue = multiprocessing.Queue()
    # p = multiprocessing.Process(target=queue_set, args=(queue,))
    # p.start()
    # p.join()
    #
    # print(queue.get())
    # print(queue.get())
    # print(queue.get())
    # print(queue.get())

    # pipes
    # f_p, s_p = multiprocessing.Pipe()
    # p = multiprocessing.Process(target=pipes_set, args=(s_p,))
    # p.start()
    #
    # print(f_p.recv())
    # f_p.send("h~")
    # p.join()





