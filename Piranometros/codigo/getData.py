from datetime import datetime, timedelta
import time

import csv
import pandas as pd
import os

from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.exceptions import ModbusException

import threading

from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from dataFunctions import connect, readData, writeData, readElement, readGroup

from parRadiation import radIDs, radNames, radDIRs, radNs, radMults
from parPower import powerIDs, powerNames, powerDIRs, powerNs, powerMults
from parVI import viIDs, viNames, viDIRs, viNs, viMults
from parTc import TcIDs, TcNames, TcDIRs, TcNs, TcMults

##################################################################
#
# Configuración de la conexión
#
##################################################################
# IP del data logger
myIP = "138.100.103.115"
# Carpeta de almacenamiento de datos
myDir = "C:/Users/etsidi_solar/Documents/Piranometros/csv/"


##################################################################
#
# Configuración de la tarea
#
##################################################################

def getData5s():
    client = ModbusClient(myIP, port = 502)
    client.connect()
    if client.connected:
        try:
            now = datetime.now()
            # Nombre del fichero CSV (un fichero por día)
            radCSV = "rad_" + now.strftime("%Y%m%d") + ".csv"  
            powerCSV = "power_" + now.strftime("%Y%m%d") + ".csv"
            # Obtiene datos de la red
            radData = readData(client, now,
                                 radIDs, radNames, radDIRs,
                                 radNs, radMults)

            powerData = readData(client, now,
                                 powerIDs, powerNames, powerDIRs,
                                 powerNs, powerMults)
            # Actualiza ficheros
            writeData(radData, radNames, myDir, radCSV)
            writeData(powerData, powerNames, myDir, powerCSV)
        finally:
            client.close()
    else:
        print(f"Failed to connect to {myIP}.")

def getData5m():
    client = ModbusClient(myIP, port = 502)
    client.connect()
    if client.connected:
        try:
            now = datetime.now()
            # Nombre del fichero CSV (un fichero por día)
            viCSV = "vi_" + now.strftime("%Y%m%d") + ".csv"  

            # Obtiene datos de la red
            viData = readData(client, now,
                              viIDs, viNames, viDIRs,
                              viNs, viMults)

            TcData = readData(client, now,
                              TcIDs, TcNames, TcDIRs,
                              TcNs, TcMults)
            # Une los resultados (merge)
            vals = TcData | viData
            names = TcNames + viNames
            # Actualiza ficheros
            writeData(vals, names, myDir, viCSV)
        finally:
            client.close()
    else:
        print(f"Failed to connect to {myIP}.")

## Programa la tarea repetitiva
## https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html
scheduler = BlockingScheduler()


## Ejecuta la tarea cada 5 segundos en la franja horaria de 6 a 21:59:55
## (resto de variables son * por defecto)
scheduler.add_job(getData5s,
                  trigger = CronTrigger(hour = '6-21', 
                                        second = '*/5'),
                  id='task5s')

## Ejecuta la tarea cada 5 minutos en la franja horaria de 6 a 21:55
## (resto de variables son * por defecto)
# ejecuta en el segundo 3 para no interferir con la tarea task5s
# (tarda algo más de 1 segundo en completarse)
scheduler.add_job(getData5m,
                  trigger = CronTrigger(hour = '6-21', 
                                        minute = '*/5',
                                        second = '3'),
                  id='task5m')

scheduler.start()


