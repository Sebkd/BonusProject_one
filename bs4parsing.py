'''Парсинг страницы Хабр'''

import requests
from bs4 import BeautifulSoup
import re

class Parsing_url():
    def __init__(self, url):
        self.__page = 1
        self.__num_pages = 0
        self.__articles = []
        self._url = url
        pass

    def parse(self):
        '''Главная функция'''
        while self.__page:

            soup_obj, error = get_page (self.__page, self._url)
            if error:
                break

            get_articles (soup_obj, self.__articles)
            self.__num_pages += 1

            self.__page = get_next_page_number (soup_obj)

        return self.__articles

    def get_page(self, page, url):
        '''Получить страницу с лучшими статьями Habr.ru'''

        error = False
        if page == 1:
            url = 'https://habr.com/ru/top'
        else:
            url = 'https://habr.com/ru/top/page' + page + '/'
        response = requests.get(url, headers = {'User-Agent' : 'Mozilla/5.0'})
        if response.status_code != 200:
            error = True
            return '', error
        soup_obj = BeautifulSoup(response.content, 'html.parser')
        return soup_obj, error

def get_articles(soup_obj, articles):
    '''Получить заголовки, адреса и тексты статей со страницы'''

    error = False # зачем?
    resurs = soup_obj.find_all('a', { 'class' : 'post__title_link'}) # wrong
    if resurs:
        for info in resurs:
            url = info.get('href')
            text = get_text(url)
            articles.append({url : [info.text, text]})


def get_text(url):
    '''Получить текст статьи по этому адресу'''

    response = requests.get(url, headers = {'User-Agent' : 'Mozilla/5.0'})
    if response.status_code != 200:
        error = True
        return ''
    soup_obj = BeautifulSoup(response.content, 'html.parser')
    return clean_text(soup_obj)

def clean_text(soup_obj):
    '''Получить очищенный текст'''

    resurs = soup_obj.find_all('div', { 'class' : 'post__text'})
    text = ''.join([info.text for info in resurs])
    text = re.sub('\n+', '\n', text) # удалить ненужные символы
    return text

def get_next_page_number(soup_obj):
    '''Получить следующий номер страницы или 0'''

    resurs = soup_obj.find('a', { 'class' : 'arrows-pagination_item-link_next'})
    if not resurs:
        return 0
    page = resurs.get('href')[12:-1]
    return page

def parse():
    '''Главная функция'''

    page = 1
    num_pages = 0
    articles = []

    while page:

        soup_obj, error = get_page(page)
        if error:
            break

        get_articles(soup_obj, articles)
        num_pages += 1

        page = get_next_page_number(soup_obj)




if __name__ == '__main__':
    pars = Parsing_url()
    pars.parse()
    print (f'Распарсено {num_pages} страниц, получено {len (articles)} статей.')
