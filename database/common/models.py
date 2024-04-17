# -*- coding: UTF-8 -*-
import peewee as pw
db = pw.SqliteDatabase('telegram.db')


class ModelBase(pw.Model):
    class Meta:
        database = db


class History(ModelBase):
    chat_id = pw.IntegerField()
    user_name = pw.CharField(max_length=50)
    film_name = pw.CharField(max_length=70)



