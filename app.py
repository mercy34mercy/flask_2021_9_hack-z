# -*- coding: utf-8 -*-
from flask import Flask
import requests
from request import req
from get_greate import great_img
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, world'

@app.route('/url',methods=['POST','GET'])
def indexs():
    try:
        if request.method == 'POST':
            top_key = request.json['quali']
            num = request.json["num"]
        elif request.method == 'GET':
            top_key = "美女"
            num = 3
    except:
        return "EOF"
    r = req(top_key,num)
    c = great_img(r[0],r[1])
    return jsonify({
    "data":[
        {
            "url":c[0],
            "alt":c[1]
        },
        {
            "url":c[2],
            "alt":c[3]
        },
        {
            "url":c[4],
            "alt":c[5]
        }
    ]
})

    




if __name__ == '__main__':
    app.run()
