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

def get_html(url):
    new_response = requests.get(url)
    return new_response.text

def currency_rates(dict_currency, string_currency):
    
        pass

def remove_trash(my_list, prefix, suffix):
    for index, value in enumerate(my_list):
        value = str (value).removeprefix (prefix)
        value = str (value).removesuffix (suffix)
        my_list[index] = value
    return my_list

def make_dict(key, value_name, value_nominal, value):
    my_dict = {}
    for index in range (len(key)):
        my_dict[key[index]] = [value_name[index], value_nominal[index], value[index]]
    return my_dict


def get_me_info(html):
    o_obj_soup = BeautifulSoup(html, 'lxml')
    print(o_obj_soup)
    currency_charcode = o_obj_soup.find_all('charcode')
    currency_nominal = o_obj_soup.find_all ('nominal')
    currency_value = o_obj_soup.find_all ('value')
    currency_name = o_obj_soup.find_all('name')
    currency_charcode = remove_trash(currency_charcode, '<charcode>', '</charcode>')
    currency_nominal = remove_trash (currency_nominal, '<nominal>', '</nominal>')
    currency_value = remove_trash (currency_value, '<value>', '</value>')
    currency_name = remove_trash(currency_name, '<name>', '</name>')
    currency = make_dict(currency_charcode, currency_name, currency_nominal, currency_value)
    return currency



def running():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    new_text = get_html(url)
    my_dict = get_me_info(new_text)
    print (currency_rates(my_dict, 'USD'))
    pass

if __name__ == '__main__':
    running()

