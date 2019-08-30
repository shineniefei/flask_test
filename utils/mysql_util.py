#!/usr/bin/env python3
# coding:utf-8

import pymysql
import logging


class MysqlUtil():
    # 创建：数据库连接
    def __init__(self, db_config):
        self.conn = pymysql.connect(**db_config)
        logging.info('DB conn ： ', db_config)

    # 切换：数据库
    def use_db(self, db):
        logging.info('DB use ： ', db)
        try:
            with self.conn.cursor() as cursor:
                cursor.execute('use ' + db)
        except Exception:
            return 'use_db error'

    # 查：返回查询内容，一元数组
    def sel_handle(self, sql):
        logging.info('DB select ： ', sql)
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                rs = cursor.fetchone()
            logging.info('DB info : ', rs)
            return rs
        except Exception:
            return 'sel_handle error'

    # 查：返回查询内容，二元数组
    def sels_handle(self, sql):
        logging.info('DB selects ： ', sql)
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                rs = cursor.fetchall()
            logging.info('DB info : ', rs)
            return rs
        except Exception:
            return 'sels_handle error'

    # 增删改： 返回受影响行数
    def cud_handle(self, sql, params=None):
        logging.info('DB cud ： ', sql, params)
        try:
            with self.conn.cursor() as cursor:
                if params:
                    effect_row = cursor.execute(sql, params)
                else:
                    effect_row = cursor.execute(sql)
                self.commit_handle()
            logging.info('DB info : ', effect_row)
            return effect_row
        except Exception:
            self.rollback_handle()
            return 'cud_handle error'

    # 回滚事务
    def rollback_handle(self):
        self.conn.rollback()
        logging.info('DB rollback')

    # 提交事务
    def commit_handle(self):
        self.conn.commit()
        logging.info('DB commit')

    # 关闭连接
    def close_handle(self):
        self.conn.close()
        logging.info('DB close')


def query(sql, db_config):
    conn = pymysql.connect(**db_config)
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            rs = cursor.fetchone()  # 返回一元数组
    except Exception as e:
        raise e
    finally:
        conn.close()
    print('db_config: {},execute sql: {},effect_row: {},get result:{}'.format(
        db_config, sql, cursor.rowcount, str(rs)))
    return rs


# 查询多条数据，返回二元数组
def querys(sql, db_config):
    conn = pymysql.connect(**db_config)
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            rs = cursor.fetchall()
    except Exception as e:
        raise e
    finally:
        conn.close()
    print('db_config: {},execute sql: {},effect_row: {},get result:{}'.format(
        db_config, sql, cursor.rowcount, str(rs)))
    return rs


def cud(sql, db_config):
    conn = pymysql.connect(**db_config)
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()
    except Exception as e:
        raise e
        conn.rollback()
    finally:
        conn.close()
    print('db_config: {},execute sql: {},effect_row: {}'.format(
        db_config, sql, cursor.rowcount))


def cud_tup(sql_tup, db_config):
    if type(sql_tup) is tuple and len(sql_tup) > 0 and db_config == '':
        return
    conn = pymysql.connect(**db_config)
    try:
        with conn.cursor() as cursor:
            for sql in sql_tup:
                cursor.execute(sql)
                print('effect_row = ', format(cursor.rowcount))
            conn.commit()
    except Exception as e:
        raise e
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    sql = '''select NOW();'''
    sql_tup = ('''select NOW();''', '''select NOW();''')
    db_config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': 'root',
        'db': 'mysql',
        # 'charset':'utf8mb4',
    }

    # querys(sql, db_config)
    mysql = MysqlUtil(db_config)
    a = mysql.sels_handle(sql)
    print(a)
    mysql.close_handle()
