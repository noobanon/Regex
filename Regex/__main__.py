import datetime
import importlib
import re
from typing import Optional, List
from telegram import Message, Chat, Update, Bot, User
from telegram.ext.dispatcher import run_async, DispatcherHandlerStop, Dispatcher
from telegram.ext import CommandHandler
from Regix import dispatcher as dp
from Regix Import TOKEN
from Regix.regix import regix_load

IMPORTED = {}

for load in regix_load:
    imported = importlib.import_module("Regix.regix." + load)
    if not hasattr(imported, "__plugin_name__"):
        imported.__plugin_name__ = imported.__name__

    if not imported.__plugin_name__.lower() in IMPORTED:
        IMPORTED[imported.__plugin_name__.lower()] = imported

    if hasattr(imported, "help_plus") and imported.help_plus:
        HELP[imported.__plugin_name__.lower()] = imported



def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Hi Yo Supp I'm Just A Regex Bot For Fun For More Use /help!")


SEND_HELP = """ - s/<text1>/<text2>(/<flag>): Reply to a message with this to perform a sed operation on that message, replacing all \
occurrences of 'text1' with 'text2'. Flags are optional, and currently include 'i' for ignore case, 'g' for global, \
or nothing. Delimiters include `/`, `_`, `|`, and `:`. Text grouping is supported. The resulting message cannot be \
larger than {}.
*Reminder:* Sed uses some special characters to make matching easier, such as these: `+*.?\\`
If you want to use these characters, make sure you escape them!
eg: \\?."""

def help(update, context):
    """Send help when the command /help is issued."""
    update.message.reply_text(SEND_HELP, parse_mode=ParseMode.MARKDOWN)

def main():
    updater = Updater('TOKEN')
    start_handler = CommandHandler("start", start)
    start_handler = CommandHandler("help", help)
    dp.add_handler(start_handler)
    dp.add_handler(help_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
