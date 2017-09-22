# -*- coding:utf-8 -*-
import urllib2
import threading
import os

filepath = os.path.split(os.path.realpath(__file__))[0]
infile = open(os.path.join(filepath,'proxy.txt'),'r')
outfile = open('validproxy.txt','w')
url ='https://www.baidu.com'

lock = threading.Lock()
cookies = urllib2.HTTPCookieProcessor()


def ip_valid():
    try:
        lock.acquire()
        line = infile.readline()
        protocol,ip,port=line.split('\t')
        lock.release()
    except Exception as e:
        print e
        print '没有数据可以读取了...'

    try:
        proxyHandler = urllib2.ProxyHandler({protocol.lower():r'http://%s:%s'%(ip,port)})
        opener = urllib2.build_opener(cookies, proxyHandler)
        opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')]
        rd = opener.open(url,timeout=5).read()
        if len(rd)>1000:
            lock.acquire()
            print 'add proxy' ,ip ,port
            outfile.write(protocol +'\t' +ip+'\t'+port+ '\n')
            lock.release()
        else:
            print 'ip出现异常或者验证过期'
    except Exception as e:
        print e


num = len(open(infile,'r').readlines())
thread_list =[]
for i in range(num):
    threads = threading.Thread(target=ip_valid,name=('thread %s' % i))
    thread_list.append(threads)
    threads.start()

for t in thread_list:
    t.join()

infile.close()
outfile.close()