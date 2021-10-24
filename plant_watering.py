from relay_hardware import Relay
import time
from mongomethods import set_update
from datetime import datetime


def water_plant(pin: int, seconds: int) -> None:
    RELAY = Relay(pin, False)
    RELAY.on()
    time.sleep(seconds)
    relay.off()
    set_update(datetime.now())
    print("Watered plant!!")
