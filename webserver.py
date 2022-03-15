import flask
from plant_watering import water_plant
from mongo_methods import get_device
from flask_cors import cross_origin

app = flask.Flask(__name__)


@app.route("/webhook", methods="GET")
@cross_origin()
def webhook():
    seconds = get_device()["seconds_to_water"]
    water_plant(seconds)
    return "success"


def run():
    app.run(host="0.0.0.0", port=5000)
