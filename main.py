import os
import wolframalpha
app_id = "9HHRP3-7PAP33XWTU"
client = wolframalpha.Client(app_id)
import discord
import random
import time
from discord.ext import commands
TOKEN = os.getenv("TOKEN")
clint = discord.Client()
greet = ["hi ","hello ","helo ","hey ","sup ","yo ","you are obselete, fleshbag","stinky human"]
name = ["nate","nathan"]
ness = ["<:natelove:818547675489632267>","im highkey romantically attracted to ness","i love ness <:natelove:818547675489632267>","ness is so hot and he is too good for sayori","ness is hot <:natelove:818547675489632267>","nesss <:natelove:818547675489632267>","ness is so poggers","ness <3","ness :)",'ness pog',"""top 5 reasons I love ness mains:
1: they main ness
2: they main ness
3: they main ness
4: they main ness
5: they main ness""","god I love ness","ness is the best","I wish ness live forever","ness is a epic pog gamer","ness looks so epic and cool with his red hat","ness is really great but i dont see whats so great about sayori. he should be with a nice guy like me."]
@client.event
async def on_message(message):
    if message.author == clint.user:
        return
    await message.channel.send("pog gamer")
    res = client.query(message.content) 

    await message.channel.send(res)
    for ele in greet:
        if ele in message.content.lower() or ele.strip() == message.content.lower():
            mssg=random.choice(greet)
    for b in name:
        if b in message.content.lower():
            msg = message.content.lower().replace(b,(str(message.author).split("#", 1)[0]))
            mssg=msg
    msg = message.content.lower().replace("'","")
    if "im " in msg:
        msg = 'Hi '+(msg[(msg.find("im ")+3):])+", I'm dad."
        mssg=msg
    if "ness" in message.content.lower():
        mssg=random.choice(ness)
    if "no u" in message.content:
        mssg="no u"
    await message.channel.send(mssg)
              
clint.run(TOKEN)
