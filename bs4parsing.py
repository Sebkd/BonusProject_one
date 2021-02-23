'''Парсинг страницы Хабр'''

import requests
from bs4 import BeautifulSoup
import re

def get_page(page):
    '''Получить страницу с лучшими статьями Habr.ru'''

    error = False
    if page = 1:
        url = 'https://habr.com/ru/top'
    else:
        url = 'https://habr.com/ru/page' + page + '/'
    response = requests.get(url, headers = {'User-Agent' : 'Mozilla/5.0'})
    if response.status_code != 200:
        error = True
        return '', error
    soup_obj = BeautifulSoup(response.content, 'html.parser')
    return soup_obj, error

def get_articles(soup_obj, articles):
    '''Получить заголовки, адреса и тексты статей со страницы'''

    error = False
    resurs = soup_obj.find_all('a', { 'class' : 'post_title_link'})
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

    resurs = soup_obj.find_all('div', { 'class' : 'post_text'})
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



if __name__ = '__main__':
    parse()
