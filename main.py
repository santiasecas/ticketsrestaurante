#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

ADMIN = os.environ["ADMIN"]

def start(update, context):
    nuevoUsuario = str(update.message.from_user.username)
    context.bot.send_message(ADMIN,'Nuevo usuario: @' + nuevoUsuario)
    update.message.reply_text('Welcome ' + nuevoUsuario + '\nYou can contact me at @santiasecas')

def calcularTickets(update, context):
    res = "Tickets 4:"
    argumentos = ['0', 'max4', '0']
    try:
        mensaje = update.message.text
        argumentos = mensaje.split(' ')
        if len(argumentos) == 1 or len(argumentos) == 3:
            if len(argumentos) == 1:
                cantidad = int(mensaje)
            elif len(argumentos) == 3:
                cantidad = int(argumentos[0])
                tope = argumentos[1]
                maximo = int(argumentos[2])
            cuatroTemp = 0
            tresTemp = 0
            ticketsRepartidos = int(cantidad / 7)
            i = 1
            if(tope == 'max4'):
                print('Hay un tope de 4')
            elif(tope =='max3'):
                print('Hay un tope de 3')

            while i >= -1:
                cuatroTemp = ticketsRepartidos + i
                cantidadRestante = int(cantidad  - (cuatroTemp * 4))
                tresTemp = int(cantidadRestante / 3)
                falta = cantidad - (cuatroTemp * 4) - (tresTemp * 3)
                if falta == 0:
                    res = "Tickets 4: " + str(cuatroTemp) + "\nTickets 3: " + str(tresTemp)
                i -= 1
            update.message.reply_text(res)
        else:
            update.message.reply_text("Por favor, envía un precio válido:")
            
    except:
        update.message.reply_text("Por favor, envía un precio válido:")

def main():
    TOKEN = os.environ["BOTTOKEN"]
    NAME = os.environ["NAME"]
    PORT = os.environ.get('PORT')
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, calcularTickets))

    updater.start_webhook(listen="0.0.0.0",port=int(PORT),url_path=TOKEN)
    updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
    updater.idle()
    
    updater.idle()

if __name__ == '__main__':
    main()