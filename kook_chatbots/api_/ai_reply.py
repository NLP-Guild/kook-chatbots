from chatbots import Blenderbot
bot = Blenderbot()

def reply(msg):
    return bot.reply(msg)

def clear_history():
    bot.conv.clear_dialog_history()