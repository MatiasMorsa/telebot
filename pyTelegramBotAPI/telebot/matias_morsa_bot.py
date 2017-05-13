import telebot
import datetime
from telebot import types
import threading
import sys
from time import mktime
from datetime import datetime, date, time, timedelta
import calendar



lista = ["Ene","07","fiesta","24:45"]
lista_diaria = []

bot = telebot.TeleBot("347218102:AAFmZbhaoJgU2PvlWpEaNujwz8L5yLpsp-Q")
tb = telebot.AsyncTeleBot("347218102:AAFmZbhaoJgU2PvlWpEaNujwz8L5yLpsp-Q")

################################CONSULTA FECHA ACTUAL##########################
@bot.message_handler(regexp="fecha de hoy")
def manejo_consulta(message):
    ahora = date.today()
    bot.send_message(message.chat.id,"Fecha: " + str(ahora))
    bot.send_message(message.chat.id,"dia: " + str(ahora)[5:7])
    
    



################### SALUDOS ############################################

@bot.message_handler(commands=["start"])
def send_welcome(message):
	bot.send_message(message.chat.id, "Facha ,como andas?")
	
	
@bot.message_handler(regexp="start")
def send_welcome(message):
	bot.send_message(message.chat.id, "Hola caballero")
	
@bot.message_handler(regexp="alo")
def send_welcome(message):
	bot.send_message(message.chat.id, "Hable mas fuerte que tengo una toalla")
	
	

#####################CONSULTA LISTA TOTAL ############################################
	
@bot.message_handler(regexp="lista de mañana")
def send_welcome(message):
	bot.send_message(message.chat.id,"a")
	

@bot.message_handler(regexp="tarea para hoy")
def manejo_consulta(message):
    ahora = date.today()
    if (len(lista)!=0):
        for x in range (0,len(lista)):
            if(((x//4)== (x / 4)) and (str(ahora)[5:7] == lista[x+1]) and ((str(ahora)[8:10] == lista[x]))):
                    
                    if (str(lista[x+3]) != "99"):
                        bot.send_message(message.chat.id,str((x//4)+1) + ") Tenes una " + lista[x+2] + " el " + lista[x+1] +" de " + lista[x] + " a las " + str(lista[x+3]) + " hs.")
                    else:
                        bot.send_message(message.chat.id,str((x//4)+1) + ") Tenes una " + lista[x+2] + " el " + lista[x+1] +" de " + lista[x])
        else:
            bot.send_message(message.chat.id,"Nada")
            bot.send_message(message.chat.id,"dia: " + str(ahora)[5:7])
            bot.send_message(message.chat.id,"mes: " + str(ahora)[8:10])



@bot.message_handler(regexp="cosas para hacer")
def funcion_lista(message):
    if (len(lista)!=0):
        for x in range (0,len(lista)):
            if((x//4)== (x / 4)):
                if (str(lista[x+3]) != "99"):
                    bot.send_message(message.chat.id,str((x//4)+1) + ") Tenes una " + lista[x+2] + " el " + lista[x+1] +" de " + lista[x] + " a las " + str(lista[x+3]) + " hs.")
                else:
                    bot.send_message(message.chat.id,str((x//4)+1) + ") Tenes una " + lista[x+2] + " el " + lista[x+1] +" de " + lista[x])
    else:
        bot.send_message(message.chat.id,"Nada")
 
 
 
############################### AGREGAR COSAS A LA LISTA ###################################################
 
@bot.message_handler(regexp="agregar")
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('Ene')
    itembtnb = types.KeyboardButton('Feb')
    itembtnc = types.KeyboardButton('Mar')
    itembtnd = types.KeyboardButton('Abr')
    itembtne = types.KeyboardButton('May')
    itembtnf = types.KeyboardButton('Jun')
    itembtng = types.KeyboardButton('Jul')
    itembtnh = types.KeyboardButton('Ago')
    itembtni = types.KeyboardButton('Sep')
    itembtnj = types.KeyboardButton('Oct')
    itembtnk = types.KeyboardButton('Nov')
    itembtnl = types.KeyboardButton('Dic')
    markup.row(itembtna, itembtnb,itembtnc,itembtnd)
    markup.row(itembtne,itembtnf,itembtng,itembtnh)
    markup.row(itembtni,itembtnj,itembtnk,itembtnl)
    bot.send_message(message.chat.id, "En que mes es:", reply_markup=markup)
    lista.append(message.text)
    bot.register_next_step_handler(message, agregar_paso_2)

def agregar_paso_2(message):
    markup = types.ForceReply(selective=False)
    bot.send_message(message.chat.id, "Que dia :", reply_markup=markup)
    lista.append(message.text)
    bot.register_next_step_handler(message,agregar_paso_3)
    
def agregar_paso_3(message):    
    markup = types.ForceReply(selective=False)
    bot.send_message(message.chat.id, "Que evento :", reply_markup=markup)
    lista.append(message.text)
    bot.register_next_step_handler(message,agregar_paso_4)
    
def agregar_paso_4(message):
    markup = types.ForceReply(selective=False)
    bot.send_message(message.chat.id, "A que hora (si no sabe ingrese 99): ", reply_markup=markup)
    lista.append(message.text)
    bot.register_next_step_handler(message,confirmacion)
    
def confirmacion(message):
    bot.send_message(message.chat.id,"Evento agregado")
    
    

bot.polling()



