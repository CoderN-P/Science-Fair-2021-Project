import time
from board import SCL, SDA
import busio
from mongo_methods import update_readings
from adafruit_seesaw.seesaw import Seesaw


i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)


class SoilMoisture:
    def __init__(self):
        self.needs_to_water = False
        self.soil_moisture = None
        self.temperature = None

    def background_reading(self):
        while True:
            self.soil_moisture = ss.moisture_read()
            self.temperature = ss.get_temp()
            update_readings(int(self.soil_moisture), float(self.temperature))
            print(
                f"Soil Moisture: {self.soil_moisture}, Temperature: {self.temperature}"
            )
            if self.soil_moisture < 400:
                self.needs_to_water = True

            time.sleep(10)
