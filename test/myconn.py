# -*- coding : utf-8 -*-


import pymysql


#  数据库连接方法，返回数据库连接实例
def get_connect():
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,  # 不要使用str 如果改源码也可以
        user='root',
        password='111111',
        db='spider',
        charset='utf8',  # 根据数据库进行设定
    )
    return conn


# 定义一个方法去处理查询,对数据结果进行操作
def outputList(conn):
    resultList = []
    try:
        with conn.cursor() as cursor:
            sql = 'select * from test where id >= %s'
            # 游标执行语句
            cursor.execute(sql, 1)
            result = cursor.fetchall()
            for row in result:
                resultList.append(row[1])
    except Exception as e:
        print(e)
    finally:
        # 可以返回也可以打印
        # return resultList
        print(resultList)


# 对数据进行批量操作 1、循环操作
def cycleInsert(conn):
    result = 0
    values = [{"id":1, "name":"lulu", "desc":"beauty"}, {"id":2, "name": "xiaohei", "desc": "black"},
              {"id":3, "name":"wang", "desc": "lovely"}]
    try:
        conn.select_db('spider')
        with conn.cursor() as cursor:
            for value in values:
                sql = "INSERT INTO spider.test (id,name,test.desc) VALUES ( %s, %s, %s);"
                cursor.execute(sql,(int(value["id"]), value["name"], value["desc"]))
                result += 1
                conn.commit()
            print('本次更新一共影响：', result, '行数据')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# 对数据进行批量操作 1、循环操作
def multiInsert(conn):
    values = [{"id":6, "name":"lulu", "desc":"beauty"}, {"id":7, "name": "xiaohei", "desc": "black"},
              {"id":8, "name":"wang", "desc": "lovely"}, {"id":9, "name":"wang", "desc": "lovely"}]
    items = []
    for value in values:
        items.append([value["id"],value["name"],value["desc"]])
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO spider.test (id,name,test.desc) VALUES ( %s, %s, %s)"

            cursor.executemany(sql, items)
            conn.commit()
            print(cursor.rowcount)
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


#  测试类，调用上面的方法进行测试
class Test:
    conn = get_connect()
    # 对查询结果进行加工
    outputList(conn)
    # 循环插入数据
    cycleInsert(conn)
    # 调用批量插入语句
    multiInsert(conn)
