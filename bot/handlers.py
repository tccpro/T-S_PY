# define hanndlers ------------------------------------------------------
from telegram.ext import CommandHandler, MessageHandler, Filters

from bot.callback_methods import start, text_message, photo_message

start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text,text_message)
photo_handler = MessageHandler(Filters.photo,photo_message)
