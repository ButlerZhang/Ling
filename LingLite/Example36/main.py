import sys
print(sys.version)
print('\n')

g_sourceFileName = r"DataSource//Naughty Brother.txt"
g_resultFileName1 = r"ResultFiles//result1.txt"
g_resultFileName2 = r"ResultFiles//result2.txt"

import os
import Example6_Coroutine as E6
from gevent.pool import Pool

from gevent import monkey
monkey.patch_all()
import gevent



if __name__ == "__main__":
    pool = Pool(2)
    urls = [r"https://github.com/", r"https://www.python.org/", r"http://www.cnblogs.com/"]
    results = pool.map(E6.run_task, urls)
    print(results)
