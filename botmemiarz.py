import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

print(os.listdir('memiarz/images'))

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('memiarz/images'))
    with open(f'memiarz/images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run("mój token")
