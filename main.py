# -*- coding: utf-8 -*-
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

ADMIN = os.environ["ADMIN"]

# MANEJADORES DE COMANDOS
def start(bot, update):
	bot.send_message(ADMIN,'Usuario iniciado: @' + str(update.message.from_user.username))
	update.message.reply_text('Bienvenido ' + update.message.from_user.username)

# Se envía mensaje de ayuda con info
def help(bot, update):
	update.message.reply_text('Help!')

# Se envía mensaje de ayuda con info
def ping(bot, update):
	update.message.reply_text("pong")

def calcularTickets(bot, update):
	cantidad = update.message.text
    
    cuatroTemp = 0
    tresTemp = 0
    
    ticketsRepartidos = int(cantidad / 7)
    
    i = 1
    while i >= -1:
        cuatroTemp = ticketsRepartidos + i
        cantidadRestante = int(cantidad  - (cuatroTemp * 4))
        tresTemp = int(cantidadRestante / 3)
        falta =(cuatroTemp * 4) + (tresTemp * 3)
        if falta = 0:
            res = "Tickets 4: " + cuatroTemp + "\nTickets 3: " + tresTemp
    i -= 1
	update.message.reply_text(res)

# Se inicia el bot
def startBot():
	TOKEN = os.environ["BOTTOKEN"]
	NAME = os.environ["NAME"]
	PORT = os.environ.get('PORT')

	# Se configura el updater
	updater = Updater(TOKEN)
	dp = updater.dispatcher
	
	# Manejadores de comandos
	dp.add_handler(CommandHandler("help", help))
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(CommandHandler('ping', ping))
	dp.add_handler(MessageHandler(Filters.text, calcularTickets))
	
	# Lanza el webhook
	updater.start_webhook(listen="0.0.0.0",port=int(PORT),url_path=TOKEN)
	updater.bot.setWebhook("https://{}.herokuapp.com/{}".format(NAME, TOKEN))
	updater.idle()

if __name__ == "__main__":
	startBot()