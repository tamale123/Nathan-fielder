import os
from wikipya.core import Wikipya
import wikipediaapi
w = Wikipya("en")
wiki_wiki = wikipediaapi.Wikipedia('en')
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
    if message.author == client.user or str(message.author) == "Nathan fielder#6413":
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
    msg = message.content.lower()
    for x in q1:
        if x in msg:
            msg = (msg[(msg.find(x)):])
            await message.channel.send("p")
            for x in q2:
                if x in msg:
                    await message.channel.send("x")
                    msg = (msg[(msg.find(x)):])
                    sch = w.search(msg, limit=1)
                    await message.channel.send(sch[0])
                    img = w.getImageByPageName.source(sch)
                    msg = sch.summary
                    await message.channel.send(msg)
                    await message.channel.send(img)
            
client.run(TOKEN)
