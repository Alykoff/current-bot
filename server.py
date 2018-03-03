# https://www.digitalocean.com/community/tutorials/docker-explained-how-to-containerize-python-web-applications
# https://github.com/datamachine/twx.botapi
import sys
import time
import re
import threading
import random
import telepot
from pprint import pprint
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup as Soup
import requests

"""
$ python3.5 skeleton_route.py <token>
"""

#message_with_inline_keyboard = None

def on_chat_message(msg):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='SNM/BTC', callback_data='press')],
               ])
    snmUrl = 'https://yobit.net/en/trade/SNM/BTC'
    print(msg)
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)

    if content_type != 'text':
        return
    user_id = msg['from']['id']
    content = requests.get(snmUrl).text
    soup = Soup(content, 'html.parser')
    lastPrice  =  soup.select('#label_last')
    if len(lastPrice) != 0:
        bot.sendMessage(user_id, '1 SNM = ' + lastPrice[0].text + ' BTC', reply_markup=keyboard)
    else:
        bot.sendMessage(user_id, 'Some trouble', reply_markup=keyboard)

def on_callback_query(msg):
    query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
    print('Callback query:', query_id, from_id, data)


def on_inline_query(msg):
    print('empty')

def on_chosen_inline_result(msg):
    result_id, from_id, query_string = telepot.glance(msg, flavor='chosen_inline_result')
    print('Chosen Inline Result:', result_id, from_id, query_string)

TOKEN = sys.argv[1]  # get token from command-line
bot = telepot.Bot(TOKEN)
#bot.update_bot_info().wait()

#keyboard = [
#    ['SNM/BTC']
#]
#reply_markup = ReplyKeyboardMarkup.create(keyboard)

answerer = telepot.helper.Answerer(bot)

bot.message_loop({'chat': on_chat_message})
print('Listening ...')
# Keep the program running.
while 1:
    time.sleep(10)
