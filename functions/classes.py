from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,InlineQueryHandler,BaseFilter
from telegram import InlineQueryResultArticle ,InputTextMessageContent
import logging

abuses = ['fuck','gay','mc','mf','motherfucker','bc','idiot']
class Abuse(BaseFilter):

    def filter(self,message):
        return "You retard" in message.text