#!/usr/bin/python3
# coding:utf-8
"""
 Copyright (C) 2024 - 2024 Meteor， Inc. All Rights Reserved
 @Time    : 2024/8/2 下午12:22
 @Author  : Meteor
 @Email   : xxx130032@gmail.com
 @Website : https://0meteor0.pythonanywhere.com/
 @File    : demo.py
 @IDE     : PyCharm
"""
from flask import Flask, request, render_template, jsonify
from openai import OpenAI

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ai')
def que():
    que = request.args.get('que')
    text = ai(que).choices[0].message.content
    return text


def ai(que):
    client = OpenAI(
        # api_key:拼接key和secret
        api_key="ddb9b6079cb119d7da856a5558af7f78:NGI3MDNlMzYzYjBhMDU5MDIxNjAyNTQ1",
        base_url='https://spark-api-open.xf-yun.com/v1'  # 指向讯飞星火的请求地址
    )
    completion = client.chat.completions.create(
        model='general',  # 指定请求的版本
        messages=[
            {
                "role": "user",
                "content": f'{que}'
            }
        ]
    )

    return completion


if __name__ == '__main__':
    app.run(debug=True)
