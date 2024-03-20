import json
import requests
from bs4 import BeautifulSoup
adress = r'https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526.'


def get_info():
    my_req = requests.get(adress)
    res_dict = my_req.text
    # инициализируем html-код страницы
    soup = BeautifulSoup(res_dict, features='html.parser')
    # считываем заголовок страницы
    title = soup.title.string
    temp = soup.find('span', 'temp__value temp__value_with-unit')
    print(temp.text)



get_info()
