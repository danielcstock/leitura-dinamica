# -*- coding: utf-8 -*-
# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from json import dumps
import StringController as strc
import sys

app = Flask(__name__)
CORS(app)
api = Api(app)

class Text(Resource):
    def __init__(self):
        f = open("test.txt", "r", encoding='utf8')
        self.text = f.read()

    def get(self):
        text = self.text
        text = text.replace("– ", "–")
        array = text.split()
        result = list()
        for word in array:
            result.append(word)
            if any(["," in word, "." in word, "?" in word, "!" in word]):
                result.append(" ")
        return jsonify(result)

api.add_resource(Text, '/text') 

if __name__ == '__main__':
    app.run()