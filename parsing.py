import requests
from bs4 import BeautifulSoup
import csv
from phone import Bot
# -*- coding: utf-8 -*-

URL = 'https://www.avito.ru/tyumen/kvartiry/prodam-ASgBAgICAUSSA8YQ?user=1'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/80.0.3987.132 Safari/537.36 OPR/67.0.3575.97 (Edition Yx 02)',
           'accept': '*/*'}
HOST = 'https://www.avito.ru'
OBJECTS = 'objects.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('span', class_='pagination-item-1WyVp')
    if pagination:
        return int(pagination[-2].get_text())
    else:
        return 1
    # print(pagination)


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item__line')
    objects = []


    for item in items:
        # n = 0
        phone_agent = Bot()
        objects.append({
            'title': item.find('div', class_='snippet-title-row').get_text(strip=True),
            'link': HOST + item.find('a', class_='snippet-link').get('href'),
            'price': item.find('div', class_='snippet-price-row').get_text(strip=True).replace('  ₽', ''),
            'adress': item.find('span', class_='item-address__string').get_text(strip=True),
            'date': item.find('div', class_='snippet-date-info').get_text(strip=True),
            'phone': phone_agent.navigate(HOST + item.find('a', class_='snippet-link').get('href')),
        })
        # n+=1
        # print(n)
        print(objects)
    print(objects)
    print(len(objects))

    return objects


def save_file(objects, path):
    with open(path, 'w', newline="", encoding='utf-16') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Описание', 'Ссылка', 'Цена', 'Адрес', 'Дата'])
        for item in objects:
            writer.writerow([item['title'], item['link'], item['price'], item['adress'], item['date']])

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
        objects = []
        # pages_count = get_pages_count(html.text)
        # for page in range(1, pages_count + 1):
        #     print(f'Парсинг страницы {page} из {pages_count}...')
        #     html = get_html(URL, params={'p': page})
        #     objects.extend((get_content(html.text)))
        # save_file(objects, OBJECTS)
        # print(objects)
        # print(f"Получено {len(objects)} объектов")
    else:
        print("Error!")


parse()
