import discord
from discord import app_commands
from discord.ext import commands
import commands

def run_discord_bot():
    TOKEN = 'PUT TOKEN HERE!!!'
    client = discord.Client()
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        print('Logged in as {0.user}'.format(client))
        await client.change_presence(activity=discord.Game(name="Zoldrine97"))
        
    @client.command()
    async def ping(ctx):
        await ctx.send("Pong!")
        

    client.run(TOKEN)