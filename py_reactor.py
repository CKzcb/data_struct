#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mrProtein 
@File    ：py_reactor.py
@Author  ：mrProtein
@Date    ：2022/7/8
@Desc    : 
"""

from twisted.internet import reactor, protocol


class WeChat(protocol.Protocol):
    """"""

    def dataReceived(self, data: bytes):
        print(data)
        self.transport.write("haode".encode())

    def connectionMade(self):
        print(self.transport)

    def connectionLost(self, reason):
        print(self.transport, reason)


class WeChatFactory(protocol.Factory):
    """"""
    protocol = WeChat

    def doStart(self):
        print("start ... ")

    def buildProtocol(self, addr):
        print("build ... ", addr)
        p = WeChat()
        p.factory = self
        return p


print("run .... ")
reactor.listenTCP(6699, WeChatFactory())
reactor.run()
