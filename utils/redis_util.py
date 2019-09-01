#!/usr/bin/env python3
# coding:utf-8

import redis


class RedisUtil():
    def __init__(self, redis_config):
        self.pool = redis.ConnectionPool(**redis_config, decode_responses=True)
        self.r = redis.StrictRedis(connection_pool=self.pool)

    def conn_redis(self):
        self.r = redis.StrictRedis(connection_pool=self.pool)
        print(self.r.ping())
        return self.r

    def use_handler(self):
        self.r.select(1)

    def set_handler(self, key, value):
        self.r.set(key, value)

    def get_handler(self, key):
        self.r.get(key)

    def lpush_handler(self, lis, value):
        self.r.lpush(self.lis, self.value)

    def lrange_handler(self, lis, st, en):
        self.r.lrange(self.lis, self.st, self.en)

    def rpop_handler(self):
        pass

    def hset_handler(self, has, key, value):
        self.r.hset(self.has, self.key, self.value)

    def hget_handler(self):
        self.r.hget()

    def hgetall_handler(self):
        pass


def redis_pool(host, port, db, password):
    pool = redis.ConnectionPool(
        host=host, port=port, db=db, password=password, decode_responses=True)
    return pool


def redis_conn(pool):
    r = redis.StrictRedis(connection_pool=pool)
    print(r.ping())
    return r


def conn_redis(host, port, db, password):
    r = redis.Redis(
        host=host, port=port, db=db, password=password, decode_responses=True)
    print(r.ping())
    return r


if __name__ == '__main__':
    redis_config = {
        'host': '127.0.0.1',
        'port': 6379,
        # 'db': 0,
        # 'password': 'redis',
    }
    RedisUtil = RedisUtil(redis_config)
    r = RedisUtil.conn_redis()
    RedisUtil.set_handler('test', '123')
    print(RedisUtil.get_handler('test'))
    RedisUtil.use_handler()