#Hijos de Abraham
#Librerias para programar
import serial
import time
from datetime import date
from datetime import datetime
from firebase import firebase

base = firebase.FirebaseApplication("https://fir-hack-b7b89.firebaseio.com/",None)
#Comunicacion con arduino
arduino=serial.Serial('COM4',9600)
time.sleep(2) 

#Leemos el puerto serial
dato=arduino.readline()

#Programa main
while(dato!=b'x\r\n'): 

    #Fecha actual
    now = datetime.now()

    #Hará un accion dependiendo el dato leido
    if(dato==b'a\r\n'): 
        print("Se presiono boton 1")
        datos = {
            'ID': '1',
            'Estado':' Activo',
            'Direccion': 'Tec',
            'Fecha': now
        }
        base.post("\Registro_Botones",datos)
    
    elif(dato==b'b\r\n'): 
        print("Se presiono boton 2")
        datos = {
            'ID': '2',
            'Estado':' Activo',
            'Direccion': 'Corona',
            'Fecha': now
        }
        base.post("\Registro_Botones",datos)     
    elif(dato==b'c\r\n'): 
        print("Se presiono boton 3")
        datos = {
            'ID': '3',
            'Estado':' Activo',
            'Direccion': 'Boulevard',
            'Fecha': now
        }
        base.post("\Registro_Botones",datos)
    elif(dato==b'd\r\n'): 
        print("Se presiono boton 4")
        datos = {
            'ID': '4',
            'Estado':' Activo',
            'Direccion': 'Galerias',
            'Fecha': now
        }
        base.post("\Registro_Botones",datos)
    elif(dato==b'e\r\n'): 
        print("Se presiono boton 5")
        datos = {
            'ID': '5',
            'Estado':' Activo',
            'Direccion': 'Costco',
            'Fecha': now
        }
        base.post("\Registro_Botones",datos)
    dato=arduino.readline()

arduino.close()

