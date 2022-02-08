"""
Telegram bot foro rolling a die.

Created by Jesús Jiménez Sánchez.
"""

from random import randint
from telegram.ext import Updater, CommandHandler
from tg_token import API_TOKEN


def roll(update, _context):
    '''
        Roll the dice.
    '''
    update.message.reply_text(randint(1, 6))


def main():
    '''
        Main.
    '''
    token = Updater(API_TOKEN, use_context=True)
    tk_dp = token.dispatcher

    tk_dp.add_handler(CommandHandler('roll', roll))

    token.start_polling()
    token.idle()


if __name__ == '__main__':
    main()
