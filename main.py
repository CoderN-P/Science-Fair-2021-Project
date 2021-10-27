from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from mongo_methods import *
import threading
from soil_moisture import SoilMoisture
from plant_watering import water_plant
import time

water_plant(5)



def main_process(soil_moisture1):
    while True:
        if soil_moisture1.needs_to_water:
            seconds = get_device()["seconds_to_water"]
            soil_moisture1.needs_to_water = False
            water_plant(seconds)
        
        time.sleep(1)

check_devices()

soil_moisture1 = SoilMoisture()


a = threading.Thread(
    target=soil_moisture1.background_reading
)
b = threading.Thread(target=main_process, args=(soil_moisture1,))
a.start()
b.start()
