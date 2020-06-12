from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,InlineQueryHandler
from telegram import InlineQueryResultArticle ,InputTextMessageContent
import logging

def inline_caps(update,context):
    query= update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(id=query.upper(),
                                 title='Caps',
                                 input_message_content=InputTextMessageContent(query.upper()))
    )
def echo(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text=update.message.text)

def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="I am a bot.How are you?")

def caps(update,context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id,text=text_caps)


updater = Updater('1033297905:AAF4KZfofsQNsdkDrHxoP15jgU5VSWAD4Tw',use_context=True)
dispatcher=updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',level=logging.INFO)
start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)
echo_handler = MessageHandler(Filters.text & (~Filters.command),echo)
dispatcher.add_handler(echo_handler)
caps_handler = CommandHandler('caps',caps)
dispatcher.add_handler(caps_handler)
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

updater.start_polling()
