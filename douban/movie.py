# -*- coding : utf-8 -*-

import json
import urllib2

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

headers = { }
headers["Accept"] = "*/*"
headers["Accept-Encoding"] = "gzip, deflate, br"
headers["Accept-Language"] = "zh-CN,zh;q=0.8"
headers["Connection"] = "keep-alive"
headers["Cookie"] = 'bid=KPtmGemzlg0; ll="118172"; __yadk_uid=WYIgYwQR1VPgD109pwS82hGo9fGTpM1m; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1505893178%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DMxZ5dy19LmoPiL5fDhbq8xeZiTJAJ3EQlrMH7Mc-UaQo7c9c6vgrY7VkjyLL3X0_%26wd%3D%26eqid%3De4aa17aa0000ce790000000659c1d8bc%22%5D; _pk_id.100001.4cf6=ae13b25c505c0988.1505876114.4.1505893178.1505890762.; _pk_ses.100001.4cf6=*; __utma=30149280.1960989146.1490509283.1505889151.1505893178.13; __utmb=30149280.0.10.1505893178; __utmc=30149280; __utmz=30149280.1505876114.10.10.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1266377649.1505876114.1505889151.1505893178.4; __utmb=223695111.0.10.1505893178; __utmc=223695111; __utmz=223695111.1505876114.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic'
headers["Host"] = "movie.douban.com"
headers["Referer"] = "http://movie.douban.com/"
headers["Upgrade-Insecure-Requests"] = 1
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"


url = 'https://movie.douban.com/j/search_tags?type=movie'


request = urllib2.Request(url)
content = urllib2.urlopen(request).read()
tags = json.loads(content)['tags']


outputFile = 'douban_movie.txt'
fw = open(outputFile, 'w')
fw.write('movieid;title;rate;url;is_new;playable;cover\n')


for tag in tags:
    start = 0
    while True:
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag='+ tag +'&page_limit=20&page_start=' + str(start)
        request = urllib2.Request(url)
        content = urllib2.urlopen(request).read()
        movies = json.loads(content)['subjects']
        if len(movies) == 0:
            break
        for movie in movies:
            movieid = movie['id']
            title = movie['title']
            rate = movie['rate']
            url = movie['url']
            is_new = movie['is_new']
            playable = movie['playable']
            cover = movie['cover']
            record = str(movieid) + ';' + title+';' + str(rate) + ';' + url + ';' + str(is_new) + ';' + str(playable) + ';' + cover + '\n'
            fw.write(record.encode('utf-8'))
            print tag + '\t' + title + '\t' + rate
        start += 20
fw.close()