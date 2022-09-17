from khl import Bot, Message
from utils import read_config



# init Bot
testBot_token = read_config()['testBot']
bot = Bot(token=testBot_token)


# register command, send `/hello` in channel to invoke
@bot.command(name='hello')
async def world(msg: Message):
    await msg.reply('world!')


# everything done, go ahead now!
bot.run()
# now invite the bot to a server, and send '/hello' in any channel
# (remember to grant the bot with read & send permissions)