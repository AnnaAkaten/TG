import telebot
from telebot import types

token = '6915082221:AAGCu2YjFbiy0x0yNoWzJbNOTrBdpe1YVCA'
bot = telebot.TeleBot(token)
what_to_do = '✨️Прогуляться по лесу и исследовать близлежайшие лесные чащи, поля и водоёмы.\n✨️Организовать рыбалку или прокатиться на велосипедах.\n✨️Попариться в бане и окунуться в купель\n✨️В непосредственной близости располагается Спа центр с бассейном, рестораны, бильярд, боулинг, лыжная база, конный клуб и открытый каток.'
rules = 'Правила проживания: \n❌строго запрещено курение, в том числе электронных сигарет. Запрещено разжигать открытые источники огня в доме и на веранде. В доме стоит противопожарная сигнализация.\n❌запрещено хождение в доме в уличной обуви;\n❌запрещено использовать на территории пиротехнику;\n❌запрещено проведение шумных вечеринок;\n❌возраст гостей для бронирования дома - от 26 лет.'


@bot.message_handler(commands=['start'])
def start_message(message):
    mess = f'Привет✌️ {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, reply_markup=bottom_menu())


@bot.message_handler()
def get_use_text(message):
    if message.text.lower() in ['hello', 'привет', 'здравствуй', 'hi', 'hello']:
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif 'фото' in message.text.lower():
        data = open('i.webp', 'rb')
        bot.send_photo(message.chat.id, data)
    elif 'забронир' in message.text.lower():
        bot.send_message(message.chat.id,
                         r'https://www.avito.ru/moskovskaya_oblast_troitsk/doma_dachi_kottedzhi/kottedzh_250m_na_uchastke_8sot._2983767192?utm_campaign=native&utm_medium=item_page_android&utm_source=soc_sharing_seller')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю')
    bot.polling(none_stop=True)


def bottom_menu():
    bottom_list = types.InlineKeyboardMarkup(row_width=2)
    bottom1 = types.InlineKeyboardButton('Посуточно', callback_data='q1')
    bottom2 = types.InlineKeyboardButton('Длительная аренда', callback_data='q2')
    bottom3 = types.InlineKeyboardButton('Фото', callback_data='q3')
    bottom4 = types.InlineKeyboardButton('Чем заняться', callback_data='q4')
    bottom5 = types.InlineKeyboardButton('Аренда бани', callback_data='q5')
    bottom6 = types.InlineKeyboardButton('Аренда купели', callback_data='q6')
    bottom_list.add(bottom1, bottom2, bottom3, bottom4, bottom5, bottom6)
    return bottom_list


def bottom_menu_for_q1():
    bottom_list = types.InlineKeyboardMarkup(row_width=2)
    bottom1 = types.InlineKeyboardButton('Стоимость в будние', callback_data='q7')
    bottom2 = types.InlineKeyboardButton('Стоиомтсь в выходные', callback_data='q8')
    bottom3 = types.InlineKeyboardButton('Условия аренды', callback_data='q9')
    bottom4 = types.InlineKeyboardButton('Забронировать', callback_data='q10')
    bottom_list.add(bottom1, bottom2, bottom3, bottom4)
    return bottom_list


def bottom_menu_for_q2():
    bottom_list = types.InlineKeyboardMarkup(row_width=2)
    bottom1 = types.InlineKeyboardButton('Стоимость', callback_data='q11')
    bottom2 = types.InlineKeyboardButton('Забронировать', callback_data='q12')
    bottom_list.add(bottom1, bottom2)
    return bottom_list


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'q1':
            bot.send_message(call.message.chat.id, 'Посуточно', reply_markup=bottom_menu_for_q1())
        elif call.data == 'q2':
            bot.send_message(call.message.chat.id, 'Длительно', reply_markup=bottom_menu_for_q2())
        elif call.data == 'q3':
            bot.send_message(call.message.chat.id,
                             r'https://www.avito.ru/moskovskaya_oblast_troitsk/doma_dachi_kottedzhi/kottedzh_250m_na_uchastke_8sot._2983767192?utm_campaign=native&utm_medium=item_page_android&utm_source=soc_sharing_seller')
        elif call.data == 'q4':
            bot.send_message(call.message.chat.id, what_to_do)
        elif call.data == 'q5':
            bot.send_message(call.message.chat.id, r'Аренда бани: 6 000 руб./4 часа')
        elif call.data == 'q6':
            bot.send_message(call.message.chat.id, r'Аренда купели: 7 000 руб./4 часа')
        elif call.data == 'q7':
            bot.send_message(call.message.chat.id,
                             'Сутки в будние (вс-чт):от 10 000 руб.\nЦены указаны за размещение 2 гостей. Стоимость размещения дополнительно гостя составляет: 1000 руб./сутки')
        elif call.data == 'q8':
            bot.send_message(call.message.chat.id,
                             'Сутки в выходные (пт-сб):от 14 000 руб.\nЦены указаны за размещение 2 гостей. Стоимость размещения дополнительно гостя составляет: 1000 руб./сутки')
        elif call.data == 'q9':
            bot.send_message(call.message.chat.id, rules)
        elif call.data == 'q10':
            bot.send_message(call.message.chat.id,
                             r'https://www.avito.ru/moskovskaya_oblast_troitsk/doma_dachi_kottedzhi/kottedzh_250m_na_uchastke_8sot._2983767192?utm_campaign=native&utm_medium=item_page_android&utm_source=soc_sharing_seller')
        elif call.data == 'q11':
            bot.send_message(call.message.chat.id, 'Стоимость аренды на месяц: 230 000 руб.')
        elif call.data == 'q12':
            bot.send_message(call.message.chat.id,
                             r'https://www.avito.ru/moskovskaya_oblast_troitsk/doma_dachi_kottedzhi/kottedzh_250m_na_uchastke_8sot._2983767192?utm_campaign=native&utm_medium=item_page_android&utm_source=soc_sharing_seller')


bot.polling(none_stop=True)
