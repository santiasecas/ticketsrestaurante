#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

ADMIN = os.environ["ADMIN"]

def start(update, context):
    bot.send_message(ADMIN,'Usuario iniciado: @' + str(update.message.from_user.username))
    update.message.reply_text('Bienvenido ' + update.message.from_user.username)

def calcularTickets(update, context):
    res = "Tickets 4:"
    cantidad = int(update.message.text)
    cuatroTemp = 0
    tresTemp = 0
    ticketsRepartidos = int(cantidad / 7)
    i = 1
    while i >= -1:
        cuatroTemp = ticketsRepartidos + i
        cantidadRestante = int(cantidad  - (cuatroTemp * 4))
        tresTemp = int(cantidadRestante / 3)
        falta = cantidad - (cuatroTemp * 4) - (tresTemp * 3)
        if falta == 0:
            res = "Tickets 4: " + str(cuatroTemp) + "\nTickets 3: " + str(tresTemp)
        i -= 1
    update.message.reply_text(res)

def main():
    TOKEN = os.environ["BOTTOKEN"]
    NAME = os.environ["NAME"]
    PORT = os.environ.get('PORT')
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, calcularTickets))

    updater.start_webhook(listen="0.0.0.0",port=int(PORT),url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
    
    updater.idle()

if __name__ == '__main__':
    main()