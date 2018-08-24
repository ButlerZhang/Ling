import sys
print(sys.version)
print('\n')

g_sourceFileName = r"DataSource//Naughty Brother.txt"
g_resultFileName1 = r"ResultFiles//result1.txt"
g_resultFileName2 = r"ResultFiles//result2.txt"

import os
from multiprocessing import Queue, Process, Pool, Pipe
import Example5_MultiThread as E5

#E5.CreateThreadMethod1()
#E5.CreateThreadMethod2()
E5.TestLock()