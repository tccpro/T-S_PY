from telegram.ext import Updater,CallbackContext,CommandHandler,MessageHandler,Filters
from telegram import Update

# definitions ------------------------------------------------------
from bot.handlers import start_handler, message_handler, photo_handler

def main():
    updater = Updater(token='5152360674:AAEmDVZT4s-uhb-Xk-TDqiHb15hJGLgTtAo',use_context=True)

    dispatcher = updater.dispatcher

    # add handler ------------------------------------------------------
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handler)
    dispatcher.add_handler(photo_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()
