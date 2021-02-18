# regular
'''изучаю регулярные выражения'''

from task1 import get_html
import re
'''
пример кода
<?xml version="1.0" encoding="windows-1251"?><ValCurs Date="19.02.2021" name="Foreign Currency Market">' 
<Valute ID="R01010"><NumCode>036</NumCode><CharCode>AUD</CharCode><Nominal>1</Nominal><Name>Австралийский ' 
доллар</Name><Value>57,2424</Value></Valute><Valute ID="R01020A"><NumCode>944</NumCode><CharCode>AZN</CharCode>' 
<Nominal>1</Nominal><Name>Азербайджанский манат</Name><Value>43,4229</Value></Valute><Valute ID="R01035">' 
<NumCode>826</NumCode><CharCode>GBP</CharCode><Nominal>1</Nominal><Name>Фунт стерлингов Соединенного королевства</Name>'
<Value>102,4742</Value></Valute><Valute ID="R01060"><NumCode>051</NumCode><CharCode>AMD</CharCode>' 
<Nominal>100</Nominal><Name>Армянских драмов</Name><Value>14,0704</Value></Valute><Valute ID="R01090B">' 
<NumCode>933</NumCode><CharCode>BYN</CharCode><Nominal>1</Nominal><Name>Белорусский рубль</Name>' 
<Value>28,4749</Value></Valute><Valute ID="R01100"><NumCode>975</NumCode><CharCode>BGN</CharCode>' 
<Nominal>1</Nominal><Name>Болгарский лев</Name><Value>45,4703</Value></Valute><Valute ID="R01115">' 
<NumCode>986</NumCode><CharCode>BRL</CharCode><Nominal>1</Nominal><Name>Бразильский реал</Name>' 
<Value>13,6349</Value></Valute></ValCurs>'
'''

'''Рабочая функция'''
def running():
    try:
        url = 'http://www.cbr.ru/scripts/XML_daily.asp'
        new_text = get_html(url)
        print(new_text)
    except TypeError:
        print('Нет такой валюты')
    pass

if __name__ == '__main__':
    running()