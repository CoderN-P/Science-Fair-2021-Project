from dotenv import load_dotenv
from mongo_methods import *
import threading
from soil_moisture import SoilMoisture
from run import main_process

load_dotenv()
check_devices()

soil_moisture1 = SoilMoisture()

a = threading.thread(
    name="background_reading", target=soil_moisture1.background_reading
)
b = threading.thread(name="main_process", target=main_process)
a.start()
b.start()
