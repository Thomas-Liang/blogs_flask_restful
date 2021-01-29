# @Time     : 2021/1/29 7:49 AM
# @Author   : Thomas
# @File     : log_utils.py
<<<<<<< HEAD
=======
import logging

from logging.handlers import RotatingFileHandler

def setup_log(level):
    # 根据创建app时的配置环境，加载日志等级
    # 设置日志的记录等级
    logging.basicConfig(level=level)
    #创建日志记录器，指明日志保存的路径，每个日志文件的大小，保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log",maxBytes=1024 * 1024 * 100, backupCount=10)
    #创建日志记录的格式
    formatter = logging.Formatter('%(asctime)s - %(levelname) %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象 (flask app使用的) 添加日子记录器
    logging.getLogger().addHandler(file_log_handler)
>>>>>>> 150ca37... Second Commit
