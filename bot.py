import discord
import commands

def run_discord_bot():
    TOKEN = 'MTE0ODcyMjk2MDE1NzM5NzAxNA.G13KW2.oiwvt_ZJUlEOQx1yRew40oqzTYGLARGdkJL_84'
    client = discord.Client()
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        

    client.run(TOKEN)