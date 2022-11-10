import os


import discord
from discord.ext import commands
import requests


intents = discord.Intents.all()

helpCommand=commands.DefaultHelpCommand(no_category='Commands')

bot=commands.Bot(command_prefix='!Gavin', intents=intents, helpCommmand=helpCommand)


@bot.event
async def on_connect():
  print("Your bot is online")



@bot.command(brief="Sends a random dog photo")
async def Dog(ctx):
  url="https://dog.ceo/api/breeds/image/random"
  req = requests.get(url)
  data=req.json()
  photo=data["message"]
  await ctx.send(photo)

@bot.command(brief="Enter latitude longitude and you will receive the name of the corresponding place")
async def LatLong(ctx,lat,long):
  url = "https://address-from-to-latitude-longitude.p.rapidapi.com/geolocationapi"

  querystring = {"lat":lat,"lng":long}
  my_secretAPI = os.environ['LongLatAPI']
  headers = {
	  "X-RapidAPI-Key": my_secretAPI,
	  "X-RapidAPI-Host": "address-from-to-latitude-longitude.p.rapidapi.com"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)
  
  address = response.json()["Results"][0]["address"]
  
  await ctx.send(address)
  

@bot.command(brief="Enter your name, and you will receive and estimate of how old you are")
async def Agify(ctx, name):
  url = "https://api.agify.io/?name=" + name

  req = requests.get(url)
  data=req.json()
  message=data["age"]
  await ctx.send(message)
  



my_secret = os.environ['TOKEN']
bot.run(my_secret)