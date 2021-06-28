import discord

client = discord.Client()

def extract_token():
    f = open("token.txt", "r")
    return str(f.read())

###IGNORE###
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('8=D')
###IGNORE###

client.run(extract_token()) #Token needs to be changed on token.txt
