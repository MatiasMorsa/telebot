import telebot
import datetime
from telebot import types
import threading
import sys
from time import mktime
from datetime import datetime, date, time, timedelta
import calendar


##################################VARIABLES########################################

message_text_old = ""
lista = ["Ene","07","fiesta","24:45"]
lista_diaria = []

archivo = open("lista.txt", "r")
for item in archivo:
    lista.append(item)
archivo.close()

bot = telebot.TeleBot("347218102:AAFmZbhaoJgU2PvlWpEaNujwz8L5yLpsp-Q")
tb = telebot.AsyncTeleBot("347218102:AAFmZbhaoJgU2PvlWpEaNujwz8L5yLpsp-Q")

################################CONSULTA FECHA ACTUAL##########################
@bot.message_handler(regexp="fecha de hoy")
def manejo_consulta(message):
    ahora = date.today()
    bot.send_message(message.chat.id,"Fecha: " + str(ahora))
    bot.send_message(message.chat.id,"mes: " + str(ahora)[5:7])
    
    



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
    bot.register_next_step_handler(message, agregar_paso_2)

def agregar_paso_2(message):
    lista.append(message.text)
    markup = types.ReplyKeyboardMarkup()
    itembtn1 = types.KeyboardButton('01')
    itembtn2 = types.KeyboardButton('02')
    itembtn3 = types.KeyboardButton('03')
    itembtn4 = types.KeyboardButton('04')
    itembtn5 = types.KeyboardButton('05')
    itembtn6 = types.KeyboardButton('06')
    itembtn7 = types.KeyboardButton('07')
    itembtn8 = types.KeyboardButton('08')
    itembtn9 = types.KeyboardButton('09')
    itembtn10 = types.KeyboardButton('10')
    itembtn11 = types.KeyboardButton('11')
    itembtn12 = types.KeyboardButton('12')
    itembtn13 = types.KeyboardButton('13')
    itembtn14 = types.KeyboardButton('14')
    itembtn15 = types.KeyboardButton('15')
    itembtn16 = types.KeyboardButton('16')
    itembtn17 = types.KeyboardButton('17')
    itembtn18 = types.KeyboardButton('18')
    itembtn19 = types.KeyboardButton('19')
    itembtn20 = types.KeyboardButton('20')
    itembtn21 = types.KeyboardButton('21')
    itembtn22 = types.KeyboardButton('22')
    itembtn23 = types.KeyboardButton('23')
    itembtn24 = types.KeyboardButton('24')
    itembtn25 = types.KeyboardButton('25')
    itembtn26 = types.KeyboardButton('26')
    itembtn27 = types.KeyboardButton('27')
    itembtn28 = types.KeyboardButton('28')
    itembtn29 = types.KeyboardButton('29')
    itembtn30 = types.KeyboardButton('30')
    itembtn31 = types.KeyboardButton('31')
    
    if(message.text == "Feb"):
        markup.row(itembtn1, itembtn2,itembtn3,itembtn4,itembtn5,itembtn6,itembtn7)
        markup.row(itembtn8,itembtn9,itembtn10,itembtn11,itembtn12,itembtn13,itembtn14)
        markup.row(itembtn15,itembtn16,itembtn17,itembtn18,itembtn19,itembtn20,itembtn21)
        markup.row(itembtn22,itembtn23,itembtn24,itembtn25,itembtn26,itembtn27,itembtn28)
    elif((message.text == "Ene") or (message.text == "Mar") or (message.text == "May") or (message.text == "Jul") or (message.text == "Ago") or (message.text == "Oct") or (message.text == "Dic")):
        markup.row(itembtn1, itembtn2,itembtn3,itembtn4,itembtn5,itembtn6,itembtn7)
        markup.row(itembtn8,itembtn9,itembtn10,itembtn11,itembtn12,itembtn13,itembtn14)
        markup.row(itembtn15,itembtn16,itembtn17,itembtn18,itembtn19,itembtn20,itembtn21)
        markup.row(itembtn22,itembtn23,itembtn24,itembtn25,itembtn26,itembtn27,itembtn28)
        markup.row(itembtn29,itembtn30,itembtn31)
    else:
        markup.row(itembtn1, itembtn2,itembtn3,itembtn4,itembtn5,itembtn6,itembtn7)
        markup.row(itembtn8,itembtn9,itembtn10,itembtn11,itembtn12,itembtn13,itembtn14)
        markup.row(itembtn15,itembtn16,itembtn17,itembtn18,itembtn19,itembtn20,itembtn21)
        markup.row(itembtn22,itembtn23,itembtn24,itembtn25,itembtn26,itembtn27,itembtn28)
        markup.row(itembtn29,itembtn30)
    bot.send_message(message.chat.id, "Que dia :", reply_markup=markup)
    bot.register_next_step_handler(message,agregar_paso_3)
    

    
def agregar_paso_3(message):    
    lista.append(message.text)
    markup = types.ForceReply(selective=False)
    bot.send_message(message.chat.id, "Que evento :", reply_markup=markup)
    bot.register_next_step_handler(message,agregar_paso_4)
    
def agregar_paso_4(message):
    lista.append(message.text)
    markup = types.ForceReply(selective=False)
    bot.send_message(message.chat.id, "A que hora (si no sabe ingrese 99): ", reply_markup=markup)
    bot.register_next_step_handler(message,confirmacion)
    
def confirmacion(message):
    lista.append(message.text)
    archivo = open("lista.txt", "w") 
    archivo.seek(0)
    for item in lista:
        archivo.write("%s\ " % item)
    archivo.close()
    bot.send_message(message.chat.id,"Evento agregado")
    
def echo_all(message):
	bot.send_message(message.chat.id,"Perdon, no te entendi ")

bot.polling()
