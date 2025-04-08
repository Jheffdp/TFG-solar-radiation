from datetime import datetime, timedelta
import time
import threading
import csv
import pandas as pd
import os
import logging
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
# from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.exceptions import ModbusException

##################################################################
#
# Funciones
#
##################################################################

# Función para obtener un registro del data logger. Previamente se ha
# establecido una conexión con ModbusClient, que devuelve un cliente
# "client" (ver función "task")
def connect(client, ID, DIR, N, mult):
    
    try:
        rr = client.read_input_registers(address = DIR,  # REGISTRO HEX
                                     count = N,  # 2 para uint32, 4 para uint64
                                     slave = ID)  # ID MODBUS
    except ModbusException as e:
        print(f"Failed to read data, {e}.")
        client.close()
        return
    else:
##        decoderBL = BinaryPayloadDecoder.fromRegisters(rr.registers,
##                                                       byteorder = Endian.BIG,
##                                                       wordorder = Endian.LITTLE)
##        BL32 = decoderBL.decode_32bit_int()
        value = client.convert_from_registers(rr.registers,
                                              data_type=client.DATATYPE.INT32,
                                              word_order = "little"
                                              )
        value = value * mult
        
        return value

# Lectura de datos usando la función connect
def get_data(client, timestamp,
             IDs, names, DIRs, Ns, mults):
    row_data = {"timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S")}
    
    # Obtengo los datos de forma secuencial y almaceno los resultados
    # en el array row_data usando el ID correspondiente como nombre.
    for i in range(0, len(IDs)): 
        val = connect(client, IDs[i], DIRs[i], Ns[i], mults[i])
        row_data[names[i]] = max(round(val, 2), 0) ## Valores
                                                   ## negativos a
                                                   ## cero, y redondea
                                                   ## dos decimales

    return row_data

# Incorpora los datos obtenidos "data" con "get_data" en una nueva
# fila del fichero CSV. Este fichero está en la carpeta "directory" y
# se llama "filename"
def update_csv(data, names, directory, filename):

    # Ruta completa del archivo
    filepath = os.path.join(directory, filename)

    header = names.copy()
    header.insert(0, "timestamp")
    # Escribe la nueva fila en el archivo CSV
    try:
        with open(filepath, mode="a", newline="") as myFile:
            writer_csv = csv.DictWriter(myFile, fieldnames = header)
            
            # Si el archivo está vacío, agrega el encabezado
            if myFile.tell() == 0:
                writer_csv.writeheader()
            
            writer_csv.writerow(data)

    except Exception as e:
        print(f"Error al actualizar el archivo CSV: {e}")



##################################################################
#
# Asignación de valores a parámetros
#
##################################################################
# IP del data logger
myIP = "138.100.103.115"
# Carpeta de almacenamiento de datos
myDir = "C:/Users/etsidi_solar/Documents/Piranometros/csv/"

IDs = [30, 31, 32, 33, 34, 35, 36, 37, 38,
       41, 42, 43,
       29, 29]  

names = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9",
         "P0", "PH", "Pinc",
         "ws", "temp"]

DIRs = [6] * 12 + [4, 0]

Ns = [2] * 14

mults = [0.001] * 13 + [0.1]

##################################################################
#
# Configuración de la tarea
#
##################################################################
def task():
    client = ModbusClient(myIP, port = 502)
    client.connect()
    if client.connected:
        try:
            now = datetime.now()
            # Nombre del fichero CSV (un fichero por día)
            myCSV = "datos" + now.strftime("%Y%m%d") + ".csv"  
            rd = get_data(client, now, IDs, names, DIRs, Ns, mults)
            update_csv(rd, names, myDir, myCSV)
        finally:
            client.close()
    else:
        print(f"Failed to connect to {myIP}.")

# Programa la tarea repetitiva
scheduler = BlockingScheduler()

## Ejecuta la tarea cada 5 segundos en la franja horaria de 6 a 21:59:55
## (resto de variables son * por defecto,
## https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html)
scheduler.add_job(task,
                  trigger = CronTrigger(hour = '6-21', 
                                        second = '*/5'),
                  id='my_task')

# scheduler.add_job(task,
#                   trigger = CronTrigger(hour = '10',
#                                         minute = '19-20',
#                                         second = '*/5'),
#                   id='my_task')

scheduler.start()


