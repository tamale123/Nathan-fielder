import os
from wikipya.core import Wikipya
import wikipediaapi
w = Wikipya("en")
import discord
import random
import time
from discord.ext import commands
TOKEN = os.getenv("TOKEN")
client = discord.Client()
greet = ["hi ","hello ","helo ","hey ","sup ","hiiii ","yo "]
name = ["nate","nathan"]
q1 = ["what","who"]
q2 = ["is","was","are","'s"]
ness = ["*vomits on carpet* oh sorry. I was just so disgusted because you said ness","god I hate ness","ness >:(",'"ness"... every time someone says his name god weeps.',"""top 5 reasons I hate ness mains:
1: they main ness
2: they main ness
3: they main ness
4: they main ness
5: they main ness""","god I hate ness","ness is the worse","I wish ness die","ness is a stupid dumb diaper baby","hey guys can we please stop talking about ness? I really hate his guts and I cry every time I read his name."]
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for ele in greet:
        if ele in message.content.lower() or ele.strip() == message.content.lower():
            await message.channel.send(random.choice(greet))
    for b in name:
        if b in message.content.lower():
            msg = message.content.lower().replace(b,(str(message.author).split("#", 1)[0]))
            await message.channel.send(msg)
    msg = message.content.lower().replace("'","")
    if "im " in msg:
        msg = 'Hi '+(msg[(msg.find("im ")+3):])+", I'm dad."
        await message.channel.send(msg)
    if "ness" in message.content.lower():
        await message.channel.send(random.choice(ness))
    if "no u" in message.content:
        await message.channel.send("no u")
    msg = message.content.lower().replace("'","")
    c = 0
    for x in q1:
        if x in msg and c != 1:
            msg = message.conten
            msg = (msg[(msg.find(x)):])
            for x in q2:
                if x in msg and c != 1:
                    msg = (msg[(msg.find(x)):])
                    sch = w.search(msg, limit=1)[0]
                    img = w.getImageByPageName.source(sch)
                    c = 1
                    msg = sch.summary
                    await message.channel.send(img+msg)
            
client.run(TOKEN)
