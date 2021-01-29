# @Time     : 2021/1/28 9:09 PM
# @Author   : Thomas
# @File     : manager.py
from flask_migrate import Migrate,MigrateCommand
from api.models import UserLogin
from api import create_app,db
from flask_script import Manager

app = create_app('dev')
manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)
if __name__ == '__main__':
    manager.run()
