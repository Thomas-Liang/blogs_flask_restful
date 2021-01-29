# @Time     : 2021/1/29 7:50 AM
# @Author   : Thomas
# @File     : auth.py
<<<<<<< HEAD
=======

from flask import Blueprint
from flask_restful import Api
from api.resources.auth import AuthResource,UsersResource,BooksResource

auth_blu = Blueprint('auth',__name__,url_prefix='/auth')

api = Api(auth_blu)
api.add_resource(AuthResource,'/session')
api.add_resource(UsersResource,'/users')
api.add_resource(BooksResource,'/books')
>>>>>>> 150ca37... Second Commit
