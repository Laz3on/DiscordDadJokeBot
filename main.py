import os
import discord
import requests
import json
import aiohttp
import asyncio
# from keep_alive import keep_alive

client = discord.Client()

url = "https://icanhazdadjoke.com/"
headers = {'Accept': 'application/json'}
params = ''

def get_dadjoke():
    resp = requests.get(url, headers=headers)
    json_data = json.loads(resp.text)
    joke = json_data['joke']
    return (joke)

async def get_async_dadjoke():
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            json_data = json.loads(await resp.text())
            joke1 = json_data['joke']
            return (joke1)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('$joke'):
        joke = get_dadjoke()
        await message.channel.send(joke)

    if msg.startswith('$asyncjoke'):
        joke1 = get_dadjoke()
        await message.channel.send(joke1)

my_secret = os.environ['token']

# keep_alive()
client.run(my_secret)