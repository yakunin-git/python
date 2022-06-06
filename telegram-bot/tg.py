#!/usr/bin/python3.8
import requests
import sys

def tg_bot(bot_message):
    bot_token = "CHANGE_TO_YOU_BOT_TOKEN_HERE"
    bot_chatID = "CHANGE_TO_YOU_CHAT_ID_HERE"
    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + bot_chatID + "&parse_mode=Markdown&text=" + bot_message
    response = requests.get(send_text)
    return response.json()


def tg_send_message():
    if len(sys.argv) > 1:
        tg_message = sys.argv[1]
    else:
        exit(0)
    tg_bot(tg_message)

tg_send_message()

