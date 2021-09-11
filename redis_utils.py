# -*- coding: utf-8 -*-
# @Time   : 2021/3/7
# @Author : lorineluo 
import redis

class OPRedis(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        if not hasattr(OPRedis, 'pool'):
            OPRedis.getRedisConn(self.host, self.port)
        self.conn = redis.Redis(connection_pool=OPRedis.pool)

    @staticmethod
    def getRedisConn(host, port):
        OPRedis.pool = redis.ConnectionPool(host=host, port=port, decode_responses=True)

    def zadd_redis(self, key, mapping):
        return self.conn.zadd(key, mapping) 

    def delete_redis(self):
        pass

    def exist_redis(self, key, name):
        return self.conn.zrank(key, name)

    def zrangebyscore_redis(self, key, start, end, withscores=False):
        return self.conn.zrangebyscore(key, start, end, withscores=False)

if __name__ == '__main__':
    opr = OPRedis('localhost', 6379)
    opr.zadd_redis('test1', {'x1': 1630729892})
    opr.zadd_redis('test1', {'x3': 1630729882})
    res = opr.zrangebyscore_redis('test1', 1630719882, 1630739182, withscores=True)
    print(res)
    print([x for (x, y) in res])
    # print(opr.zscore('test1', 'x1'))
    # print(" rank:", opr.zrank('test1', 'x1'))
    # print(opr.zrank('test1', 'x2'))