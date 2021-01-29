# @Time     : 2021/1/28 9:56 PM
# @Author   : Thomas
# @File     : config.py

import logging
from redis import StrictRedis

class Config:
    #配置文件的加载
    SECRET_KEY = 'sldjsfa;fa;lfj;akf;afasfjkljkbmsfn,sbfasblkfbasjkbf,mbasm,dnmn'
    JSON_AS_ASCII = False
    DEBUG = True

    #数据库驱动 + 连接工具
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xuan0216@127.0.0.1:3306/restful'

    #不追踪数据库的修改，节省开销
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #配置redis数据库:因为redis模块不是flask的扩展，需要自己读取配置信息
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

# 封装不同服务器环境的配置信息

class DevelopmentConfig(Config):
    #开发环境
    #开发环境和父类基本一致

    #开发环境日志等级
    LEVEL_LOG = logging.DEBUG

class ProductionConfig(Config):
    #生产环境
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xuan0216@127.0.0.1:3306/restful_prod'

    #生产环境日志等级
    LEVEL_LOG = logging.ERROR

class UnitTestConfig(Config):
    #测试环境
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xuan0216@127.0.0.1:3306/restful_test'

    #测试环境日志等级
<<<<<<< HEAD
    LEVEL_LOG = logging.DEBUG
=======
    LEVEL_LOG = logging.DEBUG

#定义字典，存储关键字对应的不同的配置类的类名
configs = {
    'dev':DevelopmentConfig,
    'pro':ProductionConfig,
    'unit':UnitTestConfig
}
>>>>>>> 150ca37... Second Commit
