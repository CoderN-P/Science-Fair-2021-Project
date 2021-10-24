from mongo_methods import update_last_watered
from relay_hardware import Relay
import time
from mongo_methods import update_last_watered
from datetime import datetime


def water_plant(pin: int, seconds: int) -> None:
    RELAY = Relay(pin, False)
    RELAY.on()
    time.sleep(seconds)
    RELAY.off()
    update_last_watered(datetime.now())
    print("Watered plant!!")
