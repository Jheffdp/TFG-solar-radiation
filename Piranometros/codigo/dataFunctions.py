from datetime import datetime, timedelta
import time

import csv
import pandas as pd
import os

from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.exceptions import ModbusException

##################################################################
#
# Funciones
#
##################################################################

# Función para obtener un registro del data logger. Previamente se ha
# establecido una conexión con ModbusTcpClient, que devuelve un cliente
# "client"
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
        if N == 4:
            datatype = client.DATATYPE.INT64
        else:
            datatype = client.DATATYPE.INT32
        value = client.convert_from_registers(rr.registers,
                                              data_type = datatype,
                                              word_order = "little"
                                              )
        value = value * mult
        
        return value

# Lectura de datos usando la función connect. La conexión tiene que
# estar previamente establecida. No cierra la conexión.
def readData(client, timestamp,
             IDs, names, DIRs, Ns, mults):
    row_data = {"timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S")}
    
    # Obtengo los datos de forma secuencial y almaceno los resultados
    # en el array row_data usando el ID correspondiente como nombre.
    for i in range(0, len(IDs)):
        # print(names[i], datetime.now().strftime("%H:%M:%S.%f"))
        val = connect(client, IDs[i], DIRs[i], Ns[i], mults[i])
        row_data[names[i]] = max(round(val, 2), 0) ## Valores
                                                   ## negativos a
                                                   ## cero, y redondea
                                                   ## dos decimales

    return row_data

# Incorpora los datos obtenidos "data" con "readData" en una nueva
# fila del fichero CSV. Este fichero está en la carpeta "directory" y
# se llama "filename"
def writeData(data, names, directory, filename):

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

## Esta función realiza el ciclo completo de lectura de un registro:
## conecta con la red, lee un registro y cierra la conexión.
def readElement(IP, ID, DIR, N, mult):
    client = ModbusClient(IP, port = 502)
    client.connect()
    if client.connected:
        try:
            rd = connect(client, ID, DIR, N, mult)
            return rd
        finally:
            client.close()
    else:
        print(f"Failed to connect to {myIP}.")


## Esta función realiza el ciclo completo de lectura de un conjunto de
## registros: conecta con la red, lee secuencialmente los registros
## del conjunto y cierra la conexión.
def readGroup(IP, IDs, names, DIRs, Ns, mults):
    client = ModbusClient(IP, port = 502)
    client.connect()
    if client.connected:
        try:
            now = datetime.now()
            rd = readData(client, now, IDs, names, DIRs, Ns, mults)
            return rd
        finally:
            client.close()
    else:
        print(f"Failed to connect to {myIP}.")
