# -*- coding:utf-8 -*-
import pymysql


# 数据库连接设置
# class MysqlConn:
conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,          # 不要使用str 如果改源码也可以
        user='root',
        password='111111',
        db='spider',
        charset='utf8',     # 根据数据库进行设定
                           )
# 选择使用的数据库
conn.select_db('spider')
try:
        # 获取游标，并且设置别名，可以多次使用
    with conn.cursor() as cursor:
        # 游标设置为字典类型
        # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 设置sql语句字符串，可以设置参数
        sql = 'select * from test where id = %s'
        # 游标执行语句
        cursor.execute(sql, 10)
        # 获取查询结果fetchone查询一条 fetchall查询所有
        #  result = cursor.fetchone()
        result = cursor.fetchall()
        print(result)

# 异常抛出
except Exception as e:
    print(e)
else:
    # 查询可以不用执行，增删改需要commit.
    conn.commit()
    print("查询成功 : ", cursor.rowcount)
finally:
    # 关闭数据库连接
    conn.close()
