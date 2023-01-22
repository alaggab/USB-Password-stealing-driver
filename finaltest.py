import requests
import telebot
import time
import json
import sys as n
import time as mm

bot=telebot.TeleBot("1439829514:AAGO0AGcxVmz-g7FZ6ecpz4PvheJTB_Fx_I")

'''server=Flask(__name__)'''

def start_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width = 2
    a=KeyboardButton('🔎 Insta Lookup')
    markup.row(a)
    return markup

@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_chat_action(msg.chat.id, 'typing')
    bot.send_message(msg.chat.id,'Hello ' + msg.from_user.first_name+"\nUse 🔎 *Insta Lookup* to Find Insta deatials",reply_markup=start_markup())

@bot.message_handler(regexp='🔎 Insta Lookup')
def ip_handler(message):    
    bot.send_chat_action(message.chat.id, 'typing')
    sent = bot.send_message(message.chat.id, "Send Intagram Username")
    bot.register_next_step_handler(sent, username)


def username(message):
    user = message.text
    s = '35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{"q":\"'+user+'\","guid":"b449de3c-1663-47bc-8cca-e83b570b60d1","device_id":"615d8b7997acf12b"}'
    userAAgent= "Instagram 99.4.0"
    url = 'https://i.instagram.com/api/v1/users/lookup/'
    myobj = {'signed_body': s,"ig_sig_key_version":"9"}
    x = requests.post(url,headers={'User-Agent':userAAgent}, data = myobj)
    try:
    	
    	bot.send_chat_action(message.chat.id, 'typing')
    	bot.send_message(message.chat.id,x.text )
    except KeyError:
        bot.send_chat_action(message.chat.id, 'typing')
        bot.send_message(message.chat.id,'❌ invalid IP address')



while True:
	try:
		bot.infinity_polling(True)
	except Exception:
		time.sleep(1)
