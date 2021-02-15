# task2
'''
Написать функцию currency_rates() , принимающую в качестве аргумента код валюты (USD,
EUR, ...) и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку
requests . В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp .
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть
содержимое ответа. Можно ли, используя только методы класса str, решить поставленную
задачу? Функция должна возвращать результат числового типа, например float . Подумайте:
есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal ?
Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в
каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
'''
import requests
from bs4 import BeautifulSoup
from lxml import html

'''Функция получения странички'''
def get_html(url):
    new_response = requests.get(url)
    return new_response.text

'''Функция возврата значения из словаря'''
def currency_rates(dict_currency, string_currency):
    return dict_currency.get(string_currency)

'''Функция очистки от мусора'''
def remove_trash(my_list, prefix, suffix):
    for index, value in enumerate(my_list):
        value = str (value).removeprefix (prefix)
        value = str (value).removesuffix (suffix)
        my_list[index] = value
    return my_list


'''Функция создания словаря из списков'''
def make_dict(key, value_name, value):
    return {key[index]: [value_name[index], value[index]] for index in range (len(key))}


'''Функция получает страницу, вырезает с нее необходимые данные, чистит от мусора и создает словарь, который
возвращает'''
def get_me_info(html):
    o_obj_soup = BeautifulSoup(html, 'lxml')
    currency_charcode = remove_trash(o_obj_soup.find_all('charcode'), '<charcode>', '</charcode>')
    currency_value = remove_trash (o_obj_soup.find_all ('value'), '<value>', '</value>')
    currency_name = remove_trash(o_obj_soup.find_all('name'), '<name>', '</name>')
    return make_dict(currency_charcode, currency_name, currency_value)




'''Рабочая функция'''
def running():
    try:
        url = 'http://www.cbr.ru/scripts/XML_daily.asp'
        new_text = get_html(url)
        my_dict = get_me_info(new_text)
        print(' '.join(currency_rates(my_dict, 'USD')))
        print (' '.join (currency_rates (my_dict, 'EUR')))
        print (' '.join (currency_rates (my_dict, 'RRR')))
    except TypeError:
        print('Нет такой валюты')
    pass

if __name__ == '__main__':
    running()

