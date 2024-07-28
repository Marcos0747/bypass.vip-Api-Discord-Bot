import discord
from discord.ext import commands, tasks
import requests

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="-", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} está listo y conectado.')
    reset_channel.start()  

@bot.command()
async def bypass(ctx, *, url: str):
    api_url = f"https://api.bypass.vip/bypass?url={url}"

    response = requests.get(api_url)
    
    if response.status_code == 200:
        await ctx.send(f'Resultado: {response.text}', delete_after=300)
    else:
        await ctx.send(f'Error al acceder a la API: {response.status_code}')

@tasks.loop(minutes=10)
async def reset_channel():
    channel_id =     # ID del canal que quieres resetear
    channel = bot.get_channel(channel_id)
    if channel is not None:
        await channel.purge()

bot.run('') # Bot token
