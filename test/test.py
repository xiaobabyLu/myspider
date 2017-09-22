# -*- coding:utf8 -*-

import urllib2
import re
import time
import random
import threading
import string

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Hosts': 'hm.baidu.com',
    'Referer': 'http://www.xicidaili.com/nn',
    'Connection': 'keep-alive'
}


def test(i):
    print "bid=%s" % "".join(random.sample(string.ascii_letters + string.digits, 11))
    print '开始第:'+ str(i)


if __name__ == "__main__":
    for n in range(1,10):
        thread = []
        print '------------------第 '+str(n)+' 批次开始执行------------------'
        for i in range(n*10,n*10+10):

            t = threading.Thread(target=test,args=(i,))
            thread.append(t)

        for i in range(1,10):
            thread[i].start()

        for i in range(1,10):
            thread[i].join()
