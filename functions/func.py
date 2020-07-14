from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,InlineQueryHandler,BaseFilter
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


def unknown(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I dont understand FTW you said buddy!")


def abused(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="You retard your mom retard")