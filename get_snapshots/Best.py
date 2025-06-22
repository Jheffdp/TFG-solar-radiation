import requests
from datetime import datetime, timedelta
import time
import os
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_dir= f'./logs'
if not os.path.exists(log_dir):
        os.makedirs(log_dir)
log_filename=os.path.join(f'./logs/snapshot_best_{time.strftime("%Y%m%d")}.log')
handler=logging.FileHandler(log_filename,mode='w+')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

def get_imagen():
    try:
        # Registra hora del sistema
        now = datetime.now()
        # Configura sesión
        session = requests.Session()
        session.auth = ("user-a", "qX7cj90H!")
        # Obtiene imagen
        response = session.get('http://138.100.103.114/cgi-bin/DownloadBestImage?')
        # Da formato a hora para nombrar directorio y fichero
        timestr_date = now.strftime("%Y%m%d")
        timestr_datetime = now.strftime("%Y%m%d_%H%M%S")
        # Emplea un directorio para cada día
        directory = f'./snapshots_best/{timestr_date}'
        # Crea el directorio si no existe
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Alamacena la imagen    
        with open(f'{directory}/rad_{timestr_datetime}.jpg', 'wb') as file:
            file.write(response.content)
            logger.info(f'Se añade rad_{timestr_datetime}.jpg')
    # Gestiona errores        
    except Exception as error:
            logger.error('Se obtuvo el siguiente error: ' + repr(error))
            print('Se obtuvo el siguiente error: ' + repr(error))

## Programa la tarea repetitiva
## https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html
scheduler = BlockingScheduler()

## Ejecuta la tarea cada 2 minutos en la franja horaria de 22 a 23:58:00
## (resto de variables son * por defecto)
scheduler.add_job(get_imagen,
                  trigger=CronTrigger(hour='17-18',
                                      second = '*/15'),
                  id='task2min')

scheduler.start()
logger.debug('Comienza el programa')
logger.info('Procesando con normalidad')
