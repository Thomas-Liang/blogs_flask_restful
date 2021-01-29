# @Time     : 2021/1/28 10:43 PM
# @Author   : Thomas
# @File     : models.py

from datetime import datetime

<<<<<<< HEAD
from werkzeug.security import generate_password_hash,check_password_hash

# from . import db



=======
from werkzeug.security import generate_password_hash, check_password_hash

from api.utils.db_utils import session_commit
from . import db


# 基础表
class BaseModel:
    def add(self, obj):
        db.session.add(obj)
        return session_commit()

    def update(self):
        return session_commit()

    def delete(self):
        return session_commit()


# 用户登录信息表
class UserLogin(BaseModel, db.Model):
    __tablename__ = 'user_login'
    id = db.Column(db.Integer, db.ForeignKey('books_info.user_id'), primary_key=True, autoincrement=True, )
    mobile = db.Column(db.String(16), unique=True, nullable=False)
    nickname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    last_login = db.Column(db.DateTime, default=datetime.now)
    login_time = db.Column(db.DateTime, default=datetime.now)

    @property
    def password(self):
        raise AttributeError('当前属性不可读')

    @password.setter
    def password(self, value):
        self.password = generate_password_hash(value)

    def check_password(self, value):
        return check_password_hash(self.password, value)

    def to_dict(self):
        res_dict = {
            'mobile': self.mobile
        }
        return res_dict


# 书籍信息表

class Books(BaseModel, db.Model):
    __tablename__ = 'books_info'
    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    category = db.Column(db.String(10), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum('0', '1'), default='1')

    def to_dict(self):
        res_dict = {
            'book_id': self.book_id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'user_id': self.user_id,
            'status': self.status
        }
        return res_dict
>>>>>>> 150ca37... Second Commit
