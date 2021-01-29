# @Time     : 2021/1/29 7:51 AM
# @Author   : Thomas
# @File     : views.py
<<<<<<< HEAD
=======
from flask import current_app, session, g
from flask_restful import Resource, reqparse, inputs
from datetime import datetime as dt

from api import db
from api.models import UserLogin, Books

from api.utils.response_utils import error, HttpCode, success


class LoginView(Resource):
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('mobile', type=inputs.regex('1[3456789]\\d{9}'), required=True,
                            nullable=False, location=['json'], help='手机号格式不正确')
        # parser.add_argument('nickname', type=inputs.regex('^[A-Za-z][A-Za-z0-9]{2,7}'), required=True,
        #                     nullable=False, location=['json'], help='昵称格式不正确')
        parser.add_argument('password', required=True, nullable=False, location=['json'],
                            help='密码不正确')
        args = parser.parse_args()

        try:
            user = UserLogin.query.filter_by(mobile=args.mobile).first()
        except Exception as e:
            current_app.logger.error(e)
            return error(HttpCode.DB_ERROR, msg='获取数据出错')

        if not user:
            return error(HttpCode.PARAMS_ERROR, msg='用户不存在')

        if not user.check_password(args.password):
            return error(HttpCode.PARAMS_ERROR, msg='密码错误')

        # 保存session
        session['user_id'] = user.id
        session['mobile'] = user.mobile
        user.last_login = dt.now()

        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            current_app.logger.error(e)
            db.session.rollback()
            return error(code=HttpCode.DB_ERROR, msg='注册数据失败')

        g.data = {
            'id': user.id,
            'success': True
        }
        return success(msg='登录成功', data=user.to_dict())


class RegisterView(Resource):
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('mobile', type=inputs.regex('1[3456789]\\d{9}'), required=True,
                            nullable=False, location=['json'], help='手机号格式不正确')
        parser.add_argument('nickname', type=inputs.regex('^[A-Za-z][A-Za-z0-9]{2,7}'), required=True,
                            nullable=False, location=['json'], help='昵称格式不正确')
        parser.add_argument('password', required=True, nullable=False, location=['json'],
                            help='密码不正确')
        args = parser.parse_args()
        user = UserLogin()
        user.nickname = args.nickname
        user.mobile = args.mobile

        try:
            db.session.add(user)
            db.session.commit()
            userinfo = UserLogin.query.filter(UserLogin.mobile == args.mobile).first()
            if not userinfo:
                return error(code=HttpCode.DB_ERROR, msg='注册数据失败')
        except Exception as e:
            current_app.logger.error(e)
            db.session.rollback()
            return error(code=HttpCode.DB_ERROR, msg='注册数据失败')
        return success(msg='注册成功', data=user.to_dict())


class LogoutView(Resource):
    def post(self):
        session.pop('user_id', '')
        session.pop('mobile', '')
        g.success = False
        return success('退出成功')


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
>>>>>>> 150ca37... Second Commit
