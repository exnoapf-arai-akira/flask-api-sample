# -*- coding: utf-8 -*-
import peewee

db = peewee.SqliteDatabase("data.db")

class myProduct(peewee.Model):
    uid = peewee.TextField()
    name = peewee.TextField()
    price = peewee.IntegerField()
    classname = peewee.TextField()

    class Meta:
        database = db

myProduct.create_table()

for line in open("user.tsv", "r"):
    (uid, name, price, classname) = tuple(line[:-1].split("\t"))
    if price.isdigit():
        myProduct.create(uid = uid,
                    name = name,
                    price = int(price),
                    classname = classname)

# confirm importing data
for p in myProduct.select():
    print p.name,p.price,p.classname
