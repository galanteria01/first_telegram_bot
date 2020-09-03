from telegram.ext import Updater,CommandHandler, MessageHandler, Filters
from telegram.ext import InlineQueryHandler, BaseFilter, ConversationHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
import logging
from functions.func import *
from functions.classes import *


# Initialised token from botfather
updater = Updater('1033297905:AAF4KZfofsQNsdkDrHxoP15jgU5VSWAD4Tw', use_context=True)
dispatcher=updater.dispatcher

# Set up logging to report errors
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(message)s', level=logging.INFO)

# Added /start to work on demand
dispatcher.add_handler(CommandHandler('start',start))

dispatcher.add_handler(MessageHandler(Filters.caption_entity("hashtag")))


# Added the /caps functionalities to the caps
dispatcher.add_handler(CommandHandler('caps', caps))

# Added inline caps funcionalities
dispatcher.add_handler(InlineQueryHandler(inline_caps))

# Added picture and video handler
dispatcher.add_handler(MessageHandler(Filters.photo | Filters.video,picvid))

# Added some random
dispatcher.add_handler(CommandHandler('owner', owner))

# Added filter to sticker
dispatcher.add_handler(MessageHandler(Filters.sticker, sticker))

# Added help handler
dispatcher.add_handler(CommandHandler('help',helpComplaints))

# Add unknown to program
dispatcher.add_handler(MessageHandler(Filters.command, unknown))

# Added the bot to repeat the non command words
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command),echo))



# Started the bot
updater.start_polling()
