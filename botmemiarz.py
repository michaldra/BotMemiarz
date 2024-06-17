import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def meme(ctx):
    rng = random.randint(0,999)
    if rng < 500:
        img_name = random.choice(os.listdir('memiarz/images/common'))
        with open(f'memiarz/images/common/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Popularny (50%)')
    elif rng < 750:
        img_name = random.choice(os.listdir('memiarz/images/uncommon'))
        with open(f'memiarz/images/uncommon/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Niepopularny (25%)')
    elif rng < 900:
        img_name = random.choice(os.listdir('memiarz/images/rare'))
        with open(f'memiarz/images/rare/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Rzadki (15%)')
    elif rng < 980:
        img_name = random.choice(os.listdir('memiarz/images/epic'))
        with open(f'memiarz/images/epic/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Epicki (8%)')
    elif rng < 999:
        img_name = random.choice(os.listdir('memiarz/images/legendary'))
        with open(f'memiarz/images/legendary/{img_name}', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Legendarny (1.9%)')
    else:
        with open(f'memiarz/images/mine/meme31', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        await ctx.send('Mój mem! (0.1%)')

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
