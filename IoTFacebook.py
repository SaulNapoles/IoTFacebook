import RPi.GPIO as GPIO
import time
import requests
import random

#Creado por Saul Rodríguez

#incializacion
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Pin
ldr = 14 

#variable
estadoDia= "día"


#peticion post para mandar el estado del día
def estadoDeDia(value1):
    report = {}
    report["value1"] = value1
    requests.post("Aquí tu link de IFTTT", data=report)

#peticion post para mandar el estado de noche
def estadoDeNoche(value1):
    report = {}
    report["value1"] = value1
    requests.post("Aquí tu link de IFTTT", data=report)

#metodo para calcular la luz
def RCtime(RCpin):
    leer = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, False)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin) == False):
        leer += 1
    return leer

#While para publicar si es de día o de noche en Facebook
while True:
    hoy = RCtime(ldr)
    
    if hoy < 400: #si es de dia
        if estadoDia == "día":
            estadoDeDia(estadoDia)
            print("Es de día")
            estadoDia = "noche"

    else: #si es de noche
        if estadoDia == "noche":
            estadoDeNoche(estadoDia)
            print("Es de noche")
            estadoDia = "día"



