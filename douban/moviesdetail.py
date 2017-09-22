# -*- coding : utf-8 -*-

import urllib2
import sys
import threading
import requests
from multiprocessing import Pool,Lock
import os
import Queue
import time
import randomheader
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')



def getMovieInfo():
    line = fr.readline()
    line = line.split(';')
    movieid = line[0]
    title = line[1]
    rate = line[2]
    url = line[3]
    # movieInfo.append((movieid,title,rate,url,randomheader.randHeader(),randomheader.randProxy()))
    return (movieid,title,rate,url,randomheader.randHeader(),randomheader.randProxy())


def get_moviedetail(movieInfo):
    movieid = movieInfo[0]
    title = movieInfo[1]
    rate = movieInfo[2]
    url = movieInfo[3]
    header = movieInfo[4]
    proxy = movieInfo[5]
    try:
        proxyHandler = urllib2.ProxyHandler(proxy)
        opener = urllib2.build_opener(proxyHandler)
        request = urllib2.Request(url,headers=header)
        content = opener.open(request).read()

        soup = BeautifulSoup(content,'html.parser')
        info = soup.select('#info')[0]
        result = info.get_text().split('\n')

        director = result[1].split(':')[1].strip()
        scriptwriter = result[2].split(':')[1].strip()
        actor = result[3].split(':')[1].strip()
        category = result[4].split(':')[1].strip()
        district = result[5].split(':')[1].strip()
        language = result[6].split(':')[1].strip()
        showtime = result[7].split(':')[1].strip()
        duration = result[8].split(':')[1].strip()
        alias = result[9].split(':')[-1].strip()
        description = soup.find_all("span", attrs={"property": "v:summary"})[0].get_text()
        description = description.lstrip().lstrip('\n\t').rstrip().rstrip('\n\t').replace('\n', '\t')

        record = str(movieid) + ',\t' + title + ',\t' + str(rate) + ',\t' + url + ',\t' + director.encode('utf8') + ',\t' + \
                  scriptwriter.encode('utf8') + ',\t' + actor.encode('utf8') + ',\t' + category.encode('utf8') + ',\t' + \
                  district.encode('utf8') + ',\t' + language.encode('utf8') + ',\t' + showtime.encode('utf8') + ',\t' + \
                  duration.encode('utf8') + ',\t' + alias.encode('utf8') + ',\t' + description.encode('utf8') + '\n'
        # lock.acquire()
        fw = open('movie_detail.txt', 'a')
        fw.write(record)
        fw.close()
        # lock.release()
        print title + '\t -----success------'
    except Exception as e:
        print e
        print title+ '\t error'


def working(movieInfo):
    while True:
        arguments = q.get()
        get_moviedetail(movieInfo)
        time.sleep(3)
        q.task_done()
# def init(l):
#     global lock
#     lock = l


if __name__ == '__main__':
    inputfile = 'douban_movie.txt'
    fr = open(inputfile, 'r')
    num = len(fr.readlines())
    fr.close()

    movieInfo = []

    fr = open(inputfile, 'r')
    for i in range(num):
        result = getMovieInfo()
        get_moviedetail(result)
        time.sleep(3)
    fr.close()

    # use muti queue
    q = Queue()
    thread_num = 2
    job_num = num
    for i in range(thread_num):
        t = threading.Thread(target=working, args=movieInfo)
        t.setDaemon(True)
        t.start()

    for i in range(job_num):
        q.put(i)
    q.join()

    # pool multi process
    # fr = open(inputfile, 'r')
    # for i in range(num):
    #     getMovieInfo()
    # fr.close()
    #
    # for info in movieInfo:
    #     get_moviedetail(info)
    #     time.sleep(3)
    # print movieInfo
    # lock = Lock()
    # pool = Pool(2, initializer=init, initargs=(lock,))
    #
    # pool.map(get_moviedetail, movieInfo)
    #
    # pool.close()
    # pool.join()

    # threading multi threads
    # lock = threading.Lock()
    # thread_list =[]
    # for i in range(num):
    #     threads = threading.Thread(target=get_moviedetail,name=('thread %s' % i))
    #     thread_list.append(threads)
    #     threads.start()
    #
    # for t in thread_list:
    #     t.join()
    #
    # fr.close()
    # fw.close()
