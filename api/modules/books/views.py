# @Time     : 2021/1/30 7:02 PM
# @Author   : Thomas
# @File     : views.py
from flask import current_app, session, g
from flask_restful import Resource, reqparse, inputs
from datetime import datetime as dt

from api import db
from api.models import Books

from api.utils.response_utils import error, HttpCode, success

class BooksView(Resource):
    def get(self):
        if not g.data.get('success'):
            return error(code=HttpCode.PARAMS_ERROR, msg='用户未登录')

    def post(self):
        if not g.data.get('success'):
            return error(code=HttpCode.PARAMS_ERROR, msg='用户未登录')

    def update(self):
        if not g.data.get('success'):
            return error(code=HttpCode.PARAMS_ERROR, msg='用户未登录')

    def delete(self):
        if not g.data.get('success'):
            return error(code=HttpCode.PARAMS_ERROR, msg='用户未登录')
