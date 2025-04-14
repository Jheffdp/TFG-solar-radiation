from datetime import datetime, timedelta
import time
import threading
import csv
import pandas as pd
import os
from apscheduler.schedulers.background import  BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

# Define la función para actualizar el archivo CSV
def actualizar_csv(nueva_fila):

    # Ruta del directorio donde se guardará el archivo
    directorio = r"C:\Users\etsidi_solar\Documents\Piranometros"
    nombre_archivo = "datos.csv"  # nombre del archivo
    # Ruta completa del archivo
    ruta_completa = os.path.join(directorio, nombre_archivo)
    
    # Escribe la nueva fila en el archivo CSV
    try:
        with open(ruta_completa, mode="a", newline="") as archivo:
            escritor_csv = csv.DictWriter(archivo, fieldnames=["timestamp",30, 31, 32, 33, 34,35,36,37,38,41,"vv","temp"])
            
            # Si el archivo está vacío, agrega el encabezado
            if archivo.tell() == 0:
                escritor_csv.writeheader()
            
            escritor_csv.writerow(nueva_fila)
            print(f"Fila añadida al archivo {nombre_archivo}: {nueva_fila}")
    except Exception as e:
        print(f"Error al actualizar el archivo CSV: {e}")

# Define el horario
hora_inicio = "6:00:00"  # Hora de inicio (formato HH:MM:SS)
hora_fin = "18:00:00"     # Hora de fin (formato HH:MM:SS)

# Convierte las horas a objetos datetime
hoy = datetime.now()
hora_inicio_datetime = datetime.strptime(hora_inicio, "%H:%M:%S").replace(
    year=hoy.year, month=hoy.month, day=hoy.day
)
hora_fin_datetime = datetime.strptime(hora_fin, "%H:%M:%S").replace(
    year=hoy.year, month=hoy.month, day=hoy.day
)


# Configura el programador de tareas
scheduler = BlockingScheduler()

ids_piranometros = [30, 31, 32, 33, 34,35,36,37,38,41]  # IDs de los piranómetros
DIR = 6  # Radiación corregida
N = 2  # Cantidad de registros a leer
mult = 0.001  # Multiplicador definido

# Función para conectar al cliente y obtener la lectura
def connect(client,ID, DIR, N, mult):
    
    rr = client.read_input_registers(address=DIR,  # REGISTRO HEX
                                     count=N,  # 2 para uint32, 4 para uint64
                                     slave=ID)  # ID MODBUS

    decoderBL = BinaryPayloadDecoder.fromRegisters(rr.registers,
                                                   byteorder=Endian.BIG,
                                                   wordorder=Endian.LITTLE)
    BL32 = decoderBL.decode_32bit_int()
    var_temp = BL32 * mult
    
    return var_temp

# Lectura de datos
def Lectura_piranometros(client, DIR, N, mult):
    row_data = {"timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}
    for ID in ids_piranometros:
        radiacion = connect(client, ID, DIR, N, mult)
        print(f"ID {ID}: {radiacion} W/m²")            
        #Guardar la radiación con el ID del piranómetro como nombre de la columna
        row_data[ID] = radiacion
    row_data["vv"] = connect(client, 29, 4, 2, 0.001)
    row_data["temp"] = connect(client, 29, 0, 2, 0.1)
    return row_data

# Función que se ejecutará cada 5 segundos
def tarea_programada():
    client = ModbusClient("138.100.103.115", port=502)
    client.connect()
    ahora = datetime.now()
    if hora_inicio_datetime <= ahora <= hora_fin_datetime:
        rd = Lectura_piranometros(client, DIR, N, mult)
        actualizar_csv(rd)
    else:
        print("Fuera del horario establecido. Deteniendo tarea.")
        scheduler.shutdown(wait=False)  # Detiene el programador cuando se pasa del horario
    client.close()

# Programa la tarea repetitiva
scheduler.add_job(
    tarea_programada,
    IntervalTrigger(seconds=5),
    start_date=hora_inicio_datetime,
    end_date=hora_fin_datetime
)


scheduler.start()