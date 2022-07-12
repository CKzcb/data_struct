
def g1():
    c = 1
    while 1:
        print("g1.. ", c)
        c = yield

def g2():
    c = 1
    while 1:
        print("g2 .. ", c)
        c = yield


def main():
    c1 = g1()
    c2 = g2()
    c1.__next__()
    c2.__next__()
    c1.send(22)
    c2.send(11)

if __name__ == '__main__':
    main()

