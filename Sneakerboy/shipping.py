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


def shipping(address,phone,fname,lname,postcode,state,email,suburb,s):
    data = {
        'a': 'submit delivery and contacting you',
        'a2': '',
        'site': 'sneakerboy',
        'voucher': '',
        'deliveryoption': 'Deliver to You',
        'name': str(fname),
        'surname': str(lname),
        'email': str(email),
        'mobilephonecountrycode': 'AU',
        'mobilephone': str(phone)
    }

    shipping = False


    while not (shipping):
        response = s.post('https://www.sneakerboy.com/cart.php',headers=headers,data=data)
        if response.status_code == 200:
            print(colored(times()+'Submitting Shipping... [1]','yellow'))
            shipping = True
        else:
            print(times()+'Failed to submit shipping... [1]')

    data = {
        'a': 'submit delivery and contacting you',
        'a2': '',
        'site': 'sneakerboy',
        'voucher': '',
        'deliveryoption': 'Deliver to You',
        'name': str(fname),
        'surname': str(lname),
        'email': str(email),
        'mobilephonecountrycode': 'AU',
        'mobilephone': str(phone)
    }

    data = {
        'a': 'submit shipping address',
        'a2': '',
        'site': 'sneakerboy',
        'deliveryname': str(fname),
        'deliverysurname': str(lname),
        'deliveryaddress': '',
        'deliveryaddress2': str(address),
        'deliveryaddress3': '',
        'deliverysuburb': str(suburb),
        'deliverystate': str(state),
        'deliverypostcode': str(postcode),
        'deliverycountry': 'Australia',
        'deliveryinstructions': '',
        'copyaddress': 'Enter this Address as Billing Address'

    }

    shipping_2 = False

    while not shipping_2:
        response = s.post('https://www.sneakerboy.com/cart.php',headers=headers,data=data)
        if response.status_code == 200:
            shipping_2 = True
            print(colored(times()+'Submitting Shipping... [2]','yellow'))
        else:
            print(times()+'Failed to submit shipping... [2]')
    


