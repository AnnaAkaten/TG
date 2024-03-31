import json
import requests
import os
from dotenv import load_dotenv
import random
import telebot
from telebot import types

movie_hist = {}


def get_token(key):
    tok_path = os.path.abspath('.env')
    load_dotenv(tok_path)
    return os.environ.get(key)


TOKEN = get_token('TOKEN_KINO')
headers = {'X-API-KEY': TOKEN}


def get_info(type_of_film):
    my_req = requests.get(f'https://api.kinopoisk.dev/v1.4/movie?year=2023&genres.name={type_of_film}', headers=headers)
    res_dict = my_req.text
    data = json.loads(res_dict)
    res = []
    m_l = data['docs']
    for i in m_l:
        res.append([i['name'], 'рейтинг kp: ' + str(i['rating']['kp']), i['description'], i['backdrop']['previewUrl']])
    res = random.choice(res)
    return [res[0], '\n'.join(res[1:3]), res[3]]
    # return data


# print(json.dumps(get_info('комедия'), indent=4))

def add_to_movie(chat_id, name):
    with open('movie_hist.txt', 'a', encoding='utf-8') as data:
        data.write(f'{chat_id} {name}')



