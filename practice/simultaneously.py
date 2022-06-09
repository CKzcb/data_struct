#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：simultaneously.py
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


线程：
    threading.current_thread() 获取到当前线程
    t.start() 当前线程准备就绪，等待cpu调度，具体调度时间由cpu决定
    t.join() 等待当前线程的任务执行完毕之后再向下继续执行
    t.setDaemon() 守护线程，（必须放在start之前执行），
        t.setDaemon(True) 设置守护线程，主线程执行完毕后，子线程也主动关闭
        t.setDaemon(False) 设置非守护线程，主线程等待子线程执行完毕后主线程才结束（默认属性）
    t.setName() 为线程设置名字，应该在start之前设置，可以使用当前线程的getName()获取线程名字

    自定义线程类，需要继承threading.Thread，并实现run方法，在run方法中写具体要做的事情

    线程安全：
        t_lock = threading.RLock() 可以使用with
        t_lock.acquire() 加锁
        t_lock.release() 释放锁

        线程安全的内置类型：list->append/short/pop/extend, dict->赋值/update等

    线程锁：
        Lock 同步锁, 它是一个基本的锁对象，每次只能锁定一次，其余的锁请求，需等待锁释放后才能获取
        RLock 递归锁 （可以嵌套使用）可重入锁
        死锁：不同线程争夺同一把锁

    线程池：
        from concurrent.futures import ThreadPoolExecutor
        pool = ThreadPoolExecutor(3)    # 创建线程池，3个线程
        f = pool.submit(print_c, c) 开启任务，返回future对象，可以添加回调函数
        pool.shutdown(True) 主线程等待子线程执行完成后





"""
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# t_lock = threading.RLock()
t_lock = threading.Lock()
t_lock_1 = threading.Lock()

pool = ThreadPoolExecutor(3)  # 创建线程池，3个线程


def print_c(c: str):
    while True:
        # t_lock.acquire()
        # t_lock_1.acquire()
        time.sleep(random.random())
        print(threading.current_thread().getName(), c)
        # t_lock_1.release()
        # t_lock.release()


def pool_result():
    time.sleep(2)
    print(20)
    return 20


def pool_done(future):
    print(future.result())
    print("done .. ")


class MyThread(threading.Thread):
    """
    需要实现run方法
    """

    def run(self) -> None:
        while True:
            print(self._args)


lock_a = threading.Lock()
lock_b = threading.Lock()
lock_c = threading.Lock()


def show_a():
    while True:
        lock_c.acquire()
        print("a")
        time.sleep(0.1)
        lock_a.release()


def show_b():
    while True:
        lock_a.acquire()
        print("b")
        time.sleep(0.1)
        lock_b.release()


def show_c():
    while True:
        lock_b.acquire()
        print("c")
        time.sleep(0.1)
        lock_c.release()


if __name__ == '__main__':
    #############
    # t_l = []
    # 1、创建线程
    # for c in ["a", "b", "c"]:
    #     # 函数处理
    #     t = threading.Thread(target=print_c, args=(c, ))
    #     # 自定义类处理
    #     # t = MyThread(args=(c,))
    #     t.setName("it`s_{}".format(c))
    #     t_l.append(t)
    #
    # for t in t_l:
    #     # 2、启动
    #     t.start()
    # for t in t_l:
    #     # 3、等待
    #     t.join()
    # for c in ["a", "b", "c"]:
    #     pool.submit(print_c, c)

    # future = pool.submit(pool_result)
    # future.add_done_callback(pool_done)
    # pool.shutdown(True)

    t_a = threading.Thread(target=show_a)
    t_b = threading.Thread(target=show_b)
    t_c = threading.Thread(target=show_c)

    lock_a.acquire()
    lock_b.acquire()

    t_a.start()
    t_b.start()
    t_c.start()

    t_a.join()
    t_b.join()
    t_c.join()
