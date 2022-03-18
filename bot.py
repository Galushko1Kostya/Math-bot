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

def calc(a, b, s):
    global c
    if s == "+":
        c = a + b
    elif s == "-":
        c = a - b
    elif s == "/":
        if b!= 0:
            c = a / b
        else:
            c = 'Error'
    elif s == "*":
        c = a * b
    elif s == "**":
        c = a ** b    
    return c
         
def check_func(update, context):
    chat = update.effective_chat
    list = update.message.text
    try:
        y, d, x = list.split()
    except ValueError:
        context.bot.send_message(chat_id=chat.id, text="invalid value")
        return
    if not y.isdigit():
        y_int = int(y)
    else:
        context.bot.send_message(chat_id=chat.id, text="invalid value")
    if not d.isdigit():
        x_int = int(x)
    else:
        context.bot.send_message(chat_id=chat.id, text="invalid value")
        f = calc(y_int, x_int, d)
        context.bot.send_message(chat_id=chat.id, text=f)
        context.bot.send_message(chat_id=chat.id, text=c)
      
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler(Filters.all, calc))
updater.start_polling()
updater.idle()