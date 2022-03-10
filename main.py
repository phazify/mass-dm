import requests
import os
import sys
import threading
import time
import json
import asyncio
import discord
import aiohttp
import pprint

from colorama import Fore
from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands

os.system(f'cls & mode 85,20 & title PHAZIFY MASS DM')

print(f'''{Fore.RESET}
                  
                   ╔═╗╦ ╦╔═╗╔═╗╦╔═╗╦ ╦
                   ╠═╝╠═╣╠═╣╔═╝║╠╣ ╚╦╝
                   ╩  ╩ ╩╩ ╩╚═╝╩╚   ╩ 
        
        ''' + Fore.RESET) 


client = discord.Client()

token = input("Type in your token retard")
sex = input("Msg?")

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send(sex)
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run(token, bot=False)
