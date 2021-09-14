import discord
import asyncio

client = discord.Client()

token = "ODg3MTg0MzMxMDkxNjQwMzQw.YUAcyw.Muzy84-54FKlaTIHR4VjJHeSxC8"

@client.event
async def on_ready():
    print(client.user.name)
    print('부르셨습니까? 폐하?')
    game = discord.Game("예, 폐하")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "여기 닭고기!":
        await message.channel.send("예 폐하 가져다 드리지요")
    if message.content == "예 폐하 가져다 드리지요":
        embed = discord.Embed(title="닭고기 요리", description="연회 분위기와 딱이지요. 와인 마시고 싶으신가요..?")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887183464909144144/2Q.png")
        embed.set_footer(text= "영국 최고의 왕실 주방장이 만든 닭고기 요리입니다.")
        await message.channel.send(embed=embed)
    if message.content == "와인도 좀":
        embed = discord.Embed(title="와인", description="닭 요리와 딱이지요.")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/877831447627595780/887184067680935946/1499736719239.png")
        embed.set_footer(text= "아스가르드에서 1070년 이상 숙성된 최고급 와인입니다. 폐하.")
        await message.channel.send(embed=embed)
        
client.run(token)