from mongo_methods import get_device
from plant_watering import water_plant
from main import soil_moisture1
import time

PIN = 11


def main_process():
    while True:
        if soil_moisture1.needs_to_water:
            seconds = get_device()["seconds_to_water"]
            water_plant(PIN, seconds)
            soil_moisture1.needs_to_water = False
        time.sleep(1)
