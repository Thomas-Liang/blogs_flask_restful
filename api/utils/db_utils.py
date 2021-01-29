# @Time     : 2021/1/29 7:49 AM
# @Author   : Thomas
# @File     : db_utils.py
<<<<<<< HEAD
=======
from sqlalchemy.exc import SQLAlchemyError

from api import db

from api.utils.response_utils import error,HttpCode

def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return error(code=HttpCode.DB_ERROR,msg=reason)
>>>>>>> 150ca37... Second Commit
