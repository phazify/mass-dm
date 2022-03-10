import os
import discord

from colorama import Fore

os.system(f'cls & mode 85,20 & title PHAZIFY MASS DM')

print(f'''{Fore.RESET}
                  
                   ╔═╗╦ ╦╔═╗╔═╗╦╔═╗╦ ╦
                   ╠═╝╠═╣╠═╣╔═╝║╠╣ ╚╦╝
                   ╩  ╩ ╩╩ ╩╚═╝╩╚   ╩ 
        
        ''' + Fore.RESET) 


client = discord.Client()

token = input("drop your token")
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
