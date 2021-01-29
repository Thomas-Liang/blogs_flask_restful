# @Time     : 2021/1/30 6:59 PM
# @Author   : Thomas
# @File     : __init__.py
from flask import Blueprint

from flask_restful import Api

from api.modules.books.views import BooksView

books_blu = Blueprint('books',__name__,url_prefix='/books')

api = Api(books_blu)

api.add_resource(BooksView,'/book')