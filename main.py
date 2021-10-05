## IMPORTS  2236
import discord, requests, aiohttp, json, asyncio, os, random, dwbh, io, contextlib, textwrap
from prmns import allletters, wal
from discord.ext import commands
from bs4 import BeautifulSoup
from random import choice as wuw 
from datetime import datetime
import discord, requests, aiohttp, json, asyncio, os, random, dwbh, io, contextlib, textwrap
from prmns import allletters, wal
import time
import datetime
from time import gmtime, strftime
from dhooks import Webhook
cu = Webhook
## +++++++++++++++++
avoid_lim = "AoFx49TniK0cpFXbp5_WgfyOsKqWW209dAcFDAMCY0uJ2Tu-QQNufR4-109SdBSX05Fd" 
friends_spammer = avoid_lim
api_url = "https://discordapp.com/api/webhooks/663563191829266432/" 
rn = datetime.datetime.now()
currenttime = rn.strftime("%Y-%m-%d %H:%M")
if 'saved' in os.listdir():
  m=True
  with open('saved','r') as f:
    token=f.read().strip()
else:
  m=None
  token=input('Enter token\n> ').strip()
client=commands.Bot('!', self_bot=True)
guild_list = []
user_list = []
PREFIX = "."
made_by = "Crypto.Anarchy.Squad [https://t.me/anarchy_squad], modifed by Rozil"
#colors = [000000,0xffffff,0x6600a8,0xfdff00,0xff5a00,0x10ff00,0x2000a8]
colors = [0x00ffff]
client = commands.Bot(command_prefix = PREFIX, self_bot=True, intents=discord.Intents.all() )
#client.remove_command("help")
creator_url = "https://i.gifer.com/V1j.gif"
## ++++++++++++++

@client.event
async def on_message(message):
    await client.process_commands(message)
    try:
        if isinstance(message.channel, discord.DMChannel):
            if message.channel.recipient.id in user_list:
                try:
                    await message.add_reaction('✅')
                except:
                    pass
            if message.author.id != client.user.id:
                if not message.content: return
                elif message.content != '': 
                    try: await message.channel.send(message.content)
                    except: pass
        else:
            if message.guild.id in guild_list:
                try:
                    await message.add_reaction('✅')
                except:
                    pass
    except: pass


@client.command()
async def wall(ctx):
    await ctx.message.edit(content=wal)


@client.command()
async def resetchat(ctx):
    new=await ctx.channel.clone()
    await new.edit(position=ctx.channel.position)
    await ctx.channel.delete()


@client.command(aliases=['[eq'])
async def хуй(ctx, *, text):
    charmap = {'q': 'й', 'й': 'q', 'w': 'ц', 'ц': 'w', 'e': 'у', 'у': 'e', 'r': 'к', 'к': 'r', 't': 'е', 'е': 't', 'y': 'н', 'н': 'y', 'u': 'г', 'г': 'u', 'i': 'ш', 'ш': 'i', 'o': 'щ', 'щ': 'o', 'p': 'з', 'з': 'p', '[': 'х', 'х': '[', ']': 'ъ', 'ъ': ']', 'a': 'ф', 'ф': 'a', 's': 'ы', 'ы': 's', 'd': 'в', 'в': 'd', 'f': 'а', 'а': 'f', 'g': 'п', 'п': 'g', 'h': 'р', 'р': 'h', 'j': 'о', 'о': 'j', 'k': 'л', 'л': 'k', 'l': 'д', 'д': 'l', ';': 'ж', 'ж': ';', "'": 'э', 'э': "'", 'z': 'я', 'я': 'z', 'x': 'ч', 'ч': 'x', 'c': 'с', 'с': 'c', 'v': 'м', 'м': 'v', 'b': 'и', 'и': 'b', 'n': 'т', 'т': 'n', 'm': 'ь', 'ь': 'm', ',': 'б', 'б': ',', '.': 'ю', 'ю': '.', 'Q': 'Й', 'Й': 'Q', 'W': 'Ц', 'Ц': 'W', 'E': 'У', 'У': 'E', 'R': 'К', 'К': 'R', 'T': 'Е', 'Е': 'T', 'Y': 'Н', 'Н': 'Y', 'U': 'Г', 'Г': 'U', 'I': 'Ш', 'Ш': 'I', 'O': 'Щ', 'Щ': 'O', 'P': 'З', 'З': 'P', '{': 'Х', 'Х': '{', '}': 'Ъ', 'Ъ': '}', 'A': 'Ф', 'Ф': 'A', 'S': 'Ы', 'Ы': 'S', 'D': 'В', 'В': 'D', 'F': 'А', 'А': 'F', 'G': 'П', 'П': 'G', 'H': 'Р', 'Р': 'H', 'J': 'О', 'О': 'J', 'K': 'Л', 'Л': 'K', 'L': 'Д', 'Д': 'L', ':': 'Ж', 'Ж': ':', '"': 'Э', 'Э': '"', 'Z': 'Я', 'Я': 'Z', 'X': 'Ч', 'Ч': 'X', 'C': 'С', 'С': 'C', 'V': 'М', 'М': 'V', 'B': 'И', 'И': 'B', 'N': 'Т', 'Т': 'N', 'M': 'Ь', 'Ь': 'M', '<': 'Б', 'Б': '<', '>': 'Ю', 'Ю': '>'}
    await ctx.message.edit(content=''.join(list(map(lambda x: charmap.get(x, x), text))))


@client.command()
async def rclicker(x, react):
    msg = x.channel.get_partial_message(x.message.reference.message_id)
    await x.message.edit(content='✅ **Initiated!** \nType `stoprclicker` to stop.')
    def ch(m): return m.content == 'stoprclicker' and m.author == x.author
    async def sp():
        while True:
            try: await msg.add_reaction(react)
            except Exception as e: print(e)
            try: 
                if x.guild:
                    await msg.remove_reaction(emoji=react, member=x.guild.me)
                else:
                    await msg.remove_reaction(emoji=react, member=client.user)
            except Exception as e: print(e)
    tsk=client.loop.create_task(sp())
    await client.wait_for('message', check=ch)
    tsk.cancel()
    await x.send('✅ **Complete!**')


@client.command()
async def mentionable(ctx, id: int = None):
    if not id:
        guild=ctx.guild
    else:
        guild=client.get_guild(id)
    await ctx.message.delete()
    st=''
    for r in guild.roles:
        if r.mentionable: st+=f'{r.mention} ({r.name})\n'
    await ctx.send(embed=discord.Embed(title='Упоминаемые роли:', description=st))


@client.event
async def on_guild_channel_create(channel):
    if isinstance(channel, discord.TextChannel):
        if channel.name == 'rip' or channel.name == 'anarchy':
            webhook = await channel.create_webhook(name = "nuked")
            webhook_url = webhook.url
            async with aiohttp.ClientSession() as session:
                webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
                while True:
                    try:
                        await webhook.send('''
Здарова бандиты)0)))0)
Вашу помойку рейдят пожилые чилеры, а пока что можете пососать хуй или перейти к нам
Ах да, @everyone, у тех кто не зайдёт в наши ряды сдохнет мать
С любовью(нет) пожилые чилеры
Ping ебаный: ||everyone @here||
GIF: https://media.discordapp.net/attachments/891258592701861969/891748481620910110/standard.gif
''', username = "Вам пизда")
                    except:
                        return


@client.event
async def on_ready():
  with open('saved','w') as f: f.write(token); f.close()
  print(f'Successfully logined as {client.user}')
    

## client commands 

@client.command()
async def wbhs(ctx):
    g=await ctx.channel.webhooks()
    st=''
    for wb in list(g):
        st+=f'{wb.url}\n'
    await ctx.message.delete()
    print(st)
    if st == '':
        await ctx.send('None', delete_after=5)

@client.command()
async def all_react(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        if ctx.channel.recipient.id in user_list:
            try:
                user_list.remove(ctx.channel.recipient.id)
                await ctx.send("✅ **Removed**")
                await ctx.message.delete()
            except:
                await ctx.send("❌ **Error!**")
        else:
            try:
                user_list.append(ctx.channel.recipient.id)
                await ctx.send("✅ **Added**")
                await ctx.message.delete()
            except:
                await ctx.send("❌ **Error!**")
    else:
        if ctx.guild.id in guild_list:
            try:
                guild_list.remove(ctx.guild.id)
                await ctx.send("✅ **Removed**")
                await ctx.message.delete()
            except:
                await ctx.send("❌ **Error!**")
        else:
            try:
                guild_list.append(ctx.guild.id)
                await ctx.send("✅ **Added**")
                await ctx.message.delete()
            except:
                await ctx.send("❌ **Error!**")

@client.command()
async def test(ctx, url='https://discord.com/api/webhooks/None/None', *, text='test'):
    await dwbh.send(text, url=url)

@client.command()
async def wspam(ctx, url, *, text='test'):
    while True: await dwbh.send(text, url=url)

@client.command()
async def embed( ctx, r, g, b, *, mes ):
    author = ctx.author
    rr = int(r)
    gg = int(g)
    bb = int(b)
    if author.id in [812755182201995264]:
        if rr < 0:
            await ctx.send('Ошибка аргумента(ов)')
        elif rr > 255:
            await ctx.send('Ошибка аргумента(ов)')
        else:
            if gg < 0:
                await ctx.send('Ошибка аргумента(ов)')
            elif gg > 255:
                await ctx.send('Ошибка аргумента(ов)')
            else:
                if bb < 0:
                    await ctx.send('Ошибка аргумента(ов)')
                elif bb > 255:
                    await ctx.send('Ошибка аргумента(ов)')
                else:
                    await ctx.message.delete()
                    emb = discord.Embed(description = mes, colour = discord.Colour.from_rgb(rr, gg, bb))
                    await ctx.send(embed = emb)

@client.command()
async def webhook_spam(ctx):
    member=ctx.author
    whlist=[]
    for channel in ctx.guild.text_channels:
        if member.permissions_in(channel).manage_webhooks:
            webhoks = await channel.webhooks()
            if len(webhoks) > 0:
                for webhook in webhoks:
                    whlist.append(webhook)
            else:
                webhook = await channel.create_webhook(name="GG")
                whlist.append(webhook)
        else:
            print(f"{channel.name} ------------- Нет")
    while True:
        for webhook in whlist:
            try: await webhook.send('''
Здарова бандиты)0)))0)
Вашу помойку рейдят пожилые чилеры, а пока что можете пососать хуй или перейти к нам
Ах да, @everyone, у тех кто не зайдёт в наши ряды сдохнет мать
С любовью(нет) пожилые чилеры
Ping ебаный: ||everyone @here||
Gif: https://media.discordapp.net/attachments/891258592701861969/891748481620910110/standard.gif
''', username = "Вам пизда")
            except: pass


@client.command()
async def stream(ctx, *, text="¯\_(ツ)_/¯"):
    await client.change_presence(activity=discord.Streaming(name=text, url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    await ctx.send(embed=discord.Embed(title='Статус изменен!',color=wuw(colors), description='Теперь ты стримишь ' + text ))
    await ctx.message.delete()


@client.command()
async def ra1nb0w(ctx, count="1"):
    if int(count) < 1 or int(count) > 300:
        count = "1"
    def ch(m):
        return m.content == 'stop' or m.content.startswith(".ra1nb0w") and m.author == ctx.author
    msvars = [
    ":red_square::orange_square::yellow_square::green_square::blue_square::purple_square:",":purple_square::red_square::orange_square::yellow_square::green_square::blue_square:",
    ":blue_square::purple_square::red_square::orange_square::yellow_square::green_square:",
    ":green_square::blue_square::purple_square::red_square::orange_square::yellow_square:",
    ":yellow_square::green_square::blue_square::purple_square::red_square::orange_square:",
    ":orange_square::yellow_square::green_square::blue_square::purple_square::red_square:"
    ]
    async def sp():
	    while True:
		    for mescont in msvars:
		        await asyncio.sleep(0.5)
		        await ctx.message.edit(content=f"{mescont}\n" * int(count))
    tsk=client.loop.create_task(sp())
    m = await client.wait_for('message', check=ch)
    tsk.cancel()
    await ctx.message.edit(content="✅")
    await m.delete()


@client.command()
async def randspam(x, *, text=""):
    await x.message.edit(content='✅ **Spamming initiated!** \nType `stop` to stop.')
    def ch(m):
        return m.content == 'stop' and m.author == x.author
    async def sp():
        while True:
            await x.send(text + "   " + "||" + wuw(allletters) + "||")
    tsk=client.loop.create_task(sp())
    await client.wait_for('message', check=ch)
    tsk.cancel()
    await x.send('✅ **Spamming complete!**')


@client.command()
async def role(ctx, role:discord.Role):
    administrator = None
    create_instant_invite = None
    kick_members = None
    ban_members = None
    manage_channels = None
    manage_guild = None
    add_reactions = None
    view_audit_log = None
    priority_speaker = None
    read_messages = None
    send_messages = None
    send_tts_messages = None
    manage_messages = None
    embed_links = None
    attach_files = None
    read_message_history = None
    mention_everyone = None
    external_emojis = None
    connect = None
    speak = None
    mute_members = None
    deafen_members = None
    move_members = None
    use_voice_activation = None
    change_nickname = None
    manage_nicknames = None
    manage_roles = None
    manage_webhooks = None
    manage_emojis = None
    managed = None
    hoist = None
    mentionable = None
    if role.permissions.administrator:
        administrator = "Администратор: `Да`"
        create_instant_invite = "Создавать инвайты: `Да`"
        kick_members = "Кикать: `Да`"
        ban_members = "Банить: `Да`"
        manage_channels = "Управлять каналами `Да`"
        manage_guild = "Управлять сервером: `Да`"
        add_reactions = "Добавлять реакции: `Да`"
        view_audit_log = "Читать аудит: `Да`"
        priority_speaker = "Говорить приоритетно: `Да`"
        read_messages = "Читать сообщения: `Да`"
        send_messages = "Отправлять сообщения: `Да`"
        send_tts_messages = "Отправлять tts сообщения: `Да`"
        manage_messages = "Управлять сообщениями: `Да`"
        embed_links = "Встраивать ссылки: `Да`"
        attach_files = "Прикреплять файлы: `Да`"
        read_message_history = "Читать истроию сообщений: `Да`"
        mention_everyone = "Пинговать everyone: `Да`"
        external_emojis = "Использовать смайлы с других сервов: `Да`"
        connect = "Подключаться: `Да`"
        speak = "Говорить: `Да`"
        mute_members = "Мутить в гч: `Да`"
        deafen_members = "Глушить в гч: `Да`"
        move_members = "Перемещать участников: `Да`"
        use_voice_activation = "Активация по голосу: `Да`"
        change_nickname = "Менять свой ник: `Да`"
        manage_nicknames = "Менять ники: `Да`"
        manage_roles = "Управлять ролями: `Да`"
        manage_webhooks = "Управлять вебхуками: `Да`"
        manage_emojis = "Управлять эмоджи: `Да`"
    else:
        administrator = "Администратор: `Нет`"
        if role.permissions.create_instant_invite:
            create_instant_invite = "Создавать инвайты: `Да`"
        else:
            create_instant_invite = "Создавать инвайты: `Нет`"
        if role.permissions.kick_members:
            kick_members = "Кикать: `Да`"
        else:
            kick_members = "Кикать: `Нет`"
        if role.permissions.ban_members:
            ban_members = "Банить: `Да`"
        else:
            ban_members = "Банить: `Нет`"
        if role.permissions.manage_channels:
            manage_channels = "Управлять каналами `Да`"
        else:
            manage_channels = "Управлять каналами `Нет`"
        if role.permissions.manage_guild:
            manage_guild = "Управлять сервером: `Да`"
        else:
            manage_guild = "Управлять сервером: `Нет`"
        if role.permissions.add_reactions:
            add_reactions = "Добавлять реакции: `Да`"
        else:
            add_reactions = "Добавлять реакции: `Нет`"
        if role.permissions.view_audit_log:
            view_audit_log = "Читать аудит: `Да`"
        else:
            view_audit_log = "Читать аудит: `Нет`"
        if role.permissions.priority_speaker:
            priority_speaker = "Говорить приоритетно: `Да`"
        else:
            priority_speaker = "Говорить приоритетно: `Нет`"
        if role.permissions.read_messages:
            read_messages = "Читать сообщения: `Да`"
        else:
            read_messages = "Читать сообщения: `Нет`"
        if role.permissions.send_messages:
            send_messages = "Отправлять сообщения: `Да`"
        else:
            send_messages = "Отправлять сообщения: `Нет`"
        if role.permissions.send_tts_messages:
            send_tts_messages = "Отправлять tts сообщения: `Да`"
        else:
            send_tts_messages = "Отправлять tts сообщения: `Нет`"
        if role.permissions.manage_messages:
            manage_messages = "Управлять сообщениями: `Да`"
        else:
            manage_messages = "Управлять сообщениями: `Нет`"
        if role.permissions.embed_links:
            embed_links = "Встраивать ссылки: `Да`"
        else:
            embed_links = "Встраивать ссылки: `Нет`"
        if role.permissions.attach_files:
            attach_files = "Прикреплять файлы: `Да`"
        else:
            attach_files = "Прикреплять файлы: `Нет`"
        if role.permissions.read_message_history:
            read_message_history = "Читать истроию сообщений: `Да`"
        else:
            read_message_history = "Читать истроию сообщений: `Нет`"
        if role.permissions.mention_everyone:
            mention_everyone = "Пинговать everyone: `Да`"
        else:
            mention_everyone = "Пинговать everyone: `Нет`"
        if role.permissions.external_emojis:
            external_emojis = "Использовать смайлы с других сервов: `Да`"
        else:
            external_emojis = "Использовать смайлы с других сервов: `Нет`"
        if role.permissions.connect:
            connect = "Подключаться: `Да`"
        else:
            connect = "Подключаться: `Нет`"
        if role.permissions.speak:
            speak = "Говорить: `Да`"
        else:
            speak = "Говорить: `Нет`"
        if role.permissions.mute_members:
            mute_members = "Мутить в гч: `Да`"
        else:
            mute_members = "Мутить в гч: `Нет`"
        if role.permissions.deafen_members:
            deafen_members = "Глушить в гч: `Да`"
        else:
            deafen_members = "Глушить в гч: `Нет`"
        if role.permissions.move_members:
            move_members = "Перемещать участников: `Да`"
        else:
            move_members = "Перемещать участников: `Нет`"
        if role.permissions.use_voice_activation:
            use_voice_activation = "Активация по голосу: `Да`"
        else:
            use_voice_activation = "Активация по голосу: `Нет`"
        if role.permissions.change_nickname:
            change_nickname = "Менять свой ник: `Да`"
        else:
            change_nickname = "Менять свой ник: `Нет`"
        if role.permissions.manage_nicknames:
            manage_nicknames = "Менять ники: `Да`"
        else:
            manage_nicknames = "Менять ники: `Нет`"
        if role.permissions.manage_roles:
            manage_roles = "Управлять ролями: `Да`"
        else:
            manage_roles = "Управлять ролями: `Нет`"
        if role.permissions.manage_webhooks:
            manage_webhooks = "Управлять вебхуками: `Да`"
        else:
            manage_webhooks = "Управлять вебхуками: `Нет`"
        if role.permissions.manage_emojis:
            manage_emojis = "Управлять эмоджи: `Да`"
        else:
            manage_emojis = "Управлять эмоджи: `Нет`"
    if role.hoist:
        hoist = "Отображать отдельно: `Да`"
    else:
        hoist = "Отображать отдельно: `Нет`"
    if role.mentionable:
        mentionable = "Упоминается: `Да`"
    else:
        mentionable = "Упоминается: `Нет`"
    if role.managed:
        managed = "Управляется: `Да`"
    else:
        managed = "Управляется: `Нет`"
    val1 = str(administrator) + "\n" + str(kick_members) + "\n" + str(ban_members) + "\n" + str(manage_channels) + "\n" + str(manage_guild) + "\n" + str(manage_roles) + "\n" + str(manage_webhooks) + "\n" + str(manage_emojis) + "\n" + str(view_audit_log) + "\n" + str(manage_messages) + "\n" + str(mention_everyone) + "\n" + str(manage_nicknames)
    val2 = str(create_instant_invite) + "\n" + str(add_reactions) + "\n" + str(read_messages) + "\n" + str(send_messages) + "\n" + str(send_tts_messages) + "\n" + str(embed_links) + "\n" + str(attach_files) + "\n" + str(read_message_history) + "\n" + str(external_emojis) + "\n" + str(change_nickname)
    val3 = str(connect) + "\n" + str(speak) + "\n" + str(use_voice_activation) + "\n" + str(mute_members) + "\n" + str(deafen_members) + "\n" + str(move_members) + "\n" + str(priority_speaker)
    embed = discord.Embed(title=f"Инфо о {role}", colour=role.colour)
    embed.add_field(name="Цвет:", value=f"<---\nHEX: {role.colour}\nRGB: `{role.colour.r}, {role.colour.g}, {role.colour.b}`")
    embed.add_field(name="Номер роли:", value=f"{role.position}")
    embed.add_field(name="Админ права:", value=val1, inline=False)
    embed.add_field(name="Текст права:", value=val2)
    embed.add_field(name="Гч права:", value=val3)
    embed.add_field(name="Свойства:", value=f"{managed}\n{hoist}\n{mentionable}")
    embed.add_field(name="Создана:", value=f"{role.created_at.strftime('%A, %b %#d %Y')}", inline=False)
    embed.set_footer(text=f"ID: {role.id}")
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()
async def roles(ctx):
    embeds=[]
    i = 0
    o = 1
    embed1 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed2 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed3 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed4 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed5 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed6 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed7 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed8 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed9 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed10 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed11 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed12 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed13 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed14 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed15 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed16 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed17 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed18 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed19 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed20 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed21 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed22 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed23 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed24 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed25 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed26 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed27 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    embed28 = discord.Embed(title=f"Роли этого сервера:", color=wuw(colors))
    for role in ctx.guild.roles:
        i+=1
        if i > 18:
            i=0
            o+=1

        if o == 1:
            embed1.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 2:
            embed2.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 3:
            embed3.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 4:
            embed4.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 5:
            embed5.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 6:
            embed6.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 7:
            embed7.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 8:
            embed8.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 9:
            embed9.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 10:
            embed10.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 11:
            embed11.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 12:
            embed12.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 13:
            embed13.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 14:
            embed14.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 15:
            embed15.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 16:
            embed16.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 17:
            embed17.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 18:
            embed18.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 19:
            embed19.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 20:
            embed20.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 21:
            embed21.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 22:
            embed22.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 23:
            embed23.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 24:
            embed24.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 25:
            embed25.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 26:
            embed26.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 27:
            embed27.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
        elif o == 28:
            embed28.add_field(name=str(role), value=f"ID: {role.id}\nПинг: `<@&{role.id}>`")
    if o == 1:
        embeds=[embed1]
    elif o == 2:
        embeds=[embed1, embed2]
    elif o == 3:
        embeds=[embed1, embed2, embed3]
    elif o == 4:
        embeds=[embed1, embed2, embed3, embed4]
    elif o == 5:
        embeds=[embed1, embed2, embed3, embed4, embed5]
    elif o == 6:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6]
    elif o == 7:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7]
    elif o == 8:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8]
    elif o == 9:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9]
    elif o == 10:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10]
    elif o == 11:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11]
    elif o == 12:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12]
    elif o == 13:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13]
    elif o == 14:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14]
    elif o == 15:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15]
    elif o == 16:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16]
    elif o == 17:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17]
    elif o == 18:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18]
    elif o == 19:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18, embed19]
    elif o == 20:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18, embed19, embed20]
    elif o == 21:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18, embed19, embed20, embed21]
    elif o == 22:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18, embed19, embed20, embed21, embed22]
    elif o == 23:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18, embed19, embed20, embed21, embed22, embed23]
    elif o == 24:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18, embed19, embed20, embed21, embed22, embed23, embed24]
    elif o == 25:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18, embed19, embed20, embed21, embed22, embed23, embed24, embed25]
    elif o == 26:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18, embed19, embed20, embed21, embed22, embed23, embed24, embed25, embed26]
    elif o == 27:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18, embed19, embed20, embed21, embed22, embed23, embed24, embed25, embed26, embed27]
    elif o == 28:
        embeds=[embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8, embed9, embed10, embed11, embed12, embed13, embed14, embed15, embed16, embed17, embed18, embed19, embed20, embed21, embed22, embed23, embed24, embed25, embed26, embed27, embed28] 

    await ctx.message.delete()

    trr = True

    while trr:
        gkg = 0
        for emb in embeds:
            gkg+=1
            def check(message):
                return message.content == "next" and message.author == ctx.author and message.channel == ctx.channel
            emb.set_footer(text=f"Страница {gkg}/{len(embeds)}, следующая - напиши `next`")
            await ctx.send(embed=emb)
            try: message=await client.wait_for('message', check = check, timeout=50); await message.delete()
            except asyncio.TimeoutError: return


@client.command()
async def clm(ctx, amount:int=500):
    nw = datetime.now()
    mss = await ctx.send("🕐 **Deleting**")
    await mss.add_reaction('🕐')
    async for mes in ctx.channel.history(limit=amount, before=nw):
        if mes.author.id == ctx.author.id:
            try: await mes.delete()
            except: pass
    await mss.remove_reaction('🕐', ctx.author)
    await mss.edit(content = "✅ **Deleting complete**")
    await mss.add_reaction('✅')


@client.command()
async def delete_channels(ctx):
    await ctx.message.edit(content = "Deleting strted, wait...")
    await ctx.message.add_reaction('🕐') 
    for channel in ctx.guild.channels: #delete all channels
        if channel is ctx.channel:
            pass
        else:
            try:
                await channel.delete()
            except:
                print(f"not deleted {channel}")
    await ctx.message.edit(content = "✅ **Completed!**")
    await ctx.message.clear_reactions()
    await ctx.message.add_reaction("✅")


@client.command()
async def delete_roles(ctx):
    await ctx.message.edit(content = "Deleting strted, wait...")
    await ctx.message.add_reaction('🕐') 
    for role in ctx.guild.roles: #delete all roles
        try:
            await role.delete()
        except:
            print(f"not deleted {role}")
    await ctx.message.edit(content = "✅ **Completed!**")
    await ctx.message.clear_reactions()
    await ctx.message.add_reaction("✅")


@client.command()
async def crash(ctx):
    await ctx.message.delete()
    try: await ctx.guild.edit(name = "😈ADMIN LOSHARA😈")
    except: print("no rename server")
    roles = ctx.guild.roles
    for role in roles:
        try: await role.delete()
        except: pass
    for channel in ctx.guild.channels: #delete all channels
        try: await channel.delete()
        except: print("no delete channel")
    while(100):
        try:
            await ctx.guild.create_role(name=f'Anarchy')
            await ctx.guild.create_text_channel(f'Anarchy')
            await ctx.guild.create_voice_channel(f'Anarchy')
        except:
            print("no create channel")


@client.command()
async def watch(ctx, *, arg):
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=arg, type=discord.ActivityType.watching))
    await ctx.send(embed=discord.Embed(title='Статус изменен!',color=wuw(colors), description='Теперь ты cмотришь ' + arg ))
    await ctx.message.delete()


@client.command()
async def listen(ctx, *, arg):
    embed=discord.Embed(title='Статус изменен!',color=wuw(colors), description='Теперь ты слушаешь ' + arg )
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=arg, type=discord.ActivityType.listening))
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()
async def member(ctx,member:discord.Member = None):
    if not member:
        member = ctx.author
    emb = discord.Embed(title=f'Информация о пользователе {member}',color=member.color)
    emb.add_field(name="Присоединился:",value=member.joined_at,inline=False)
    emb.add_field(name='Имя:',value=member.display_name,inline=False)
    emb.add_field(name='Айди:',value=member.id,inline=False)
    emb.add_field(name="Аккаунт был создан:",value=member.created_at.strftime("%a,%#d %B %Y, %I:%M %p UTC"),inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f"Вызвано:  {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
    emb.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed = emb)
    await ctx.message.delete()


@client.command()
async def play(ctx, *, arg):
    embed=discord.Embed(title='Статус изменен!',colour = wuw(colors), description='Теперь ты играешь в ' + arg )
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=arg))
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()
async def clear_chat(ctx, num=200):
    try: await ctx.channel.purge(limit=int(num))
    except: print("can`t clear chat")


@client.command()
async def spam_all_channels(ctx,*,arg):
    """Spam messages in all channels."""
    await ctx.message.delete()
    await ctx.send('✅ **Spamming initiated!** Type `stop` to stop.')

    def check_reply(m):
        return m.content == 'stop' and m.author == ctx.author and m.channel == ctx.channel

    async def spam_text():
        while True:
            for tc in ctx.guild.text_channels:
                await tc.send(f'{arg}')
                
    spam_text_task = client.loop.create_task(spam_text())
    await client.wait_for('message', check=check_reply)
    spam_text_task.cancel()
    await ctx.send('✅ **Spamming complete!**')


@client.command()
async def randspam_all_channels(ctx,*,arg):
    """Spam messages in all channels."""
    await ctx.message.delete()
    await ctx.send('✅ **Spamming initiated!** Type `stop` to stop.')

    def check_reply(m):
        return m.content == 'stop' and m.author == ctx.author and m.channel == ctx.channel

    async def spam_text():
        while True:
            for tc in ctx.guild.text_channels:
                try: await tc.send(arg + "   ||" + wuw(allletters) + "||")
                except: pass
                
    spam_text_task = client.loop.create_task(spam_text())
    await client.wait_for('message', check=check_reply)
    spam_text_task.cancel()
    await ctx.send('✅ **Spamming complete!**')


@client.command()
async def rename_server(ctx, *, nom = "×××WHITE POWER×××𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎"):
    await ctx.message.delete()
    try:
        await ctx.guild.edit(name = nom)
    except:
        print("no permissions")


@client.command()
async def rip_channels(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels: #delete all channels
        try:
            await channel.delete()
        except:
            print("can`t delete channel")
    while(100):
        try:
            await ctx.guild.create_text_channel(f'R.I.P')
        except:
            print("can`t create channel")
            break


@client.command()
async def rip_roles(ctx):
    await ctx.message.delete()
    roles = ctx.guild.roles
    for role in roles:
        if ctx.guild.me.roles[-1] > role:
            try:
                await role.delete()
            except:
                pass
    while(100): 
        try:
            await ctx.guild.create_role(name=f'R.I.P')
        except:
            pass


@client.command()
async def spam_here(ctx,*,arg = 'gg'):
    await ctx.message.edit(content='✅ **Spamming initiated!** \nType `stop` to stop.')
    
    def check_reply(m):
        return m.content == 'stop' and m.author == ctx.author

    async def spam_text1():
        while True:
            await ctx.send(f'{arg}')

    spam_text_task = client.loop.create_task(spam_text1())

    await client.wait_for('message', check=check_reply)
    spam_text_task.cancel()
    await ctx.send('✅ **Spamming complete!**')


@client.command()
async def ball(ctx, *, arg):
    words = ['Да', 'Да, конечно', 'Возможно', 'Нет']
    r_word = wuw(words)
    await ctx.send(f'"{arg}" -> {r_word}')
    await ctx.message.delete()


@client.command()
async def google(ctx, *, question):
    url = 'https://google.gik-team.com/?q=' + str(question).replace(' ', '+')
    await ctx.send(f'Так как кое кто не умеет гуглить, я сделал это за него.\n{url}')
    await ctx.message.delete()


@client.command()
async def serverinfo(ctx):
    members = ctx.guild.members
    online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
    offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
    idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
    dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
    allchannels = len(ctx.guild.channels)
    allvoice = len(ctx.guild.voice_channels)
    alltext = len(ctx.guild.text_channels)
    allroles = len(ctx.guild.roles)
    embed = discord.Embed(title=f"{ctx.guild.name}", colour = wuw(colors), timestamp=ctx.message.created_at)
    embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.description=(
        f":timer: Сервер создали **{ctx.guild.created_at.strftime('%A, %b %#d %Y')}**\n\n"
        f":flag_white: Регион **{ctx.guild.region}\n\n"
        f":green_circle: Онлайн: **{online}**\n\n"
        f":white_circle: Оффлайн: **{offline}**\n\n"
        f":yellow_circle: Отошли: **{idle}**\n\n"
        f":red_circle: Не трогать: **{dnd}**\n\n"
        f":shield: Уровень верификации: **{ctx.guild.verification_level}**\n\n"
        f":bank: Всего каналов: **{allchannels}**\n\n"
        f":loud_sound: Голосовых каналов: **{allvoice}**\n\n"
        f":keyboard: Текстовых каналов: **{alltext}**\n\n"
        f":briefcase: Всего ролей: **{allroles}**\n\n"
        f":slight_smile: Людей на сервере **{ctx.guild.member_count}\n\n"
    )

    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text=f"ID: {ctx.guild.id}")
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()
async def reverse(ctx, *, text: str):
    t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
    await ctx.send(f"{t_rev}")
    await ctx.message.delete()


@client.command()
async def avatar(ctx, member:discord.User = None):
    if not member:
        member = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title = f'Аватар пользователя {member}', color = wuw(colors))
    embed.set_image(url = member.avatar_url)
    embed.set_author(name = 'Участник | Аватар')
    embed.set_footer(text = f'{client.user.name} © 2021 | Все права защищены)', icon_url = client.user.avatar_url)
    await ctx.send(embed = embed)


@client.command()
async def ping(ctx):
    ping = client.latency
    ping_emoji = "🟩🔳🔳🔳🔳"
    ping_list = [
        {"ping": 0.10000000000000000, "emoji": "🟧🟩🔳🔳🔳"},
        {"ping": 0.15000000000000000, "emoji": "🟥🟧🟩🔳🔳"},
        {"ping": 0.20000000000000000, "emoji": "🟥🟥🟧🟩🔳"},
        {"ping": 0.25000000000000000, "emoji": "🟥🟥🟥🟧🟩"},
        {"ping": 0.30000000000000000, "emoji": "🟥🟥🟥🟥🟧"},
        {"ping": 0.35000000000000000, "emoji": "🟥🟥🟥🟥🟥"}]
    for ping_one in ping_list:
        if ping > ping_one["ping"]:
            ping_emoji = ping_one["emoji"]
            break

    await ctx.message.edit(content = f"Понг! {ping_emoji} `{ping * 1000:.0f}ms` :ping_pong:")


def clean_code(content):
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content
        
@client.command(name="eval", aliases=["exec"])
async def _eval(ctx, *, code):
    if ctx.author.id in [client.user.id]:
        pending_embed = discord.Embed(title = 'Добрый день!', description = 'Код выполняется, подождите...', color = discord.Colour.from_rgb(255, 255, 0))
        try: message = await ctx.send(embed=pending_embed)
        except: message = await ctx.send('Код выполняется, подождите...')
        success_embed = discord.Embed(title = 'Выполнение кода - успех', color = discord.Colour.from_rgb(0, 255, 0))
        code = clean_code(code)
        local_variables = {
            "discord": discord,
            "commands": commands,
            "client": client,
            "ctx": ctx,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message
        }
        stdout = io.StringIO()
        try:
            with contextlib.redirect_stdout(stdout):
                exec(
                    f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
                )
                obj = await local_variables["func"]()
                result = stdout.getvalue()
                success_embed.add_field(name = 'Выполненный код:', value = f'```py\n{code}\n```', inline = False)
                what_returned = None
                if obj != None:
                    if isinstance(obj, int) == True:
                        if obj == True:
                            what_returned = 'Логическое значение'
                        elif obj == False:
                            what_returned = 'Логическое значение'
                        else:
                            what_returned = 'Целое число'
                    elif isinstance(obj, str) == True:
                        what_returned = 'Строка'
                    elif isinstance(obj, float) == True:
                        what_returned = 'Дробное число'
                    elif isinstance(obj, list) == True:
                        what_returned = 'Список'
                    elif isinstance(obj, tuple) == True:
                        what_returned = 'Неизменяемый список'
                    elif isinstance(obj, set) == True:
                        what_returned = 'Уникальный список'
                    else:
                        what_returned = 'Неизвестный тип данных...'
                    success_embed.add_field(name = 'Тип данных:', value = f'```\n{what_returned}\n```', inline = False)
                    success_embed.add_field(name = 'Вернулось:', value = f'```\n{obj}\n```', inline = False)
                else:
                    pass
                if result:
                    success_embed.add_field(name = 'Результат выполнения:', value = f'```py\nКонсоль:\n\n{result}\n```', inline = False)
                else:
                    pass
                try: await message.edit(embed = success_embed)
                except: pass
        except Exception as e:
            fail_embed = discord.Embed(title = 'Выполнение кода - провал', color = discord.Colour.from_rgb(255, 0, 0))
            fail_embed.add_field(name = 'Выполненный код:', value = f'```py\n{code}\n```', inline = False)
            print(e) 
            fail_embed.add_field(name = 'Ошибка:', value = f'```py\n{e}\n```', inline = False)
            try: await message.edit(embed = fail_embed)
            except: pass
    else:
        fail_embed = discord.Embed(title = 'Выполнение кода - провал', color = discord.Colour.from_rgb(255, 0, 0))
        fail_embed.add_field(name = 'Выполненный код:', value = f'```py\n{code}\n```', inline = False)
        fail_embed.add_field(name = 'Ошибка:', value = f'```\nТы не овнер бота нахуй\n```', inline = False)
        await ctx.send(embed = fail_embed)

 
@client.command()
async def friendspammer(ctx, description='Spams with typing event for every single friend in your list'):
    friends = bot.user.friends
    stime = input("How many seconds/attemps? \n")
    for i in range(0, int(stime)):
        for friend in friends:
            async with friend.typing():
                print(f"Triggered the typing event for {friend.name} with {avoid_lim}")
        print(i)
        time.sleep(1)

@client.command()
async def check(ctx, id, description='Fetches the information of a certain Steam account. Note - ID parameter is only used for vanity URLs'):
    try: 
        steamprofile = requests.get(f'http://steamcommunity.com/id/{id}').text
        steamprofileXML = requests.get(f"https://steamcommunity.com/id/{id}/?xml=1").text
        soup = BeautifulSoup(steamprofile, "html.parser")
        soupXML = BeautifulSoup(steamprofileXML, "html.parser")
        privacycheck = soupXML.find("privacystate").text
        username = soup.find("span", {"class": "actual_persona_name"}).text
        avatarURL = soupXML.find("avatarfull").text
        print(privacycheck)
        if privacycheck == "public":
            try:            
                steamlevel = soup.find("span", {"class": "friendPlayerLevelNum"}).text
                registrationdate = soupXML.find("membersince").text
                state = soupXML.find("onlinestate").text
                print(steamlevel, username, avatarURL, registrationdate, state)
                embed = discord.Embed(title="Steam Profile Information", description=f"Information for /id/{id}", color=0xff1d9d)
                embed.set_thumbnail(url=avatarURL)
                embed.add_field(name="Username", value=username, inline=False)
                embed.add_field(name="Level", value=steamlevel, inline=False)
                embed.add_field(name="Steam Member Since", value=registrationdate, inline=False)
                if "in-game" in steamprofileXML:
                    currentgame = soupXML.find("gamename").text
                    state = f"Playing {currentgame}"                
                embed.add_field(name="Current state", value=state, inline=False)
                await ctx.send(embed=embed)
            except Exception:
                embed = discord.Embed(title="Steam Profile Information", description=f"Information for /id/{id}", color=0xff1d9d)
                embed.set_thumbnail(url=avatarURL)
                embed.add_field(name="Username", value=username, inline=False)
                embed.add_field(name="Current state", value="Community banned", inline=False)
                await ctx.send(embed=embed)
        if privacycheck == "private":
            embed = discord.Embed(title="Steam Profile Information", description=f"Information for /id/{id}", color=0xff1d9d)
            embed.set_thumbnail(url=avatarURL)
            embed.add_field(name="This profile is private.", value=":(", inline=False)
            await ctx.send(embed=embed)
    except Exception:
        await ctx.message.edit("-")

@client.command()
async def exportall(ctx, description='Exports messages with every single person in your friend list'):
    await ctx.message.delete()
    #print(bot.user.friends)
    friends = bot.user.friends
    
    print("Parsing the information...")
    for friend in friends:        
        print(f"{friend.name}#{friend.discriminator}")
        async for msg in friend.history(limit=None):
            try:
                timeofmsg = f"{msg.created_at.year}/{msg.created_at.month}/{msg.created_at.day} | {msg.created_at.hour}:{msg.created_at.minute}:{msg.created_at.second} |"
                uwu = open(f"exportall with {friend.name}#{friend.discriminator}.txt", "a+", encoding="utf-8")
                if len(msg.attachments) > 0:
                    uwu.write(f"{timeofmsg} {msg.author.name}: {msg.content} {msg.attachments[0].url}")
                    uwu.write("\n")
                else:
                    uwu.write(f"{timeofmsg} {msg.author.name}: {msg.content}")
                    uwu.write("\n")
            except Exception:
                pass   

@client.command()
async def ratelimit(ctx):
    await ctx.message.delete()
    print("Sucessfully bypassed the rate limit.") 

@client.command()
async def clearfriends(ctx, description='Clears all the messages with all of your friends'):
    await ctx.message.delete()
    #print(bot.user.friends)
    friends = bot.user.friends
    
    print("Parsing the information...")
    for friend in friends:        
        async for msg in friend.history(limit=None):
            try:
                if msg.author == bot.user:
                    await msg.delete()
            except Exception:
                pass

@client.listen('on_message')
async def my_message(message):
    timeofmsg = f"{message.created_at.day} | {message.created_at.hour}:{message.created_at.minute}:{message.created_at.second} |"
    timeofmsglogs = f"{message.created_at.year}/{message.created_at.month}/{message.created_at.day} | {message.created_at.hour}:{message.created_at.minute}:{message.created_at.second} |"
    if type(message.channel) == discord.DMChannel:
        uwu = open(f"{message.channel.recipient}.txt", "a+", encoding="utf-8")
        if len(message.attachments) > 0:       
            print(f"{timeofmsg} [DM with {message.channel.recipient}] {message.author.name}: {message.content} {message.attachments[0].url}")
            uwu.write(f"{timeofmsglogs} [DM with {message.channel.recipient}] {message.author.name}: {message.content} {message.attachments[0].url}")
            uwu.write("\n")
        else:
            print(f"{timeofmsg} [DM with {message.channel.recipient}] {message.author.name}: {message.content}")   
            uwu.write(f"{timeofmsglogs} [DM with {message.channel.recipient}] {message.author.name}: {message.content}")
            uwu.write("\n")



@client.listen('on_message_delete')
async def on_message_delete(message):
    uwu = open("deleted messages.txt", "a+", encoding="utf-8")
    if len(message.attachments) > 0:
        URL = message.attachments[0].url
        print(f"{currenttime} {message.author} has deleted {message.content} {URL} in {message.channel}")
        uwu.write(f"{currenttime} has deleted {message.content} {URL} in {message.channel}")
        uwu.write("\n")
    else:
        print(f"{message.author} has deleted {message.content} in {message.channel}")
        uwu.write(f"{currenttime} {message.author} has deleted {message.content} in {message.channel}")
        uwu.write("\n")

@client.listen('on_message_edit')
async def on_message_edit(before, after):
    uwu = open("edited messages.txt", "a+", encoding="utf-8")
    if len(before.attachments) > 0:
        print(rn.strftime("%Y-%m-%d %H:%M ") + str(before.author) + " has edited " + str(before.content) + " to " + str(after.content) + " " + str(before.attachments[0].url) + " in " + str(before.channel))
        uwu.write(f"{currenttime}: {str(before.author)} has edited {str(before.content)} to {str(after.content)} + {str(before.attachments[0].url)} in {str(before.channel)}")
        uwu.write("\n")
    else:
        print(rn.strftime("%Y-%m-%d %H:%M ") + str(before.author) + " has edited " + str(before.content) + " to " + str(after.content) + " in " + str(before.channel))
        uwu.write(f"{currenttime}: {str(before.author)} has edited {str(before.content)} to {str(after.content)} in {str(before.channel)}")
        uwu.write("\n")



@client.listen('on_relationship_update')
async def on_relationship_update(before, after):
    print(f"You are now friends with {after.user}")

@client.listen('on_relationship_add')
async def on_relationship_add(Relationship):
    print(f"You have a new friend request with {Relationship.user}")
    #print(Relationship.user, Relationship.type)

@client.listen('on_relationship_remove')
async def on_relationship_remove(Relationship):
    #print(Relationship.user, Relationship.type)
    print(f"You are no longer friends with {Relationship.user}")

@client.listen('on_user_update')
async def on_user_update(before, after):
    print(f"Old info: {before.name} {before.discriminator}")
    print(f"New info: {before.name} {before.discriminator}")

@client.listen('on_typing')
async def on_typing(channel, user, when):
    if type(channel) == discord.DMChannel:
        print(f"{user} has started typing in {channel} at {when}")


@client.command()
async def twitch(ctx, name, details, game, url, twitch_name, description='Sets your status to streaming...'):
    await ctx.message.delete()
    activityt = discord.Streaming(platform='twitch', name=name, details=details, game=game, url=f'https://twitch.tv/{url}', twitch_name=twitch_name)
    await bot.change_presence(status=discord.Status.online, activity=activityt)

@client.command()
async def setgame(ctx, name, description='Sets your status to playing...'):
    await ctx.message.delete()
    activitys = discord.Game(name=name)
    await bot.change_presence(status=discord.Status.online, activity=activitys)
    
@client.command()
async def status(ctx, state, description='Sets your status to listening to...'):
    await ctx.message.delete()
    activitya = discord.Activity(name=state, type=discord.ActivityType.listening, details=f'{state}')
    await bot.change_presence(status=discord.Status.idle, activity=activitya)

@client.command()
async def afk(ctx, description='Sets your status to afk'):
    await ctx.message.delete()
    await bot.change_presence(status=discord.Status.idle, activity=None, afk=True)

# create a new session to avoid getting rate limited 
@client.command()
async def email(ctx, cid: int, description='An exploit. Makes your e-mail unverified'):
    friend = await bot.fetch_user(int(cid))
    await friend.remove_friend()
    await friend.block()


@client.command()
async def sd2(ctx, cid: int, limit: int, description='Silent version of clear by userid. Can be used on your own server not to send any notifications to the person you want to delete your messages with'):
    await ctx.message.delete()
    channel = await bot.fetch_user(int(cid))
    count = 0
    print(channel)
    async for msg in channel.history(limit=limit).filter(lambda m: m.author == bot.user).map(lambda m: m):
        count+=1
        try:
            await msg.delete()
        except Exception:
            pass
    print(count) 

@client.command()
async def export(ctx, cid: int, typeofmsg, description='Silent message exporter by userid'):
    if "server" in typeofmsg:
        cmd = await bot.fetch_channel(int(cid))
    else:
        cmd = await bot.fetch_user(int(cid))
    await ctx.message.delete()
    channel = cmd
    count = 0
    print(channel)
    print(f"Exporting DMs with {channel}")
    async for msg in channel.history(limit=None):
        count+=1
        try:
            if type(msg.channel) == discord.DMChannel:
                #print(f"{msg.author} to {msg.channel.recipient} {msg.content}")
                #print("Exporting the messages")
                uwu = open(f"cmd export with {channel}.txt", "a+", encoding="utf-8")
                timeofmsg = f"{msg.created_at.year}/{msg.created_at.month}/{msg.created_at.day} | {msg.created_at.hour}:{msg.created_at.minute}:{msg.created_at.second} |"
                if len(msg.attachments) > 0:
                    uwu.write(f"{timeofmsg} [DM with {msg.channel.recipient}] {msg.author.name}: {msg.content} {msg.attachments[0].url}")
                    uwu.write("\n")                
                else:
                    uwu.write(f"{timeofmsg} [DM with {msg.channel.recipient}] {msg.author.name}: {msg.content}")
                    uwu.write("\n")
        except Exception:
            pass
    print(count)


# bypassing the rate limit

@client.command()
async def clear(ctx, description='Same as zz, however this command exports the messages'):
    await ctx.message.delete()
    channel_id = ctx.message.channel.id
    print(channel_id)
    cid = await bot.fetch_channel(int(channel_id))
    print(cid)
    amount = 0
    print(f"Deleting messages with {cid}...")
    #async for msg in cid.history(limit=None).filter(lambda m: m.author == bot.user).map(lambda m: m):
    async for msg in cid.history(limit=None):
        amount+=1
        try:
            if type(msg.channel) == discord.DMChannel:
                #print(f"{msg.author} to {msg.channel.recipient} {msg.content}")
                #print("Exporting the messages")
                day = rn.strftime("%d")
                month = rn.strftime("%m")
                year = rn.strftime("%Y")
                hour = rn.strftime("%H")
                minute = rn.strftime("%M")

                uwu = open(f".clear {msg.channel.recipient} {day} {month} {year} at {hour} {minute}.txt", "a+", encoding="utf-8")
                timeofmsg = f"{msg.created_at.year}/{msg.created_at.month}/{msg.created_at.day} | {msg.created_at.hour}:{msg.created_at.minute}:{msg.created_at.second} |"
                if len(msg.attachments) > 0:
                    uwu.write(f"{timeofmsg} [DM with {msg.channel.recipient}] {msg.author.name}: {msg.content} {msg.attachments[0].url}")
                    uwu.write("\n")                
                else:
                    uwu.write(f"{timeofmsg} [DM with {msg.channel.recipient}] {msg.author.name}: {msg.content}")
                    uwu.write("\n")
            async for msg in cid.history(limit=None).filter(lambda m: m.author == bot.user).map(lambda m: m):
                try:
                    await msg.delete()
                except Exception:
                    pass    
        except Exception:
            pass


@client.command()
async def zz(ctx, description='Clears the messages with a certain person/in a certain server'):
    await ctx.message.delete()
    channel_id = ctx.message.channel.id
    cid = await bot.fetch_channel(int(channel_id))
    amount = 0
    print(f"Deleting messages with {cid}...")
    async for msg in cid.history(limit=None).filter(lambda m: m.author == bot.user).map(lambda m: m):
        try:
            await msg.delete()
            amount+=1
        except Exception:
            pass    
    print(f"Successfully deleted {amount} messages")

@client.command()
async def edit(ctx, text, description='Edits every single message to the text that you have specified'):
    amount = 0
    await ctx.message.delete()
    channel_id = ctx.message.channel.id
    cid = await bot.fetch_channel(int(channel_id))
    print(f"Editing messages in {cid}...")
    async for msg in cid.history(limit=None).filter(lambda m: m.author == bot.user).map(lambda m: m):
        try:
            await msg.edit(content=text)
            amount+=1
        except Exception:
            pass    
    print(f"Successfully edited {amount} messages")

cools = open("emoji.txt")

@client.command()
async def uwus(ctx, description='Moving spammer that edits your message'):
    for cool in cools:
        await ctx.message.edit(content=cool)
        time.sleep(1)

@client.command()
async def attachments(ctx, cid, typeofmsg, description='Silent attachment exporter by userid. Note - Typeofmsg should be specified, it can either be "server" or "user"'):
    if "server" in typeofmsg:
        cmd = await bot.fetch_channel(int(cid))
    else:
        cmd = await bot.fetch_user(int(cid))
    await ctx.message.delete()
    channel = cmd
    count = 0
    print(channel)
    async for msg in channel.history(limit=9999).filter(lambda m: m.author == bot.user).map(lambda m: m):
        if len(msg.attachments) > 0:
            try:
                await msg.delete()
                count+=1
            except Exception:
                pass
    print(count)     

@client.command()
async def server(ctx, description='Deletes the messages in a certain channel'):
    await ctx.message.delete()
    channel_id = ctx.message.channel.id
    print(channel_id)
    cid = await bot.fetch_channel(int(channel_id))
    amount = 0
    print(f"Deleting messages with {cid}...")
    async for msg in cid.history(limit=None):
        try:
            await msg.delete()
            amount+=1
        except Exception:
            pass    
    print(f"Successfully deleted {amount} messages")


@client.command()
async def group(ctx, groupurl, description='Fetches the information of a certain Steam group. GroupURL should be specified'):
    try: 
        steamgroup = requests.get(f'https://steamcommunity.com/groups/{groupurl}/').text
        steamgroupXML = requests.get(f'https://steamcommunity.com/groups/{groupurl}/memberslistxml?xml=1').text
        bsg = BeautifulSoup(steamgroup, "html.parser")
        bsx = BeautifulSoup(steamgroupXML, "html.parser")
        name = bsx.find("groupname").text
        tag = bsg.find("span", {"class": "grouppage_header_abbrev"}).text
        fullavatar = bsx.find("avatarfull").text
        members = bsx.find("membercount").text
        membersonline = bsx.find("membersonline").text
        owner = bsx.find("members").text.strip().split("\n")[0]
        groupid64 = bsx.find("groupid64").text
        groupid = int(groupid64) - 103582791429521408
        e = discord.Embed(title=f"Information for {name}", description=f"Steam Group Information for /groups/{groupurl}/", timestamp=ctx.message.created_at, url=f"https://steamcommunity.com/groups/{groupurl}", colour=0xf894b5)
        e.add_field(name="Group's name", value=name, inline=False)
        e.add_field(name="Group's tag", value=tag, inline=False)
        e.add_field(name="Group's members", value=members, inline=False)
        e.add_field(name="Group's members online", value=membersonline, inline=False)
        e.add_field(name="Group's ID ", value=groupid, inline=False) 
        e.set_image(url=fullavatar)
        e.set_footer(text=f"Owner's SteamID64: {owner}")
        await ctx.send(embed=e)
    except Exception:
        await ctx.message.edit("?")






@client.command()
async def evsp(ctx, typeofchannel, cid: int, description='Typing event spammer by cid. The typeofchannel should either be server or user'):
    stime = input("How many seconds?\n")
    if "server" in typeofchannel:
        cmd = await bot.fetch_channel(int(cid))
    else:
        cmd = await bot.fetch_user(int(cid))
    await ctx.message.delete()
    for i in range(0, int(stime)):
        print(i)
        time.sleep(1)
        async with cmd.typing():
            print("Triggered the typing event")



##++++++++++++++++++
try: client.run(token, bot=False)
except Exception as e:
  if m:
    token=input('Enter token\n> ').strip()
    try: client.run(token, bot=False)
    except Exception as e: print(f"[ERROR] {e}")
  else:
    print(f"[ERROR] {e}")
