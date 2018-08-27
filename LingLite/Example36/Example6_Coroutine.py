#!/usr/local/bin/python

# Describe : Coroutine



from gevent import monkey
from gevent.pool import Pool
monkey.patch_all()
import gevent
import urllib.request


######################################################################################

def run_task(url):
    print("Visit --> %s" % url)
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        print("%d bytes received from %s." % (len(data), url))
        #print(data)
    except Exception as e:
        print(e)
    return ("url:%s ---> finish" % url)

######################################################################################

#if __name__ == "__main__":
#    urls = [r"https://github.com/", r"https://www.python.org/", r"http://www.cnblogs.com/"]
#    greenlets = [gevent.spawn(E6.run_task, url) for url in urls ]
#    gevent.joinall(greenlets)

######################################################################################

#if __name__ == "__main__":
#    pool = Pool(2)
#    urls = [r"https://github.com/", r"https://www.python.org/", r"http://www.cnblogs.com/"]
#    results = pool.map(run_task, urls)
#    print(results)
