from telegram.ext import Updater,CommandHandler
import logging
def start(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="I am a bot.How are you?")

updater= Updater('1033297905:AAF4KZfofsQNsdkDrHxoP15jgU5VSWAD4Tw',use_context=True)
dispatcher=updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',level=logging.INFO)
start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)
updater.start_polling()
