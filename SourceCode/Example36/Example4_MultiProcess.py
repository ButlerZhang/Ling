#!/usr/local/bin/python

# Describe : multi processes

import os
import time
import random
from multiprocessing import Queue, Process, Pool, Pipe

######################################################################################

def Fork():
    print("current process(%s) start..." % os.getpid())
    pid = os.fork()             #only use in Linux/Unix
    if pid < 0:
        print("error in fork")
    elif pid == 0:
        print("I am child process(%s) and my parent process is (%s)",
              (os.getpid(), os.getppid()))
    else:
        print("I(%s) created a child process(%s)." % (os.getpid(), pid))

######################################################################################

def runProcess(name, data):
    print("Child process %s (%s) running..." % (name, os.getpid()))
    print("data = " + data)

###multiprocessing.Process must write in "if __name__ == '__main__'"
#if __name__ == '__main__':
#    print("Parent process %s." % os.getpid())
#    for i in range(5):
#        p = Process(target=runProcess, args=(str(i), "hello"))
#        print("Process will start.")
#        p.start()
#    p.join()
#    print("Process end.")

######################################################################################

def runTask(name):
    print("Task %s (pid = %s) is running..." % (name, os.getpid()))
    time.sleep(random.random() * 5)
    print("Task %s end." % name)

#if __name__ == '__main__':
#    print("Current process %s." % os.getpid())
#    p = Pool(processes=3)
#    for i in range(5):
#        p.apply_async(E4.runTask, args=(i,))
#    print("Waiting for all task done...")
#    p.close()
#    p.join()
#    print("All task done.")

######################################################################################

def proc_write(q, urls):
    print("Process(%s) is writing..." % os.getpid())
    for url in urls:
        q.put(url)
        print("Put %s to queue..." % url)
        time.sleep(random.random())

def proc_read(q):
    print("Process(%s) is reading..." % os.getpid())
    while True:
        url = q.get(True)
        print("Get %s from queue." % url)

#if __name__ == '__main__':
#    q = Queue()
#    proc_writer1 = Process(target=proc_write, args=(q,['url1','url2','url3']))
#    proc_writer2 = Process(target=proc_write, args=(q,['url4','url5','url6']))
#    proc_reader = Process(target=proc_read, args=(q,))

#    proc_writer1.start()
#    proc_writer2.start()
#    proc_reader.start()

#    proc_writer1.join()
#    proc_writer2.join()

#    proc_reader.terminate()

######################################################################################

def proc_send(pipe, urls):
    for url in urls:
        print("Process (%s) send: %s" % (os.getpid(), url))
        pipe.send(url)
        time.sleep(random.random())

def proc_recv(pipe):
    while True:
        print("Process (%s) rev: %s" % (os.getpid(), pipe.recv()))
        time.sleep(random.random())

#if __name__ == '__main__':
#    pipe = Pipe()
#    p1 = Process(target=E4.proc_send, args=(pipe[0], ['url_'+str(i) for i in range(10)]))
#    p2 = Process(target=E4.proc_recv, args=(pipe[1],))
#    p1.start()
#    p2.start()
#    p1.join()
#    p2.join()
