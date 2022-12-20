# HW_09_bot

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from log import log

def hello(update: Update, context: CallbackContext) -> None:
    log(update, context)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('5974854603:AAE51l57BX-RxoBrHZZsOxOqXsygUPBc5V4')

updater.dispatcher.add_handler(CommandHandler("hello", hello))




print("bot is run")

updater.start_polling()
updater.idle()