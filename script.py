from khl import Bot, Message
from kook_chatbots.utils import read_config
from kook_chatbots.api_ import print_msg_info
from kook_chatbots.api_ import ai_reply
import asyncio

# init Bot
testBot_token = read_config()['testBot']
bot = Bot(token=testBot_token)


# register command, send `/hello` in channel to invoke
@bot.command(name='hello')
async def world(msg: Message):
    task1 = asyncio.create_task(print_msg_info(msg))
    # await print_msg_info(msg)
    await msg.reply('world!')
    await task1

@bot.on_message()
async def auto_reply(msg: Message):
    msg_content = msg.content
    print(msg_content)
    response = ai_reply(msg_content)
    await msg.reply(response)



# everything done, go ahead now!
bot.run()
# now invite the bot to a server, and send '/hello' in any channel
# (remember to grant the bot with read & send permissions)