#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import configparser

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

ruta = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(f'{ruta}/config.ini')

ADMIN = config['BOT_CONFIG']['ADMIN']

def start(update, context):
    nuevo_usuario = str(update.message.from_user.username)
    context.bot.send_message(ADMIN,f'Nuevo usuario: @{nuevo_usuario}')
    update.message.reply_text(f'Welcome, {nuevo_usuario}\nYou can contact me at @santiasecas')

def calcularTickets(update, context):
    res = "Tickets 4:"
    argumentos = ['0', 'max4', '0']
    try:
        mensaje = update.message.text
        argumentos = mensaje.split(' ')
        cantidad = int(argumentos[0])
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

    except:
        update.message.reply_text("Por favor, envía un precio válido:")

def main():
    TOKEN = config['BOT_CONFIG']['TOKEN']
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, calcularTickets))

    updater.start_polling()    
    updater.idle()

if __name__ == '__main__':
    main()