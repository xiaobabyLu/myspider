# -*- coding:utf-8 -*-

"""
    Created on 2017-09-17
    @Author : Bruce Lu
    @Desc : Analysis sku data
"""

import os
import MysqlConn
import ProductSku

s = os.sep
root = unicode("d:" + s + "桌面" + s + "爬虫" + s , 'utf-8')
# 获取sku目录列表
fileList = ProductSku.get_file(os.path.join(root,'bevol-detial'+s))

# print os.path.join(root,'bevol-detial'+s)
#
# print fileList

# 创建数据库连接实例
myconn =MysqlConn.MySqlConn()
# 获取entity对应字段信息，解析json字符串
# resultList = get_entity(fileList)
# 插入entity表数据,批量执行
# sql = 'insert into product.sku_entity VALUES (%s, %s, %s, %s, %s,%s, %s, ' \
#       '%s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)'
# print myconn.insert_many(sql,resultList)

# # 获取goods对应字段信息
# resultList = get_goods(fileList)
# # 插入goods表数据，批量执行
# sql = "insert into product.sku_goods VALUES (%s, %s, %s, %s, %s,%s,%s, %s, %s, %s, " \
#       "%s,%s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s,%s)"
# print myconn.insert_many(sql,resultList)

# # 获取doyen相关信息
# resultList = get_doyen(fileList)
# # 插入doyen表信息
# sql ="insert into product.sku_doyen VALUES (%s, %s, %s, %s, %s,%s,%s, %s, %s)"
# print myconn.insert_many(sql,resultList)

# 获取doyen相关信息
# resultList = ProductSku.get_goodsext(fileList)
# 插入doyen表信息
# sql ="insert into product.sku_goodsext VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
# print myconn.insert_many(sql,resultList)

# # 获取useds相关信息
# resultList = ProductSku.get_composition(fileList)
# # 插入useds表信息
# sql ="insert into product.sku_composition VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s," \
#      " %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"
# print myconn.insert_many(sql,resultList)

# # 获取useds相关信息
# resultList = ProductSku.get_compo_used(fileList)
# # 插入useds表信息
# sql ="insert into product.sku_composition_useds VALUES (%s, %s)"
# print myconn.insert_many(sql,resultList)


# # 获取effect相关信息
# resultList = ProductSku.get_effect(fileList)
# # 插入effect表信息
# sql ="insert into product.sku_effect VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
# print myconn.insert_many(sql,resultList)

# 获取safety相关信息
# resultList = ProductSku.get_safety(fileList)
# # print resultList
# # 插入safety表信息
# sql ='insert into product.sku_safety VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)'
# print myconn.insert_many(sql,resultList)

myconn.dispose()
