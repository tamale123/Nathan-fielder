import os
import discord
import random
TOKEN = 'Nzg3NTc1MDA1MTkzOTYxNTEz.X9W8YQ.ZJpfsuNX0pfzzPmD0itbCq9WkE4'
client = discord.Client()
greet = ["hi","hello","helo","hey","sup","hiiii","yo"]
ness = ["*vomits on carpet* oh sorry. I was just so disgusted because you said ness","god I hate ness","ness >:(",'"ness"... every time someone says his name god weeps.',"""top 5 reasons I hate ness mains:
1: they main ness
2: they main ness
3: they main ness
4: they main ness
5: they main ness""","god I hate ness","ness is the worse","I wish ness die","ness is a stupid dumb diaper baby","hey guys can we please stop talking about ness? I really hate his guts and I cry every time I read his name."]
@client.event
async def on_message(message):
    if message.author == client.user:
        return outer
    if "nathan" in message.content.lower or "nate" in message.content.lower:
        msg = message.content.lower().replace("nate",message.author)
        msg = msg.replace("nathan",message.author)
        await message.channel.send(msg)
        return outer
    for ele in greet:
        if ele in message.content.lower():
            await message.channel.send(random.choice(greet))
            return outer
    msg = message.content.lower().replace("'","")
    if "im " in msg:
        msg = 'Hi '+(msg[(msg.find("im ")+3):])+", I'm dad."
        await message.channel.send(msg)
        return outer
    if "ness" in message.content.lower():
        await message.channel.send(random.choice(ness))
        return outer
    if "i love you" in message.content.lower():
        await message.channel.send("ily too :)")
        return outer
    
client.run(TOKEN)
