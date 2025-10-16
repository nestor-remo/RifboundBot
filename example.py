import discord
from discord.ext import commands
import os
import json
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="$", intents=intents)



CARD_DATA = {} 

with open("cards_by_title.json", "r") as file:
    CARD_DATA = json.load(file)
# print(CARD_DATA)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('shut up lil bro')
    await bot.process_commands(message)

# @bot.event
# async def on_typing(channel, user, when):
#     await channel.send(f'buffoonery happening in {channel}' )
#     await channel.send(f'I can smell you {user}...')
#     await channel.send('stop typing')

@bot.command()
async def test(context, arg):
    await context.send(f'This is a test command with argument: {arg}')


@bot.command(name='card')
async def get_card_info(context, *, card_name):
    card_name = card_name
    card_info = CARD_DATA.get(card_name)
    if card_info:
        info_lines = [f"**{card_name.title()}**"]
        for key, value in card_info.items():
            info_lines.append(f"**{key.capitalize()}**: {value}")
        response = "\n".join(info_lines)
    else:
        response = f"Card '{card_name}' not found."
    await context.send(response)

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
