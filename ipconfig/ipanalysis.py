# -*- coding:utf-8 -*-
import urllib
import json
# import pandas as pd


def ip_analysis(ip):
    url = "http://ip.taobao.com//service/getIpInfo.php?ip=" + ip
    html = urllib.urlopen(url).read().decode('utf-8')
    jsondata = json.loads(html)
    # print jsondata['data']
    if jsondata['code'] == 1:
        return 0
    else:
        return (jsondata['data']['ip'],jsondata['data']['country'],jsondata['data']['area'],jsondata['data']['region'],
                jsondata['data']['city'],jsondata['data']['county'],jsondata['data']['isp'],jsondata['data']['country_id'],
                jsondata['data']['area_id'],jsondata['data']['region_id'],jsondata['data']['city_id']
                ,jsondata['data']['county_id'],jsondata['data']['isp_id']
                )
