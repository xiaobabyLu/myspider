# -*- coding: utf-8 -*-
from multiprocessing.dummy import Pool as ThreadPool,Lock

import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def init(l):
    global lock
    lock = l


def spider(url):

    lock.acquire()
    print '---------------------\n'
    print url[0]
    print url[1]
    lock.release()

    # print url


if __name__ == "__main__":
    lock = Lock()
    pool = ThreadPool(2,initializer=init, initargs=(lock,))
    f = open('content.txt', 'a')
    page = []
    for i in range(1, 21):
        page.append((i,i+1))

    results = pool.map(spider, page)
    pool.close()
    pool.join()
    f.close()
    print results