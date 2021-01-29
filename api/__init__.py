# @Time     : 2021/1/28 10:43 PM
# @Author   : Thomas
# @File     : __init__.py.py
import redis

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

# from api.utils.log_utils import setup_log

from config.config import configs,Config

