#!/usr/local/bin/python

# Describe : multi thread


import random
import time, threading

######################################################################################

def thread_run(urls):
    print("Current %s is running..." % threading.current_thread().name)
    for url in urls:
        print("%s ----->>> %s" % (threading.current_thread().name, url))
        time.sleep(random.random())
    print("%s ended." % threading.current_thread().name)

def CreateThreadMethod1():
    print("%s is running...." % threading.current_thread().name)
    t1 = threading.Thread(target=thread_run, name='Thread_1', args=(['url1','url2','url3'],))
    t2 = threading.Thread(target=thread_run, name='Thread_2', args=(['url4','url5','url6'],))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("%s ended." % threading.current_thread().name)

######################################################################################

class MyThread(threading.Thread):
    def __init__(self, name, urls):
        threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print("Current %s is running..." % threading.current_thread().name)
        for url in self.urls:
            print("%s ----->>> %s" % (threading.current_thread().name, url))
            time.sleep(random.random())
        print("%s ended." % threading.current_thread().name)

def CreateThreadMethod2():
    print("%s is running...." % threading.current_thread().name)
    t1 = MyThread(name='Thread_1', urls = ['url1','url2','url3'],)
    t2 = MyThread(name='Thread_2', urls = ['url4','url5','url6'],)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("%s ended." % threading.current_thread().name)

######################################################################################

num = 0
myLock = threading.RLock()

class TestLockThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global num
        while True:
            myLock.acquire()
            print("%s locked, Number = %d" % (threading.current_thread().name, num))
            if num >= 4:
                myLock.release()
                print("%s released, Number = %d" % 
                      (threading.current_thread().name, num))
                break
            num+=1
            print("%s released, Number = %d" % 
                  (threading.current_thread().name, num))
            myLock.release()

def TestLock():
    thread1 = TestLockThread('Thread_1')
    thread2 = TestLockThread('Thread_2')
    thread1.start()
    thread2.start()
