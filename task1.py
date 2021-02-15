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

def currency_rates(argv):
        pass

def get_me_info(html):
    o_obj_soup = BeautifulSoup(html, 'lxml')
    print(o_obj_soup)
    # print (o_obj_soup.text)
    currency = o_obj_soup.findAll('valute')
    print(currency)
    pass



def running():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    new_text = get_html(url)
    get_me_info(new_text)
    # print(new_text)
    pass

if __name__ == '__main__':
    running()

