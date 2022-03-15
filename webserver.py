import flask
from plant_watering import water_plant
from flask import request
from mongo_methods import get_device
from flask_cors import cross_origin

app = flask.Flask(__name__)


@app.route("/webhook", methods="POST")
@cross_origin()
def webhook():
    data = request.get_json()
    device = get_device()
    if data["password"] != device["password"]:
        return "Wrong password"
    water_plant(device["seconds_to_water"])
    return "success"


def run():
    app.run(host="0.0.0.0", port=5000)
