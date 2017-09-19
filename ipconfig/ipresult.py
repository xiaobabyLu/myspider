# -*- coding:utf-8 -*-
import time

import MysqlConn
import ipanalysis


def get_ip():

    try:
        sql = "select ip from iptables where staticdate>= %s"
        result = mysqlconn.query_all(sql,time.strftime("%Y-%m-%d",time.localtime(int(time.time()))))
    except Exception as e:
        print(e)
    finally:
        return result


if __name__ == '__main__':
    mysqlconn = MysqlConn.MySqlConn()
    iplist = list(get_ip())
    ipinfoList = []
    for ip in iplist:
        ipinfo = ipanalysis.ip_analysis(ip['ip'])
        if ipinfo == 0:
            continue
        else:
            ipinfoList.append(ipinfo)
    # print ipinfoList
    insertsql = 'insert into ipinfo VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    mysqlconn.insert_many(insertsql,ipinfoList)
    mysqlconn.dispose()
