from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
from mongo_methods import *
import threading
from soil_moisture import SoilMoisture
from webserver import run


check_devices()

soil_moisture1 = SoilMoisture()


a = threading.Thread(target=soil_moisture1.background_reading)
b = threading.Thread(target=run)
a.start()
b.start()
