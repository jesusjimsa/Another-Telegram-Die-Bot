"""
Telegram bot for rolling a die.

Created by Jesús Jiménez Sánchez.
"""

from random import randint
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from tg_token import API_TOKEN
from sticker_ids import ALL


URL = f"https://api.telegram.org/bot{API_TOKEN}/"


def get_url(url):
    '''
        Send request to the Telegram API.
    '''
    response = requests.get(url, timeout=60)
    content = response.content.decode("utf8")
    return content


def send_sticker(chat_id, die_result):
    '''
        Respond with sticker.
    '''
    url = URL + f"sendSticker?sticker={die_result}&chat_id={chat_id}"
    get_url(url)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''
        Welcome message
    '''
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Welcome!\nTo roll a die, use the /roll command.")

async def roll(update, _context):
    '''
        Roll the dice.
    '''
    die_result = randint(1, 6)
    send_sticker(update.message.chat_id, ALL[die_result - 1])
    await update.message.reply_text(die_result)


def main():
    '''
        Main.
    '''
    app = ApplicationBuilder().token(API_TOKEN).build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler("roll", roll))

    app.run_polling()


if __name__ == '__main__':
    main()
