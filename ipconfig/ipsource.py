# -*- coding: utf-8 -*-

"""
    Created on 2017-09-16
    @Author : Bruce Lu
    @Desc : catch ip
"""


from bs4 import BeautifulSoup
import requests
import MysqlConn

# 'ascii' codec can't encode characters in position ，fixed coding问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 主要是验证拉，sleep暂停
import time

url_list = []
ip_list = []

# 获取该网站的可获取ip的urls,并且生成固定格式list
def getUrls(url):
    pages = ['1.html','2.html', '3.html', '4.html', '5.html']
    r = requests.get(url)
    content = r.content.decode('gbk')
    soup = BeautifulSoup(content,'html.parser')
    for index, k in enumerate(soup.find_all('table')[1].find_all('a')):
        if index != 0:
            for page in pages:
                url_list.append({'name' : k.string, 'url': r'http://www.66ip.cn'+k['href'].replace('1.html',page)})
        else:
            for page in pages:
                url_list.append({'name': k.string, 'url': k['href']+r'/'+page})


def getIpList(name,url):
    fd = requests.get(url)
    content = fd.content
    soup = BeautifulSoup(content,'html.parser')
    for index, tr in enumerate(soup.find_all('table')[2].find_all('tr')):
        if index != 0:
            td = tr.find_all('td')
            # ip_list.append({'来源': name, 'ip': td[0].contents[0],'端口号': td[1].contents[0], '代理位置': td[2].contents[0],
            #                 '代理类型': td[3].contents[0], '验证时间': td[4].contents[0]})
            ip_list.append((name, td[0].contents[0],td[1].contents[0], td[2].contents[0],td[3].contents[0],td[4].contents[0]))
            # print ip_list
            # time.sleep(100)

getUrls('http://www.66ip.cn/')
for url in url_list:
    getIpList(url['name'],url['url'])
# getIpList('test',r'http://www.66ip.cn/')
myconn =MysqlConn.MySqlConn()

sql =  'insert into spider.ipagent VALUES (%s,%s,%s,%s,%s,%s)'

print myconn.insert_many(sql,ip_list)

myconn.dispose()