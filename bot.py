from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pprint import pprint

TOKEN = '5245584590:AAGv6oc2i2A7yu7Kmmj-JBlM0DMGn_5Hwx0'
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
print('Bot started. Press Ctrl+Z to exit')

def start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! Welcome to currency Bot!")

def help(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Hello! List of commands: start, help, calc")

def math(a, b, sing):
    if sing == "+":
        print(a + b)
        result = a + b
    elif sing == "-":
        print(a - b)
        result = a - b
    elif sing == "*":
        print(a * b)
        result = a * b
    elif sing == "/":
        print(a / b)
        result = a / b
    elif sing == "**":
        print(a ** b)
        result = a ** b
    else:
        return "error"
    return result
         
def float(update, context):
    chat = update.effective_chat
    list = update.message.text
    try:
        b, c, d = list.split()
    except ValueError:
        context.bot.send_message(chat_id=chat.id, text="invalid value")
        return
    if b.isdigit():
        b_float = float(b)
    else:
        context.bot.send_message(chat_id=chat.id, text="invalid value")
    if d.isdigit():
        d_float = float(d)
    else:
        context.bot.send_message(chat_id=chat.id, text="invalid value")
        g = math(b_float, d_float, c)
        context.bot.send_message(chat_id=chat.id, text=g)
      
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('calc', math))
updater.start_polling()
updater.idle()