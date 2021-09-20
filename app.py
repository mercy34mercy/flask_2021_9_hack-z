# -*- coding: utf-8 -*-
from flask import Flask
from request import req
from get_greate import great_img

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, world'

@app.route('/koi')
def indexs():
    r = req()
    c = great_img(r[0],r[1])
    return c

    




if __name__ == '__main__':
    app.run()
