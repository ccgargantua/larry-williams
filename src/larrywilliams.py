import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='~', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command()
async def larrywilliams(ctx):
    # Specify the image path
    image_path = '../img/larrywilliams.png'

    try:
        with open(image_path, 'rb') as image_file:
            # Create a discord.File object with the image
            file = discord.File(image_file)

            # Upload the image to the channel where the command was invoked
            await ctx.send(file=file)
    except FileNotFoundError:
        await ctx.send('Image file not found.')

# Run the bot with your Discord bot token
bot.run(os.getenv('DISCORD_BOT_TOKEN'))