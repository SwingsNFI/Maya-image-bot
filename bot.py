from random import Random, random, sample
from multiprocessing import context
from email.policy import default
from dotenv import load_dotenv
from telnetlib import SEND_URL
from unittest import result
from math import perm
import lightbulb
import listodata
import hikari
import random
import os

load_dotenv()

bot = lightbulb.BotApp(
    token = os.getenv("DISCORD_TOKEN"),
    default_enabled_guilds=
    (
    707938586988642376, 
    965307477698707506, 
    767743597809500160, 
    134028939764039681,
    )
)


@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent):
    if isinstance(event.exception, lightbulb.CommandIsOnCooldown): 
        await event.context.respond(f"Hey, dont spam! <:mayagun:978841590644752464>", flags=hikari.MessageFlag.EPHEMERAL)
    if isinstance(event.exception, lightbulb.MaxConcurrencyLimitReached):
        await event.context.respond(f"You're trying to run too many commands at the same time! <:mayagun:978841590644752464>", flags=hikari.MessageFlag.EPHEMERAL)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('bot has started!')

# Greetings
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('ping', 'check if maya is awake!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond(random.choice(listodata.Greeting_list))

# Maya
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('maya', 'provides an adorable maya image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def maya(ctx):
    await ctx.respond(random.choice(listodata.Maya_list))

# Megu
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('megu', 'provides an adorable megu image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def megu(ctx):
    await ctx.respond(random.choice(listodata.Megu_list))

# Chino
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('chino', 'provides an adorable chino image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def chino(ctx):
    await ctx.respond(random.choice(listodata.Chino_list))

# Chimame
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('chimame', 'provides an adorable chimame image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def chimame(ctx):
    await ctx.respond(random.choice(listodata.Chimame_list))

# Cocoa
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('cocoa', 'provides an adorable cocoa image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def cocoa(ctx):
    await ctx.respond(random.choice(listodata.Cocoa_list))

# Rize
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('rize', 'provides an adorable rize image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def rize(ctx):
    await ctx.respond(random.choice(listodata.Rize_list))

# Syaro
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('syaro', 'provides an adorable syaro image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def syaro(ctx):
    await ctx.respond(random.choice(listodata.Syaro_list))

# Chiya
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('chiya', 'provides an adorable chiya image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def chiya(ctx):
    await ctx.respond(random.choice(listodata.Chiya_list))

# Pat Maya
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('patmaya', 'pats maya!')
@lightbulb.implements(lightbulb.SlashCommand)
async def patmaya(ctx):
    await ctx.respond('<a:mayapat1:855215364370595840>')

# Pat Megu
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('patmegu', 'pats megu!')
@lightbulb.implements(lightbulb.SlashCommand)
async def patmegu(ctx):
    await ctx.respond('<a:MeguPat:904726832027422720>')

# Pat Chino
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('patchino', 'pats chino!')
@lightbulb.implements(lightbulb.SlashCommand)
async def patchino(ctx):
    await ctx.respond('<a:patchino:997143091175751791>')

# CQC
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('cqc', 'Use CQC!')
@lightbulb.implements(lightbulb.SlashCommand)
async def cqc(ctx):
    await ctx.respond(random.choice(listodata.cqc_list))

bot.run()
