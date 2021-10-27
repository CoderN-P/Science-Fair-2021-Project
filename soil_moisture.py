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
            self.soil_moisture = int(ss.moisture_read())
            print(self.soil_moisture)
            update_readings(self.soil_moisture, self.temperature)
            self.temperature = ss.get_temp()
            if self.soil_moisture < 800:
                    self.needs_to_water = True

            time.sleep(10)
