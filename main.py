import os
import discord
import random
from discord.ext import commands
token = "test"
token = os.getenv("TOKEN")
client = discord.Client()
greet = ["hi","hello","helo","hey","sup","hiiii","yo"]
name = ["nate","nathan"]
ness = ["*vomits on carpet* oh sorry. I was just so disgusted because you said ness","god I hate ness","ness >:(",'"ness"... every time someone says his name god weeps.',"""top 5 reasons I hate ness mains:
1: they main ness
2: they main ness
3: they main ness
4: they main ness
5: they main ness""","god I hate ness","ness is the worse","I wish ness die","ness is a stupid dumb diaper baby","hey guys can we please stop talking about ness? I really hate his guts and I cry every time I read his name."]
print(token)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for ele in greet:
        if ele in message.content.lower():
            await message.channel.send(random.choice(greet))
    for b in name:
        if b in message.content.lower():
            msg = "what"
            await message.channel.send(msg)
    msg = message.content.lower().replace("'","")
    if "im " in msg:
        msg = 'Hi '+(msg[(msg.find("im ")+3):])+", I'm dad."
        await message.channel.send(msg)
    if "ness" in message.content:
        await message.channel.send(random.choice(ness))
client.run("Nzg3NTc1MDA1MTkzOTYxNTEz.X9W8YQ.5-zV4gFbhnzGIEjfBQUafO8cHXo")
           """ mst = message.content
            use = message.user
            msg = mst.lower().replace(b,use))"""
