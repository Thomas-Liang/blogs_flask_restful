# @Time     : 2021/1/29 7:50 AM
# @Author   : Thomas
# @File     : auth.py
<<<<<<< HEAD
=======

from flask import current_app
from flask_restful import Resource, reqparse, inputs
from api import db
from api.models import Books, UserLogin
from api.utils.auth_utils import Auth
from api.utils.response_utils import error, HttpCode, success


class AuthResource(Resource):
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('mobile', type=inputs.regex('1[3456789]\\d{9}'), required=True,
                            nullable=False, location=['json'], help='手机号格式不正确')
        parser.add_argument('password', required=True, nullable=False, location=['json'],
                            help='密码不正确')
        args = parser.parse_args()
        return Auth().authenticate(args.mobile, args.password)

    def delete(self):
        pass


class UsersResource(Resource):
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
>>>>>>> 150ca37... Second Commit
