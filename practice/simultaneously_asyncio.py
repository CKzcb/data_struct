#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：simultaneously_asyncio.py
@Author  ：mrProtein
@Date    ：2022/6/9
@Desc    :

协程：不是计算机提供的，而是人提供的，又称为微线程，用户态上下文切换的技术

1.greenlet
2.yield
3.asyncio
4.async/await


    await后面三种可等待对象：协程对象、Future、Task对象->IO等待


Task对象：在事件循环中添加多个任务

asyncio.create_task(协程对象)创建协程任务Task对象
ensure_future()


Future: task继承future





"""
import asyncio
# asyncio 3.4 之后


async def task():
    print("gogogo...")
    await asyncio.sleep(2)
    print("done .. ")


async def task_1():
    print("task_1 ... ")
    await asyncio.sleep(1)
    print("done 1 ... ")



async def main():
    """"""
    print("start main ... ")
    t = asyncio.create_task(task())
    t1 = asyncio.create_task(task_1())

    print("main end ... ")
    ret1 = await t
    ret2 = await t1



async def main1():
    t_l = [
        asyncio.create_task(task()),
        asyncio.create_task(task_1())
    ]

    done, _ = await asyncio.wait(t_l)
    for t in done:
        print(t.get_loop())


if __name__ == '__main__':
    asyncio.run(main1())