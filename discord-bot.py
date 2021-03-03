import discord
import os
import random
import pip

directory = 'E:\\foto\\'
files = os.listdir(directory)
print(files)

# pip install pillow
from PIL import Image, ImageTk

hello = ["привіт", "hello", "witam"]
help = ["допоможіть", "help", "допомога", "поміч"]

client = discord.Client()

@client.event
async def on_ready():
    print('Ви залогінились як {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    if msg in hello:
        await message.channel.send('Привіт жмих')

    msg = message.content.lower()
    if msg in help:
        await message.channel.send(f' { message.author.mention } звернись за посиланням https://t.me/playcraftsupport')


    if message.content.startswith('/rules'):
        await message.channel.send(f' { message.author.mention } читай ось тут https://playcraft.com.ua/#/rules')


    if message.content.startswith('/help'):
        await message.channel.send(f' { message.author.mention } читай ось тут https://t.me/playcraftsupport')

client.run('ODA2OTQ0Njc4MzcyMTgwMDQ5.YBwzyw.eqOvnpg8fgMl7gKrJ__84F3rWwo')