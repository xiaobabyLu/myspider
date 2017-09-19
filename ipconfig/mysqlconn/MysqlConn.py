# -*- coding:utf-8 -*-

"""
    Created on 2017-09-15
    @Author : BruceLu
    @Desc : MySQL DataBase connection
"""
import MySQLdb
from MySQLdb.cursors import DictCursor
from DBUtils.PooledDB import PooledDB
import ConfigGet

config = ConfigGet.getConfig()
# print config
connKwargs = {'host': config['host'], 'port': config['port'],
              'user': config['user'], 'passwd': config['passwd'],
              'db': config['db'], 'charset': config['charset']}


class MySqlConn(object):

    __pool = None

    def __init__(self):
        self._conn = MySqlConn.__get_conn()
        self._cursor = self._conn.cursor()

    @staticmethod
    def __get_conn():
        if MySqlConn.__pool is None:
            __pool = PooledDB(creator=MySQLdb, mincached=1, maxcached=20,cursorclass=DictCursor,**connKwargs)
        return __pool.connection()

    def query_all(self, sql, param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count > 0:
            result = self._cursor.fetchall()
        else:
            result = False
        return result

    def query_one(self,sql,param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count> 0:
            result = self._cursor.fetchone()
        else:
            result = False
        return result

    def query_many(self,sql,size,param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql, param)
        if count> 0:
            result = self._cursor.fetchmany(size)
        else:
            result = False
        return result

    # 定义插入的数据最后一条的id
    def __get_insertid(self):
        self._cursor.execute('select @@IDENTITY as id')
        result = self._cursor.fetchall()
        return result[0]['id']

    def insert_one(self,sql,value):
        self._cursor.execute(sql,value)
        return self.__get_insertid()

    def insert_many(self,sql,values):
        count = self._cursor.executemany(sql,values)
        return count

    def __get_operate(self,sql,param=None):
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql,param)
        return count

    def update(self,sql,param=None):
        return self.__get_operate(sql,param)

    def delete(self,sql,param=None):
        return self.__get_operate(sql,param)

    def begin(self):
        self._conn.autocommit(0)

    def end(self,option='commit'):
        if option == 'commit':
            self._conn.commit()
        else:
            self._conn.rollback()

    def dispose(self,isEnd = 1):
        if isEnd == 1:
            self.end('commit')
        else:
            self.end('rollback')
        self._cursor.close()
        self._conn.close()
