import time
from mongo_methods import update_readings
import chirp
from plant_watering import water_plant
from mongo_methods import get_device
import datetime


chirp = chirp.Chirp(
    address=0x20,
    read_moist=True,
    read_temp=True,
    read_light=True,
    temp_scale="celsius",
    temp_offset=0,
)


class SoilMoisture:
    def __init__(self):
        self.soil_moisture = None
        self.temperature = None
        self.data_num = 0

    def background_reading(self):
        while True:
            chirp.trigger()
            self.soil_moisture = int(chirp.moist)
            print(self.soil_moisture)
            self.temperature = chirp.temp
            if self.data_num % 6 == 0:
                update_readings(self.soil_moisture, self.temperature)
            self.data_num += 1
            if self.soil_moisture < 800:
                seconds = get_device()["seconds_to_water"]
                water_plant(seconds)

            time.sleep(10)
