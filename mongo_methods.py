import pymongo, dns
import commands, os

client = pymongo.MongoClient(os.getenv("MONGOURI"))

db = client.main_data

registered_devices = db.registered_devices

ip = commands.getoutput("hostname -I")


def check_devices() -> None:
    if not registered_devices.count_documents({"_id": ip}):
        registered_devices.insert_one(
            {
                "_id": ip,
                "Password": None,
                "seconds_to_water": 10,
                "last_watered": None,
                "temperature": None,
                "soil_moisture": None,
            }
        )


def get_device() -> dict:
    return dict(registered_devices.find_one({"_id": ip}))


def update_last_watered(time) -> None:
    registered_devices.update_one({"_id": ip}, {"$set": {"last_watered": time}})


def update_readings(temperature: float, soil_moisture: int) -> None:
    registered_devices.update_one(
        {"_id": ip},
        {"$set": {"temperature": temperature, "soil_moisture": soil_moisture}},
    )