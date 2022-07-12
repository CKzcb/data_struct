from threading import Thread, Lock

l1 = Lock()
l2 = Lock()
l3 = Lock()


def p1():
    while True:
        l1.acquire()
        print("p1 ...")

        l2.release()


def p2():
    while True:
        l2.acquire()
        print("p2 ... ")
        l3.release()


def p3():
    while True:
        l3.acquire()
        print("p3 ... ")
        l1.release()


if __name__ == '__main__':
    l2.acquire()
    l3.acquire()

    t1 = Thread(target=p1)
    t2 = Thread(target=p2)
    t3 = Thread(target=p3)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
