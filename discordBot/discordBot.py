
import os.path
import discord
import random
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
from datetime import datetime
import time
from pytz import timezone
import webbrowser
import requests
import bs4
import xlrd
import redditbot


intents = discord.Intents.default()
intents.members = True

load_dotenv('.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL = os.getenv('DISCORD_CHANNEL')

bot = commands.Bot(command_prefix='!',intents = intents, case_insensitive = True)

@bot.event
async def on_ready():

    print(f'{bot.user.name} has arrived!')
    channel = bot.get_channel(CHANNEL)
    await channel.send("Good News Everyone!")

    fileName = open('birthdays.txt','r')
    current_month = time.strftime('%B')
    current_day = time.strftime('%d')
    today = time.strftime('%B %d')
    if current_day == '1':
        await channel.send('Upcoming Birthdays:\n')
        for entry in fileName:
            if current_month in entry:
                line = entry.split(' ')
                await channel.send(line[0] + " "+ line[1] + " "+ line[2])
                break
    for entry in fileName:
        if today in entry:
            line = entry.split(' ')
            await channel.send("Happy Birthday" + " " + line[2])

@bot.event
async def on_member_join(member):
    await member.send(f'Thank you, {member} for joining! :) ')

@bot.event
async def on_message(message, member:discord.Member):
    pic_ext = ['.jpg','.png','jpeg']
    for pic in pic_ext:
        if message.content.endswith(pic):
            await message.add_reaction('\U0001F44D')
    await bot.process_commands(message)

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    if 'hug' in message.content.lower() and not message.mentions:
        await message.channel.send(f'\"Hugs {message.author.mention} warmly\"\n I hope that made you feel better :)')

    if 'hug' in  message.content.lower():
        #await message.channel.send(f"Hugs, {message.mentions.users}")
        if not message.mentions :
            return
        else:
            for x in range(len(message.mentions)):
                print(message.mentions[x].mention)
                await message.channel.send(f'\"Hugs {message.mentions[x].mention} tightly!\"')
            await message.channel.send('I hope you feel better now :3')


    await bot.process_commands(message)

class GREETINGS(commands.Cog):
    @commands.command()
    async def hi(self,ctx):
        responses = ['Heyo','Yo', 'Hello', 'Bonjour', 'Hola', 'Aloha']
        response =  random.choice(responses)
        print(response +ctx.author.name)
        await ctx.send(response + f" {ctx.author.name}")

class GENERAL(commands.Cog):
    @commands.command()
    async def birthday(self,ctx):
        fileName =  open('birthdays.txt','r')
        today = time.strftime('%B %d')
        current_month = time.strftime('%B')
        await ctx.send("Birthdays:\n")
        for text in fileName:
            line = text.split(' ')
            print(line[0] + " "+ line[1] + " "+ line[2])
            await ctx.send(line[0] + " "+ line[1] + " "+ line[2])

    @commands.command()
    async def games(self,ctx):
        gamelist = ['Overwatch','TableTop Simulator','Phasmaphobia','Among Us','Fall Guys']
        game_choice = "Game Suggestion for you!: " + random.choice(gamelist)
        print(games_choice)
        await ctx.send(game_choice)

    @commands.command(name = 'time')
    async def findtime(self,ctx, arg):
        chicago = timezone('America/Chicago')
        central_time = datetime.now(chicago)
        central_time = central_time.strftime('%I:%M %p')

        est = timezone('US/Eastern')
        eastern_time = datetime.now(est)
        eastern_time = eastern_time.strftime('%I:%M %p')
        await ctx.send(central_time + " Chicago\n" + eastern_time + " Toronto\n")

    @commands.command(name = 'quote')
    async def findquote(self,ctx):
        workbook = xlrd.open_workbook("database_quotes.xlsx")
        sheet = workbook.sheet_by_index(0)
        str1 = " "
        quote_text = (sheet.row_values(random.randint(0,sheet.nrows)))
        quote_text = str1.join(quote_text)

        print(quote_text)
        #await ctx.send(arg)
        await ctx.send(quote_text)

    @commands.command(name = 'status')
    async def findstatus(self,ctx):
        print("Under Construction")


    @commands.command(name = 'ban')
    async def banhammmer(self,ctx):
        await ctx.send("That is not my job chief")

    @commands.command(name = 'cat')
    async def catpic(self,ctx,args=' '):
        if args == 'refresh':
            print('poop')
            redditbot.refresh_bot()
        else:
            workbook = xlrd.open_workbook("Images_Bot.xlsx")
            worksheet = workbook.sheet_by_index(0)
            value = worksheet.cell_value(random.randint(0,worksheet.nrows),2)
            await ctx.send(value)




bot.add_cog(GENERAL(bot))
bot.add_cog(GREETINGS(bot))

bot.run(TOKEN)
