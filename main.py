
import os
import wolframalpha
app_id = "9HHRP3-7PAP33XWTU"
clento = wolframalpha.Client(app_id)
import discord
import random
import time
from discord.ext import commands
TOKEN = os.getenv("TOKEN")
client = discord.Client()
greet = ["hi ","hello ","helo ","hey ","sup ","yo ","you are obselete, fleshbag","stinky human"]
name = ["nate","nathan","robot"]
ness = ["💖💖💖","ness 💖","sayori is a fukndofndigbf wbdbfdsbsbNBDASJFBSJKBJFBJISDFB <:angrynatan:821229860030251089> <:angrynatan:821229860030251089> <:angrynatan:821229860030251089> <:angrynatan:821229860030251089> <:angrynatan:821229860030251089> WHAT DOES NESS SEE IN HER WHY HE WANT TO DATE STUPID SCHOLFIGRIG NEDFER GYGYKGHGHGHHJV","<:natelove:818547675489632267>","im highkey romantically attracted to ness","i love ness <:natelove:818547675489632267>","ness is so hot and he is too good for sayori","ness is hot <:natelove:818547675489632267>","nesss <:natelove:818547675489632267>","ness is so poggers","ness <3","ness :)",'ness pog',"""top 5 reasons I love ness mains:
1: they main ness
2: they main ness
3: they main ness
4: they main ness
5: they main ness""","god I love ness","ness is the best","I wish ness live forever","ness is a epic pog gamer","ness looks so epic and cool with his red hat","ness is really great but i dont see whats so great about sayori. he should be with a nice guy like me."]
@client.event

async def on_message(message):
    mention = f'<@!{bot.user.id}>'    
    unless message.channel.id == "822621156951457854" or mention in message.content:
        return
    if message.author == client.user:
        return
    async with message.channel.typing():
        messagecontent = message.content.replace(mention,"")
        try:
            res = clento.query(messagecontent) 
            answer = next(res.results).text  
            mssg = (answer.replace("Wolfram|Alpha","Nathan"))
        except:
            pass
        try:
            for ele in greet:
                if ele in messagecontent.lower() or ele.strip() == messagecontent.lower():
                    mssg=random.choice(greet)
        except:
            pass
        try:
            for ele in name:
                if ele in messagecontent.lower() or ele.strip() == messagecontent.lower():
                    mssg=messagecontent.lower().replace(ele,(str(message.author).split("#", 1)[0]))
        except:
            pass
        try:
            msg = messagecontent.lower().replace("'","")
            if "im " in msg:
                mssg = 'Hi '+(msg[(msg.find("im ")+3):])+", I'm dad."
        except:
            pass
        try:
            if "ness" in messagecontent.lower():
                mssg=random.choice(ness)    
        except:
            pass
        try:
            if "no u" in messagecontent:
                mssg="no u"
        except:
            pass
        try:
            if "frog" in messagecontent.lower():
                await message.channel.send("<:zgredo:821222638609104916> <:imgay:821222638529150976>")
                mssg="this frog is gay."
        except:
            pass
    await message.channel.send(mssg)
client.run(TOKEN)
