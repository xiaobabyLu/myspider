# -*- coding: utf-8 -*-
'''
    Created  on 2017-09-15
    @Author : Bruce Lu
    @Desc : test
'''
import MysqlConn

mysqlconn = MysqlConn.MySqlConn()

print 1111
sqlall = 'select * from iptables'

sql_insert = 'insert into iptables(ip,staticdate) VALUES (%s,%s)'

values =[('172.1.0.10','2017-09-15'),('172.1.33.10','2017-09-16')]

result = mysqlconn.query_all(sqlall)

print mysqlconn.insert_many(sql_insert,values)

print result

mysqlconn.dispose()
