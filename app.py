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
    top_key = "美女"
    num = 9
    try:
        if request.method == 'POST':
            top_key = request.json['query'] 
            num = request.json["num"]
        elif request.method == 'GET':
            top_key = "美女"
            num = 9
    except:
        return "EOF"
    r = req(top_key,num)
    c,d = great_img(r[0],r[1],num)

    

    
    jsonify = ({
        "data":[]
    })

    for i in range(len(c)):
        print(c[i])
        add_data={
            "url":c[i],
            "alt":d[i]
        }
        jsonify["data"].append(add_data)

    print(jsonify)
    
    
    return jsonify

    

if __name__ == '__main__':
    app.run()
