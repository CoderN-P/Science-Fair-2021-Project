import pymongo, dns
import subprocess, os

client = pymongo.MongoClient(os.getenv("MONGOURI"))

db = client.main_data
print(os.getenv("MONGOURI"))
registered_devices = db.registered_devices

ip = subprocess.getoutput('hostname -I').split(' ')[0]
print(ip)
def check_devices() -> None:
    if not registered_devices.count_documents({"_id": ip}):
        registered_devices.insert_one(
            {
                "_id": ip,
                "Password": None,
                "seconds_to_water": 10,
                "last_watered": None,
                "temperature": None,
                "soil_moisture": [],
            }
        )


def get_device() -> dict:
    return dict(registered_devices.find_one({"_id": ip}))


def update_last_watered(time) -> None:
    registered_devices.update_one({"_id": ip}, {"$set": {"last_watered": time}})


def update_readings(soil_moisture, temperature) -> None:
    registered_devices.update_one(
        {"_id": ip},
        {"$set": {"temperature": temperature, "soil_moisture": soil_moisture}},
    )
