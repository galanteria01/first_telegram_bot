from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,InlineQueryHandler,BaseFilter
from telegram import InlineQueryResultArticle ,InputTextMessageContent
import logging
from functions.func import *
from functions.classes import *



abuse_man = Abuse()

# Initialised token from botfather
updater = Updater('1033297905:AAF4KZfofsQNsdkDrHxoP15jgU5VSWAD4Tw',use_context=True)
dispatcher=updater.dispatcher

# Set up logging to report errors
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',level=logging.INFO)

# Added /start to work on demand
start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

#Added retarded friendly
retard_handler = MessageHandler(abuse_man,abused)

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

# Added some random
owner_handler = CommandHandler('owner',owner)
dispatcher.add_handler(owner_handler)

# Added filter to sticker
sticker_handler = MessageHandler(Filters.sticker,sticker)
dispatcher.add_handler(sticker_handler)

# Add unknown to program
unknown_handler = MessageHandler(Filters.command,unknown)
dispatcher.add_handler(unknown_handler)


# Started the bot
updater.start_polling()
