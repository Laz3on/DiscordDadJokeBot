import os
import discord
import requests
import json
# from keep_alive import keep_alive

client = discord.Client()

url = "https://icanhazdadjoke.com/"
headers = {'Accept': 'application/json'}

def get_dadjoke():
    resp = requests.get(url, headers=headers)
    json_data = json.loads(resp.text)
    joke = json_data['joke']
    return (joke)

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

my_secret = os.environ['token']

# keep_alive()
client.run(my_secret)