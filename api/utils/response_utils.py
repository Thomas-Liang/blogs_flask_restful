# @Time     : 2021/1/29 7:49 AM
# @Author   : Thomas
# @File     : response_utils.py
<<<<<<< HEAD
=======
from flask import jsonify

class HttpCode:
    OK           = 200
    DB_ERROR     = 400
    AUTH_ERROR   = 401
    PARAMS_ERROR = 406
    SERVER_ERROR = 500

def resp_result(code,msg,data):
    return jsonify(code=code,msg=msg,data=data)

def success(msg,data=None):
    return resp_result(HttpCode.OK,msg,data)

def error(code,msg,data=None):
    return resp_result(code,msg,data)
>>>>>>> 150ca37... Second Commit
