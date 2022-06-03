# Modifier les occurences : test_bot(id de votre channel) / bot.run(id de votre token)

import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="!")




@bot.event
async def on_ready():
    print("Bot is ready")
    test_bot = bot.get_channel()
    bot.load_extension("music")
    await test_bot.send("Bonjour ! tapez /help pour avoir de l'aide :)")



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    test_bot = bot.get_channel()
    await bot.process_commands(message)
    message.content = message.content.lower()

    if  message.content.startswith('/help') :
        await message.reply('Bonjour, pour les sondages, utilisez: \n ▶️ /yn pour les questions fermées \n ▶️ /poll pour les questions ouvertes \n ▶️ Ne pas oublier de rajouter le nombre de choix (ex : poll2)')

    if  message.content.startswith('/yn'):
        await test_bot.send('@everyone Votez ici ⬆️')
        await message.add_reaction('👍')
        await message.add_reaction('👎')

    if  message.content.startswith('/poll2'):
        await test_bot.send('@everyone Votez ici ⬆️')
        await message.add_reaction('1️⃣')
        await message.add_reaction('2️⃣')

    if  message.content.startswith('/poll3'):
        await test_bot.send('@everyone Votez ici ⬆️')
        await message.add_reaction('1️⃣')
        await message.add_reaction('2️⃣')
        await message.add_reaction('3️⃣')

    if  message.content.startswith('/poll4'):
        await test_bot.send('@everyone Votez ici ⬆️')
        await message.add_reaction('1️⃣')
        await message.add_reaction('2️⃣')
        await message.add_reaction('3️⃣')
        await message.add_reaction('4️⃣')

    if  message.content.startswith('/poll5'):
        await test_bot.send('@everyone Votez ici ⬆️')
        await message.add_reaction('1️⃣')
        await message.add_reaction('2️⃣')
        await message.add_reaction('3️⃣')
        await message.add_reaction('4️⃣')
        await message.add_reaction('5️⃣')

    if message.content == 'quoi':
        await message.reply('feur')
    
    if message.content == 'hein':
        await message.reply('deux')

    if message.content == 'ouais':
        await message.reply('stern')

    if message.content == 'qui':
        await message.reply('rikou')

    if message.content == "del":
        await message.channel.purge(limit=10)


bot.run("")