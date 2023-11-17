from flask import Flask, request, jsonify
from flask_cors import CORS
from jsonschema import validate, ValidationError, SchemaError
from werkzeug.datastructures import ImmutableMultiDict as imd
import werkzeug.exceptions as wer_exp

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
            try:
                for i in keys:
                    gotten_json[i] = float(gotten_json[i])
            except ValueError:
                return wer_exp.BadRequest()

            if gotten_json is None:
                self.__app__.logger.error("get_sector_points() returned BadRequest")
                return wer_exp.BadRequest()

            if not self.__validate_sector_schema_receive__(self, gotten_json):
                self.__app__.logger.error("get_sector_points() returned BadRequest")
                return wer_exp.BadRequest()

            # TODO: there"s must be a function of receiving json from lower agents

            # sending_json = {"a": "b"}
            # try:
            #     self.__validate_sector_schema_send__(self, sending_json)
            # except SchemaError:
            #     self.__app__.logger.error("get_sector_points() returned NotFound")
            #     return wer_exp.NotFound()

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

            # TODO: there"s must be a function of receiving json of about one point
            rout_points = {"A": "b"}
            try:
                self.__validate_point_schema_send__(self, rout_points)
            except SchemaError:
                self.__app__.logger.error("get_point() returned NotFound")
                return wer_exp.NotFound()

            return jsonify(rout_points)

        @self.__app__.route("/api/v1/map/route", methods=["GET"])
        def get_rout():
            """
            Method for getting list of routing points.
            return: jsonify response
            """
            received = request.args
            gotten_json = imd.to_dict(received)

            if gotten_json is None:
                self.__app__.logger.error("get_rout() returned BadRequest")
                return wer_exp.BadRequest()

            # TODO: there"s must be a function of receiving json of route points
            rout_points = {"A": "b"}

            try:
                self.__validate_rout_points_schema_send__(self, rout_points)
            except SchemaError:
                self.__app__.logger.error("get_rout() returned NotFound")
                return wer_exp.NotFound()

            return jsonify(rout_points)

    @staticmethod
    def __validate_sector_schema_receive__(self, gotten_json):
        """
        Validate sector received json.
        return bool
        """
        try:
            validate(gotten_json, schemas.sector_schema_receive)
            return True
        except ValidationError:
            self.__app__.logger.error("sector receive error")
            return False

    @staticmethod
    def __validate_sector_schema_send__(self, sending_json):
        """
        Validate sector sent json.
        return bool
        """
        try:
            validate(sending_json, schemas.sector_send_schema)
            return True
        except ValidationError:
            self.__app__.logger.error("sector send", ValidationError)
            return False

    @staticmethod
    def __validate_rout_points_schema_send__(self, sending_json):
        """
        Validate rout points send json.
        """
        try:
            validate(sending_json, schemas.send_rout_schema)
            return True
        except ValidationError:
            self.__app__.logger.error("rout points send", ValidationError)
            return False

    @staticmethod
    def __validate_point_schema_send__(self, sending_json):
        """
        Validate point send json.
        return: bool
        """
        try:
            validate(sending_json, schemas.send_point)
            return True
        except ValidationError:
            self.__app__.logger.error("point send", ValidationError)
            return False


if __name__ == "__main__":
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
    request_agent = RequestAgent(app)
    app.run(host="0.0.0.0", port=4444, debug=True)
