# -*- coding: UTF-8 -*-
from python_basic_diploma.database.common.models import *
from python_basic_diploma.database.common.models import History, db
from typing import Any


def fulfill_date(data_base, model, *data: list) -> Any:
    with data_base.atomic():
        model.insert_many(data).execute()


def retrieve_all_data(data_base, model, chat_id: int) -> str:
    with data_base.atomic():
        response = [i.film_name for i in model.select().where(History.chat_id == chat_id)]

    return '\n'.join(response)


for i in retrieve_all_data(db, History, History.film_name):
    print(i)


class CRUDInterface:
    @staticmethod
    def create():
        return fulfill_date

    @staticmethod
    def retrieve():
        return retrieve_all_data

#
# if __name__ == '__main__':
#     fulfill_date()
#     retrieve_all_data()
#     CRUDInterface()
