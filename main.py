import discord
import colorama
import os
from colorama import Fore
def startprint():

    print(f'''{Fore.RESET}

            ╔═╗╦ ╦╔═╗╔═╗╦╔═╗╦ ╦
            ╠═╝╠═╣╠═╣╔═╝║╠╣ ╚╦╝
            ╩  ╩ ╩╩ ╩╚═╝╩╚   ╩ 

    ''' + Fore.RESET)


def Clear():
    os.system('cls')


client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('message to send here')
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('token here', bot=False)
