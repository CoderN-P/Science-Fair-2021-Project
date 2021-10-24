from mongo_methods import get_device
from plant_watering import water_plant
from main import soil_moisture1

PIN = 11


def main_process():
    if soil_moisture1:
        seconds = get_device()["seconds_to_water"]
        water_plant(PIN, seconds)
