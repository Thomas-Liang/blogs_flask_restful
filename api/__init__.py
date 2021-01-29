# @Time     : 2021/1/28 10:43 PM
# @Author   : Thomas
# @File     : __init__.py.py
import redis

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

<<<<<<< HEAD
# from api.utils.log_utils import setup_log

from config.config import configs,Config

=======
from api.utils.log_utils import setup_log

from config.config import configs,Config

db = SQLAlchemy()


def create_app(config_name):
    config = configs[config_name]
    app = Flask(__name__)
    app.config.from_object(config)
    setup_log(config.LEVEL_LOG)
    db.init_app(app)

    # redis设置
    global redis_store
    redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT,decode_responses=True)

    from api.modules.passport import passport_blu
    app.register_blueprint(passport_blu)
    from api.routes.auth import auth_blu
    app.register_blueprint(auth_blu)

    return app

>>>>>>> 150ca37... Second Commit
