import sys
print(sys.version)
print('\n')

g_sourceFileName = r"DataSource//Naughty Brother.txt"
g_resultFileName1 = r"ResultFiles//result1.txt"
g_resultFileName2 = r"ResultFiles//result2.txt"

import os
from multiprocessing import Queue, Process, Pool, Pipe
import Example4 as E4


if __name__ == '__main__':
    pipe = Pipe()
    p1 = Process(target=E4.proc_send, args=(pipe[0], ['url_'+str(i) for i in range(10)]))
    p2 = Process(target=E4.proc_recv, args=(pipe[1],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()