# -*- coding:utf-8 -*-

"""
    Created on 2017-09-17
    @Author : Bruce Lu
    @Desc : Analysis sku data
"""

import os
import json
import MysqlConn


s = os.sep
rootpath = unicode("d:" + s + "桌面" + s + "爬虫" + s,'utf-8')

file = os.path.join(rootpath,r'bevol-sku.json\bevol-sku.json')

fd = open(file).read()

lines = json.loads(fd)

prdList =[]

for i in lines:
    if len(i['cps_search'])>2000:
        print
    prdList.append((i['hit_num'],i['remark'],i['alias'],i['brand_id'],i['approval'],i['image'],i['tstamp'],i['remark3'],i['id'],
                   i['index_name'],i['title'],i['tag_ids'],i['category'],i['price'],i['cps_search'],i['c_sort'],i['data_type'],
                   i['safety_1_num'],i['capacity'],i['comment_num'],i['grade'],i['like_num'],i['mid'],i['hidden_skin'],i['alias_2']))

mysqlconn = MysqlConn.MySqlConn()

insertsql = 'insert into product.productdetail VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

print mysqlconn.insert_many(insertsql,prdList)

mysqlconn.dispose()