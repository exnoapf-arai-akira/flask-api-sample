# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response
import peewee
import json

db = peewee.SqliteDatabase("data.db")
db.connect()
class myProduct(peewee.Model):
    uid = peewee.TextField()
    name = peewee.TextField()
    price = peewee.IntegerField()
    classname = peewee.TextField()

    class Meta:
        database = db

api = Flask(__name__)

# set a action url
@api.route('/getprice/<string:name>', methods=['GET'])

def get_price(name):
    try:
        price = myProduct.get(myProduct.name == name)
    except myProduct.DoesNotExist:
        return make_response(jsonify({'error': 'no such as name'}), 200)

    result = {
        "result":True,
        "data":{
            "name":price.name,
            "price":price.price,
            "classname":price.classname
            }
        }

    return make_response(json.dumps(result, ensure_ascii=False))

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__== '__main__':
    api.run(host='0.0.0.0', port=3000)
