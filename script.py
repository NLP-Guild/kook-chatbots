from khl import Bot, Message
from kook_chatbots.utils import read_config
from kook_chatbots.api_ import ai_reply,CommandManager,print_msg_info,clear_chat_history
import asyncio

# init Bot
testBot_token = read_config()['testBot']
bot = Bot(token=testBot_token)

# command magager
command_manager = CommandManager()
command_manager.register_command('hello',lambda :'world','send a hello world sentence')
command_manager.register_command('clearhistory',clear_chat_history,'清楚聊天机器人对话历史')

# register command, send `/hello` in channel to invoke
# @bot.command(name='hello')
# async def world(msg: Message):
#     task1 = asyncio.create_task(print_msg_info(msg))
#     # await print_msg_info(msg)
#     await msg.reply('world!')
#     await task1


@bot.on_message()
async def auto_reply(msg: Message):
    print_msg_info(msg)

    msg_content = msg.content
    # command
    if msg_content.startswith('/'):
        response = command_manager.parse_command_and_exec(msg_content)
        if response is not None:
            await msg.reply(response)

    # normal text
    else:
        if msg.ctx.channel.id == '5025001924381672': #机器人聊天频道
            response = ai_reply(msg_content)
            await msg.reply(response)



# everything done, go ahead now!
bot.run()
# now invite the bot to a server, and send '/hello' in any channel
# (remember to grant the bot with read & send permissions)