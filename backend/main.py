import werkzeug.exceptions as wer_exp
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.datastructures import ImmutableMultiDict as imd

import backend.agents.json_schemas as schemas


class RequestAgent:
    """
    This class is for processing request about map sector landmarks.
    It gets information of client's map position.
    The response must be a list of landmarks data in the requested sector.
    """

    def __init__(self, flask_app: Flask):
        self.__app__ = flask_app
        self.__handle__()

    def __handle__(self):
        @self.__app__.route("/api/v1/sector/points", methods=["GET"])
        def get_sector_points():
            """
            Method gets the request for receiving list
            of landmarks in a specific sector.
            Returns a response of json list of landmarks and it's data.
            return: json response
            """
            received = request.args
            gotten_json = imd.to_dict(received)

            keys = gotten_json.keys()

            print(wer_exp.BadRequest())
            try:
                for i in keys:
                    gotten_json[i] = float(gotten_json[i])
            except ValueError:
                return wer_exp.BadRequest()

            if gotten_json is None:
                self.__app__.logger.error("get_sector_points() returned BadRequest")
                return wer_exp.BadRequest().code

            # TODO: task calling

            sending_json = {"points": [{"name": "name1",
                                        "lat": 54.098865472796994,
                                        "lng": 26.661071777343754,
                                        "type": "museum"}]}

            return jsonify(sending_json)

        @self.__app__.route("/api/v1/map/point", methods=["GET"])
        def get_point():
            """
            Method for getting info about one landmark.
            return: jsonify response
            """
            received = request.args
            gotten_json = imd.to_dict(received)

            if gotten_json is None:
                self.__app__.logger.error("get_point() returned BadRequest")
                return wer_exp.BadRequest()

            # TODO: task calling

            landmark = {}

            return jsonify(landmark)

        @self.__app__.route("/api/v1/map/route", methods=["GET"])
        def get_route():
            """
            Method for getting list of routing points.
            return: jsonify response
            """
            received = request.args
            gotten_json = imd.to_dict(received)

            if gotten_json is None:
                self.__app__.logger.error("get_rout() returned BadRequest")
                return wer_exp.BadRequest()

            # TODO: task calling

            route_points = {}

            return jsonify(route_points)


if __name__ == "__main__":
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
    request_agent = RequestAgent(app)
    app.run(host="0.0.0.0", port=4444, debug=True)
