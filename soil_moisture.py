import time
from board import SCL, SDA
import busio
from mongo_methods import update_readings
from adafruit_seesaw.seesaw import Seesaw
from plant_watering import water_plant
from mongo_methods import get_device

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)


class SoilMoisture:
    def __init__(self):
        self.soil_moisture = None
        self.temperature = None

    def background_reading(self):
        while True:
            self.soil_moisture = int(ss.moisture_read())
            print(self.soil_moisture)
            update_readings(self.soil_moisture, self.temperature)
            self.temperature = ss.get_temp()
            if self.soil_moisture < 800:
                seconds = get_device()["seconds_to_water"]
                water_plant(seconds)

            time.sleep(10)
