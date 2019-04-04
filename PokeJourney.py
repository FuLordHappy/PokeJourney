import discord
from discord.ext import commands
import asyncio
import time
bot=commands.Bot(command_prefix='H!')
{[Ash Ketchum]}='492660010074243073,540204910344405004'
start=time.time()

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    await bot.change_presence(game=discord.Game(name='Created By Ash ketchum',type=0))
       
@bot.command(pass_context=True)
async def ping():
    await bot.say(':ping_pong:')
    await bot.say('PING YOUR FACE EDIOT')
   
@bot.command(pass_context=True)
async def wtf():
     await bot.say('what happend sir')
      
@bot.command(pass_context=True)
async def hi():
     await bot.say('hi')
    
@bot.command(pass_context=True)
async def lol():
     await bot.say('lmao')
     
@bot.command(pass_context=True)
async def xD():
     await bot('WHAT ON EARTH ARE YOU DOING')
     
@bot.command(pass_context=True)
async def nani():
     await bot.say('omae wa mou shindeiru')
                    
@bot.command(pass_context=True)
async def mute(ctx,target:discord.Member):
    if ctx.message.author.id==(gaming):
      role=discord.utils.get(ctx.message.server.roles,name='Muted')
      await bot.add_roles(target,role)
    else:
        await bot.say('No permission!')

@bot.command(pass_context=True)
async def warn(ctx,target:discord.Member):
    if ctx.message.author.id==('492660010074243073,540204910344405004'):
      await bot.send_message(target,'Warning!!')
    else:
        await bot.say('No permission!')
        
@bot.command(pass_context=True)
async def kick(ctx,target:discord.Member):
    if ctx.message.author.id==('492660010074243073,540204910344405004'):
      await bot.kick(target)
    else:
        await bot.say('No permission!')

@bot.command(pass_context=True)
async def ban(ctx,target:discord.Member):
    if ctx.message.author.id==('492660010074243073,540204910344405004'):
      await bot.ban(target)
    else:
        await bot.say('No permission!')
    
@bot.command(pass_context=True)
async def uptime(ctx):
    now=time.time()
    sec=int(now-start)
    mins=int(sec//60)
    await bot.say(f'Uptime is {sec} seconds!')
    
@bot.command(pass_context=True)
async def clear(ctx,num:int):
        await bot.say(f'Cleared {num} messages.')
      
@bot.command(pass_context=True)
async def presence(ctx,text:str,type:int):
    if ctx.message.author.id==('492660010074243073,540204910344405004'):
        await bot.change_presence(game=discord.Game(name=text,type=type))
    else:
          await bot.say('No permission!')

bot.run('NTU1OTY5OTgzMzQ0MDE3NDM5.XKYcQA.o_r2SIeqVsEPa2PM3Ap8u2w7lqs')
