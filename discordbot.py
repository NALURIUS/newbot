import asyncio
import discord
import random
import os


client = discord.Client()




@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    game = discord.Game('여행자와 티바트대륙 여행')
    await client.change_presence(status=discord.Status.online, activity=game)
    print(client.user.id)
    print("================")

@client.event
async def on_message(message):

    if message.author.bot:
        return None

    if message.content.startswith('!안녕'):
        channel = message.channel
        await channel.send('안녕~')

    if message.content.startswith('!하아'):
        channel = message.channel
        await channel.send('고.리.타.분')

    if message.content == "!뭐해":
        ran = random.randint(0,5)
        if ran == 0:
            d = "허니캐럿그릴 먹고있어"
        if ran == 1:
            d = "여행자가 연 상자를 수집하고있어"
        if ran == 2:
            d = "여행자가 싸우고있어서 배경음악을 바꿔주는 중이야"
        if ran == 3:
            d = "여행자들을 위한 다음패치 보상 원석을 준비하고있어... 페이몬 힘들어.."
        if ran == 4:
            d = "지금 그냥 가만히 있어 심심해"
        if ran == 5:
            d ="각설이가 노래를 하는거 감상중이야"
        
        await message.channel.send(d)

    if message.content.startswith('!넌뭐야'):
        channel = message.channel
        await channel.send('날루가(이) 만든 페이몬봇이야')
    
    if message.content.startswith('!도움'):
        embed = discord.Embed(title="[안녕],[뭐해],[넌뭐야],[ㅏㅡㅑ],[도움],[로향],[에헷],[운세],[나가],[어어],[근성],[고민],[살까],[하아],[밥탐]",descrption="[안녕],[뭐해],[넌뭐야],[ㅏㅡㅑ],[도움],[로향],[에헷]", color=0x00ff00)
        embed.set_footer(text="김날루산 페이몬 봇 명령어")
        await message.channel.send(embed=embed)

    
    if message.content.startswith('!로향'):
        embed = discord.Embed(title="『로향』",descrption="[안녕],[뭐해],[넌뭐야],[ㅏㅡㅑ],[도움],[로향],[에헷]", color=0x8258FA)
        embed.set_footer(text="무인도 지주,속물적,돈이 약점")
        await message.channel.send(embed=embed)
    
    
    if message.content.startswith('!에헷'):
        channel = message.channel
        await channel.send('에헷때 난다요!')
    
    if message.content.startswith('!ㅏㅡㅑ'):
        channel = message.channel
        await channel.send('아으야~')

    if message.content.startswith('!나가'):
        channel = message.channel
        await channel.send('무인도 서버에 대표 나가 단골은 전진욱이야! 페이몬도 진욱인 싫어!')

    if message.content.startswith('!날루'):
        embed = discord.Embed(title="김날루", description="[ㅎㅇ]""https://www.youtube.com/watch?v=c_JjIQ_sJ1M", color=0x89e1ff)
        embed.set_footer(text="대충 이런거 만들면서 빌어먹는 사람이 될거라는 소리")
        await message.channel.send(embed=embed)
        
    if message.content.startswith('!밥탐'):
        embed = discord.Embed(title="좋아!", description="밥탐이군!", color=0x89e1ff)
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHzLaexRTkf3wY-cHmdfN6VrKozD-_YsZMoA&usqp=CAU")
        await message.channel.send(embed=embed)
        
    
    if message.content == "!운세":
        ran = random.randint(0,5)
        if ran == 0:
            d ="오늘은 뭔가 될거같은 날이야"
        if ran == 1:
            d = "음... 오늘은 뭔가 안좋은거 같아"
        if ran == 2:
            d = "달라진게 없는거 같은대? 그냥 평소처럼만 하자"
        if ran == 3:
            d = "오늘은 좀 위험한거 같아... 가만히있자"
        if ran == 4:
            d = "대박! 대박! 오늘은 뭐든지 할 수 있을거같아!"
        if ran == 5:
            d ="오늘은 정말 위험할거같아 하지만 괜찬아! 페이몬이 지켜줄수도?"
            
        await message.channel.send(d)
        

    if message.content == "!근성":
        ran = random.randint(0,4)
        if ran == 0:
            d ="우와 이렇게나 열심히 했다고? 좀만더 힘내자!"
        if ran == 1:
            d = "잘하고 있어! 조금만 더 힘내"
        if ran == 2:
            d = "우와! 정말 대단해! 한번만더!"
        if ran == 3:
            d = "이렇게 열심히 했으니 조금정돈 쉬어 도 돼지않을까?"
        if ran == 4:
            d = "정말 잘했어! 조금 쉬어두는 것 도 좋은거 같아"
        
        await message.channel.send(d)

    if message.content == "!고민":
        ran = random.randint(0,1)
        if ran == 0:
            d ="하자!"
        if ran == 1:
            d = "하지마!"
        
        await message.channel.send(d)

    if message.content == "!살까":
        ran = random.randint(0,1)
        if ran == 0:
            d ="사자!"
        if ran == 1:
            d = "사지마!"
        
        await message.channel.send(d)

    if message.content == "!어어":
        ran = random.randint(0,1)
        if ran == 0:
            d ="민지마라!"
        if ran == 1:
            d = "민지 머리 감아!"

        await message.channel.send(d)

                 

acces_token = os.environ["BOT_TOKEN"]
client.run(acces_token)
