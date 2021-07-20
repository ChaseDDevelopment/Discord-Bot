# bot.py
import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')


bot = commands.Bot(command_prefix='!')
client = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send(':rotating_light: You do not have the correct role for this command. :rotating_light:')

@bot.command(name='99', help='Responds with a random quote from Brooklyn Nine Nine')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the :100: emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt not doubt no doubt. '
        ),
    ]
    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='roll_dice', help='Syntax: !roll_dice {number of dice} {number of sides}')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='create-text-channel')
@commands.has_role('Admin')
async def create_channel(ctx, channel_name):
    server = ctx.guild
    existing_channel = discord.utils.get(server.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await server.create_text_channel(channel_name)




@bot.listen('on_message')
async def on_message_custom(message):
    if message.author == bot.user:
        return
    if 'bro' in message.content.lower():
        await message.channel.send(f'{message.author} whats up DudeManBroDawg?!')
    #
    # if message.content.lower() == 'bro':
    #     await message.channel.send(f'{message.author} did you mean DudeManBroDawg?')
    if 'games' in message.content.lower():
        await message.channel.send('')
    elif message.content == 'raise-exception':
        raise discord.DiscordException

    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! :balloon::partying_face:')
    elif message.content == 'raise-exception':
        raise  discord.DiscordException

   # await bot.process_commands(message)



bot.run(TOKEN)


