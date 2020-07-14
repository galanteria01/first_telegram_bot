from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,InlineQueryHandler
from telegram import InlineQueryResultArticle ,InputTextMessageContent
import logging


def inline_caps(update,context):
    query= update.inline_query.query
    if not query:
        return
    results = list()
    results.append(InlineQueryResultArticle(id=query.upper(),title='Caps',
                                            input_message_content=InputTextMessageContent(query.upper())))

def sticker(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Thats really stupid sticker.U suck 24/7")


def echo(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text=update.message.text)


def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="I am a bot.How are you?")


def caps(update,context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id,text=text_caps)


def picvid(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="This is a picvid bruh")


def owner(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Shoury Sharma")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Github: galanteria01")
    context.bot.send_message(chat_id=update.effective_chat.id, text="telegram: shanuu12e")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Fuck off dude")
# Initialised token from botfather
updater = Updater('1033297905:AAF4KZfofsQNsdkDrHxoP15jgU5VSWAD4Tw',use_context=True)
dispatcher=updater.dispatcher

# Set up logging to report errors
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',level=logging.INFO)

# Added /start to work on demand
start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

# Added the bot to repeat the non command words
echo_handler = MessageHandler(Filters.text & (~Filters.command),echo)
dispatcher.add_handler(echo_handler)

# Added the /caps functionalities to the caps
caps_handler = CommandHandler('caps',caps)
dispatcher.add_handler(caps_handler)

# Added inline caps funcionalities
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

# Added picture and video handler
picvid_handler = MessageHandler(Filters.photo | Filters.video,picvid)
dispatcher.add_handler(picvid_handler)

#Added some random
owner_handler = CommandHandler('owner',owner)
dispatcher.add_handler(owner_handler)

#Added filter to sticker
sticker_handler = MessageHandler(Filters.sticker,sticker)
dispatcher.add_handler(sticker_handler)
# Started the bot
updater.start_polling()
