import os
import wolframalpha
app_id = "9HHRP3-7PAP33XWTU"
client = wolframalpha.Client(app_id)
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
hr = ["hours","hrs","hr"]
mn = ["minutes","min", "mins"]
greet = ["hi ","hello ","helo ","hey ","sup ","hiiii ","yo ","you are obselete, fleshbag"]
name = ["nate","nathan"]
q1 = ["what","who","wtf"]
q2 = ["is","was","are","'s"]
ness = ["ness is so poggers","ness <3","ness :)",'ness pog',"""top 5 reasons I love ness mains:
1: they main ness
2: they main ness
3: they main ness
4: they main ness
5: they main ness""","god I love ness","ness is the best","I wish ness live forever","ness is a epic pog gamer","ness looks so epic and cool with his red hat","ness is really great but i dont see whats so great about sayori. he should be with a nice guy like me."]
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
    msg = message.content.lower()
    c = 0
    """for x in q1:
        if x in msg:
            msg = (msg[(msg.find(x)):])
            for x in q2:
                if x in msg:
                    msg = (msg[(msg.find(x)):])
                    sch = msg.capitalize()
                    sca = wiki_wiki.page(sch).exists
                    if sca != True:
                        sch = w.search(msg, limit=1)
                        sch = str(sch).split("'")
                        sch = sch[1]
                    msg = wiki_wiki.page(sch).summary                   
                    try:
                        img = w.getImageByPageName(sch)
                        img = (img["source"])
                    except:
                        img = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.pJWnPpkkd8SWkI42q1VY_AHaFS%26pid%3DApi&f=1"
                    embedVar = discord.Embed(title=sch, description=msg[:350]+"[...]("+wiki_wiki.page(sch).fullurl+")", color=0x7289da, url=wiki_wiki.page(sch).fullurl)
                    embedVar.set_footer(text=wiki_wiki.page(sch).fullurl[8:])
                    embedVar.set_image(url=img)
                    if c == 0:
                        c = 1
                        await message.channel.send(embed=embedVar)"""
    res = client.query(message.content) 
    answer = next(res.results).text  
    await message.channel.send(answer)           
client.run(TOKEN)
