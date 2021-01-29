# @Time     : 2021/1/29 7:51 AM
# @Author   : Thomas
# @File     : __init__.py
<<<<<<< HEAD
=======
from flask import Blueprint

from flask_restful import Api

from api.modules.passport.views import LoginView,RegisterView,LogoutView,BooksView

passport_blu = Blueprint('passport',__name__,url_prefix='/passport')

api = Api(passport_blu)
api.add_resource(LoginView,'/login')
api.add_resource(RegisterView,'/register')
api.add_resource(LogoutView,'/logout')
# api.add_resource(BooksView,'/books')
>>>>>>> 150ca37... Second Commit
