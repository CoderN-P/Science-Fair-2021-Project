from mongo_methods import update_last_watered
import time
from mongo_methods import update_last_watered
from datetime import datetime
from relay_hardware import Relay

RELAY = Relay(12, False)


def water_plant(seconds: int) -> None:
    RELAY.on()
    print('watering plant')
    time.sleep(seconds)
    RELAY.off()
    update_last_watered(datetime.now())
    print("Watered plant!!")
