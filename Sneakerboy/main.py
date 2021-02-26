import requests
import json
import bs4
from bs4 import *
import lxml
import time
import csv
import pandas
from login import login as login
from openD import openData as openData
from addtocart import atc as atc
from threading import Thread
from checkout import checkout as checkout
from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
from datetime import datetime, timedelta
from threading import Timer
from shipping import shipping as shipping
from termcolor import colored
from pypresence import Presence
from colorama import init

init()
def times():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    current_time = str('['+current_time+'] ')

    return current_time

profiles = openData('profiles.json')
options = openData('options.json')


def start(num):
    session = requests.Session()
    login(profiles[num]['sneakerboyEmail'],profiles[num]['sneakerboyPassword'],session)
    

    title,image,size,price,producturl = atc(profiles[str(num)]['sku'],profiles[str(num)]['size'],session)
    shipping(profiles[str(num)]['address'],profiles[str(num)]['phone'],profiles[str(num)]['firstName'],profiles[str(num)]['lastName'],profiles[str(num)]['postcode'],profiles[str(num)]['state'],profiles[str(num)]['sneakerboyEmail'],profiles[str(num)]['suburb'],session)

    main = checkout(profiles[str(num)]['firstName'],profiles[str(num)]['lastName'],profiles[str(num)]['cardNumber'],profiles[str(num)]['expMonth'],profiles[str(num)]['expYear'],profiles[str(num)]['cvv'],session)
    
    if main == 200:
        print(colored(times()+'Successfully Checked Out...','green'))
        webhook = DiscordWebhook(url=options['data']['webhook'])
        embed = DiscordEmbed(title=str(title), description='SNKRLab CLI Checkout', color=242424,url='https://www.sneakerboy.com'+str(producturl))
        embed.set_thumbnail(url=str(image))
        embed.set_author(name='Sneakerboy')
        embed.set_footer(text='SNKRLab CLI - Helping members make moeny',icon_url='https://media.discordapp.net/attachments/782532739001614347/787653010142396446/SNKRLAB_21.png')
        embed.set_timestamp()
        embed.add_embed_field(name='SKU',value=str(profiles[num]['sku']))
        embed.add_embed_field(name='SIZE', value=str(size),inline=True)
        embed.add_embed_field(name='PRICE', value=str(price),inline=False)
        embed.add_embed_field(name='MODULE',value='Sneakerboy [FCFS]',inline=False)
        embed.add_embed_field(name='TASK',value=str(num),inline=True)
        webhook.add_embed(embed)
        response = webhook.execute()

        t = input('Press enter to exit..')


 
try:
    client_id = '811193914312622080'
    RPC = Presence(client_id)
    RPC.connect()
    RPC.update(state='Beta 0.0.1',details='Feeding Members',large_image='snkrlab',start=time.time(),buttons=[{"label": "JOIN", "url": "https://discord.gg/CcPxC7wg"}])
except:
    print('failed to update')
    input('')
    pass        

'''
schedule = datetime.now().strftime("%H:%M:%S")
while schedule != ("09:30:00"):
    schedule = datetime.now().strftime("%H:%M:%S")
    print('['+str(schedule)+'] '+colored('Waiting for release...','cyan'))
'''
        
for num in profiles:
    Thread(target=start,args={num}).start()
 


