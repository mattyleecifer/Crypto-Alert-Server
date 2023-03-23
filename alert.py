import telebot
import requests

BOT_TOKEN = 'telegramtoken'
bot = telebot.TeleBot(BOT_TOKEN)

# real key
API_KEY = "apikey"
SECRET_KEY = "secretkey"

from binance import Client
from binance.enums import *
import time, sys
client = Client(API_KEY, SECRET_KEY)

def getchatids():
    req = requests.get("https://api.telegram.org/bot[telegramtoken]/getUpdates")
    req = req.json()
    chatids = [i['message']["chat"]["id"] for i in req['result']]
    return list(set(chatids))

def sendmessage(message):
    chatids = getchatids()
    for user in chatids:
        bot.send_message(user, message)

watchcoin = sys.argv[1]
paircoin = sys.argv[2]
alert = float(sys.argv[3])
start = float(client.get_historical_trades(symbol=f'{watchcoin}{paircoin}')[-1]['price'])

while True:
    lastprice = float(client.get_historical_trades(symbol=f'{watchcoin}{paircoin}')[-1]['price'])
    if start > alert and lastprice < alert:
        sendmessage(f'{watchcoin}{paircoin} has crossed {alert}')
        break
    elif start < alert and lastprice > alert:
        sendmessage(f'{watchcoin}{paircoin} has crossed {alert}')
        break
    time.sleep(1)
