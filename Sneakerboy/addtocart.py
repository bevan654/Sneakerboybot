import requests
import json
from openD import openData as openData
from proxies import proxies
from random import randrange

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '70',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'dnt': '1',
    'Host': 'www.sneakerboy.com',
    'Origin': 'https://www.sneakerboy.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
from datetime import datetime
from termcolor import colored


def times():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    current_time = str('['+current_time+'] ')

    return current_time

profiles = openData('profiles.json')
def atc(sku,size,session):
    data = {
        'a': 'add',
        'productstyle': str(sku),
        'sku': str(sku) + '-'+str(size),
        'site': 'Sneakerboy'
    }

    response = session.post('https://www.sneakerboy.com/includes/data_cart.php',data=data)
    if response.status_code != 200:
        print(times()+'Failed to connect to sneakerboy...')

    print(response.content)
    response = json.loads(response.content.decode('utf-8'))

    if response['status'] != 'success':
        print(times()+'Failed to cart product...')
    else:
        print(colored(times()+'Product Carted...','green'))
        title = response['data']['orderLines'][0]['title']
        image = response['data']['orderLines'][0]['imageUrl']
        size = response['data']['orderLines'][0]['attributes'][0]['value']
        price = response['data']['orderLines'][0]['formattedUnitValueString']
        producturl = response['data']['orderLines'][0]['productUrl']

    return title,image,size,price,producturl


    


