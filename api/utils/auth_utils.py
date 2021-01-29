# @Time     : 2021/1/29 7:49 AM
# @Author   : Thomas
# @File     : auth_utils.py
<<<<<<< HEAD
=======

import datetime
import jwt
import time
from config.config import Config
from api.models import UserLogin
from api.utils.response_utils import success, error, HttpCode


class Auth:
    @staticmethod
    def encode_auth_token(user_id, login_time):
        # 生成认证token
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'iss': 'test',
                'data': {
                    'id': user_id,
                    'login_time': login_time
                }
            }
            return jwt.encode(
                payload,
                Config.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, Config.SECRET_KEY, leeway=datetime.timedelta(days=1))
            if 'data' in payload and 'id' in payload['data']:
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token 过期'
        except jwt.InvalidTokenError:
            return '无效Token'

    def authenticate(self, mobile, password):
        user = UserLogin.query.filter_by(mobile=mobile).first()
        if not user:
            return error(HttpCode.AUTH_ERROR, '用户不存在')
        if user.check_password(password):
            login_time = int(time.time())
            user.login_time = login_time
            user.update()
            token = self.encode_auth_token(user.id, login_time)
            token = str(token, encoding='utf-8')
            return success('登录成功', data={'token': token})
        else:
            return error(HttpCode.PARAMS_ERROR, '密码错误')

    def identity(self, request):
        # 用户鉴权
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token_array = auth_header.split(" ")
            if not auth_token_array or auth_token_array[0] != 'JWT' or len(auth_token_array) != 2:
                return HttpCode.AUTH_ERROR
            else:
                auth_token = auth_token_array[1]
                payload = self.decode_auth_token(auth_token)
                if not isinstance(payload, str):
                    user_id = payload.get('data').get('id')
                    login_time = payload.get('data').get('login_time')
                    user = UserLogin.query.get(user_id)
                    if not user:
                        return HttpCode.AUTH_ERROR
                    else:
                        if user.last_login == login_time:
                            return success(msg='用户认证成功', data={"user_id": user.id})
                        else:
                            return error(code=HttpCode.AUTH_ERROR, msg='用户认证失败')
                else:
                    return error(code=HttpCode.AUTH_ERROR, msg='用户认证失败')
        else:
            return error(code=HttpCode.AUTH_ERROR, msg='用户认证失败')
>>>>>>> 150ca37... Second Commit
