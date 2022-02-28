"""
Telegram bot foro rolling a die.

Created by Jesús Jiménez Sánchez.
"""

from random import randint
import requests
from telegram.ext import Updater, CommandHandler
from tg_token import API_TOKEN
from sticker_ids import ALL


URL = "https://api.telegram.org/bot{}/".format(API_TOKEN)


def get_url(url):
    '''
        Send request to the Telegram API.
    '''
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def send_sticker(chat_id, die_result):
    '''
        Respond with sticker.
    '''
    url = URL + "sendSticker?sticker={}&chat_id={}".format(die_result, chat_id)
    get_url(url)


def roll(update, _context):
    '''
        Roll the dice.
    '''
    die_result = randint(1, 6)
    send_sticker(update.message.chat_id, ALL[die_result - 1])
    update.message.reply_text(die_result)


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
