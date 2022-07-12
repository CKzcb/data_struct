from kazoo.client import KazooClient
import time
import uuid
my_id = uuid.uuid4()

def leader_func():
    print("I am the leader {}".format(str(my_id)))
    while True:
        print("{} is working! ".format(str(my_id)))
        time.sleep(3)

zk = KazooClient(hosts='49.233.27.128:12181,49.233.27.128:12182,49.233.27.128:12183,49.233.27.128:12184')
zk.start()

election = zk.Election("/electionpath")

# blocks until the election is won, then calls
# leader_func()
election.run(leader_func)
print("mmmm")