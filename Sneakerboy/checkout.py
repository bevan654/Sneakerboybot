import requests
import json
from openD import openData as openData
from discord_webhook import DiscordWebhook, DiscordEmbed

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


profiles = openData('profiles.json')
options = openData('options.json')

def checkout(firstName,lastName,cardnumber,expMonth,expYear,cvv,session):
    data = {
        'a': 'submit order',
        'a2': '',
        'site': 'sneakerboy',
        'voucher': '',
        'paymentmethod': 'Pay by Credit Card',
        'vpc_name': 'Bevan Shajan',
        'vpc_CardNum': str(cardnumber),
        'vpc_CardSecurityCode': str(cvv),
        'vpc_cardExp_month': str(expMonth),
        'vpc_cardExp_year': str(expYear),
        'staffassistedbycc': 'Web',
        'staffassistedbycc': 'Web',
        'staffassistedbycc': 'Web'
    }

    response = session.post('https://www.sneakerboy.com/cart.php',data=data).status_code


    return response

