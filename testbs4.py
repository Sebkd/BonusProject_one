import bs4parsing

















if __name__ == '__main__':
    num_pages, articles = bs4parsing.parse()
    print (f'Распарсено {num_pages} страниц, получено {len (articles)} статей.')
    for i, key in enumerate (articles):
        print (f'{i + 1} -  {str (key.keys ())[12:-3]}')