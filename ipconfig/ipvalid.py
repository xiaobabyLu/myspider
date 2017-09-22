# -*- coding : utf-8 -*-

import urllib2
import time
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

print sys.getdefaultencoding()

xici_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Hosts': 'hm.baidu.com',
    'Referer': 'http://www.xicidaili.com/nn',
    'Connection': 'keep-alive'
}
baidu_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
              'Connection':'keep-alive',
              'Referer':'https://www.baidu.com/',
              'Accept-Encoding':'gzip, deflate, br',
              'Accept-Language':'zh-CN,zh;q=0.8'
              # 'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3'

              }
req_timeout = 5
testUrl = 'https://www.douban.com/'
testStr = 'douban'

cookies = urllib2.HTTPCookieProcessor()
checked_num =0
grasp_num =0

file = open(r'douban_proxy.txt','a')

for page in range(1,10):
    req = urllib2.Request('http://www.xici.net.co/nn/'+str(page),None,xici_headers)
    html_doc = urllib2.urlopen(req,timeout=req_timeout).read()
    soup = BeautifulSoup(html_doc,'html.parser')
    trs = soup.find('table',id = 'ip_list').find_all('tr')
    # print trs[1:]
    for tr in trs[1:]:
        tds = tr.find_all('td')
        ip = tds[1].text.strip()
        port = tds[2].text.strip()
        location = tds[3].text.strip()
        ishidden = tds[4].text.strip()
        protocol = tds[5].text.strip()
        if protocol =='HTTP' or protocol == 'HTTPS':
            print '%s = %s : %s' % (protocol,ip,port)
            grasp_num += 1
            proxyHandler = urllib2.ProxyHandler({'http':r'http://%s:%s' % (ip,port)})
            opener = urllib2.build_opener(cookies,proxyHandler)
            opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')]

            try:
                print 1111
                req = opener.open(testUrl,timeout=req_timeout)
                print 2222
                result = req.read()
                print 3333
                print result
                pos = result.find(testStr)
                if pos>1:
                    file.write(protocol+'\t'+ip+'\t'+port+'\n')
                    file.flush()
                    checked_num += 1
                    print checked_num,grasp_num
                else:
                    print 'forbbidon'
                    continue
            except Exception as e:
                continue
file.close()
print checked_num,grasp_num