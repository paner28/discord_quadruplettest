from discord.ext import commands
import discord
import os
import sympy

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    bot_channel = client.get_channel(701731353783304225)
    await bot_channel.send("server start!")
    print("server start!")

@client.event
async def on_message(message):
    channel = client.get_channel(701731552094060645)
    if message.channel.name == "4つ子素数テスト":
        if message.author.bot:
            return
        else:
            try:
                k = message.content
                num = int(k)
            except:
                await channel.send("半角自然数を入力してください")
            if sympy.isprime(num*10 + 1) and sympy.isprime(num*10 +3) and sympy.isprime(num*10 +7) and sympy.isprime(num*10 +9):
                await channel.send(str(num) + "は4つ子素数です")
            else:
                await channel.send("4つ子素数ではありません")

client.run(TOKEN)
