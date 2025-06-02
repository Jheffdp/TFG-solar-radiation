import requests
import time
import os
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_filename=os.path.join(f'.\logs\snapshot_{time.strftime("%Y%m%d")}.log')
handler=logging.FileHandler(log_filename,mode='w+')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

def get_imagen():
    try:
        session = requests.Session()
        session.auth = ("user-a", "qX7cj90H!")
        timestr_date = time.strftime("%Y%m%d")
        timestr_datetime = time.strftime("%Y%m%d_%H%M%S")
        response = session.get('http://138.100.103.114/cgi-bin/DownloadLiveImage?')
        directory = f'.\snapshots\\{timestr_date}'
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(f'{directory}\\rad_{timestr_datetime}.jpg', 'wb') as file:
            file.write(response.content)
            logger.info(f'Se añade rad_{timestr_datetime}.jpg')
    except Exception as error:
            logger.error('Se obtuvo el siguiente error: ' + repr(error))
            print('Se obtuvo el siguiente error: ' + repr(error))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    ## Programa la tarea repetitiva
    ## https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html
    scheduler = BlockingScheduler()

    ## Ejecuta la tarea cada 5 segundos en la franja horaria de 6 a 21:59:55
    ## (resto de variables son * por defecto)
    scheduler.add_job(get_imagen,
                      trigger=CronTrigger(hour='20-21',
                                          second = '*/15'),
                      id='task15min')

    scheduler.start()
    logger.debug('Comienza el programa')
    logger.info('Procesando con normalidad')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
