# @Time     : 2021/1/28 9:09 PM
# @Author   : Thomas
# @File     : app.py
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run()
