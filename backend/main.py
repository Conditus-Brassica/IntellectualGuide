from flask import Flask, request, jsonify
from jsonschema import validate, ValidationError

import backend.agents.json_schemas as schemas


class RequestAgent:
    """
    This class is for processing request about map sector landmarks.
    It gets information of client's map position.
    The response must be a list of landmarks data in the requested sector.
    """

    def __init__(self, flask_app: Flask):
        self.__app__ = flask_app
        self.handle()

    def handle(self):
        @self.__app__.get('/')
        def get_sector_points():
            """
            Method gets the request for receiving list
            of landmarks in a specific sector.
            Returns a response of json list of landmarks and it's data.
            :return: json response
            """
            gotten_json = request.get_json()
            if gotten_json is None:
                self.__app__.logger.error("get_sector_points() returned None")
                return jsonify([])

            if not self.validate_sector_schema_receive(self, gotten_json):
                return jsonify([])

            # TODO: there's must be a function of receiving json from lower agents
            sending_json = {"a": "b"}

            if not self.validate_sector_schema_send(self, sending_json):
                return jsonify([])

            return jsonify(sending_json)

        @self.__app__.get('/')
        def get_rout_points():
            # TODO: there's must be a function of receiving json of route points
            rout_points = {"A": "b"}

            if not self.validate_rout_points(self, rout_points):
                return jsonify([])

            return jsonify(rout_points)

    @staticmethod
    def validate_sector_schema_receive(self, gotten_json):
        try:
            validate(gotten_json, schemas.sector_schema_receive)
            return True
        except ValidationError:
            self.__app__.logger.error("sector receive", ValidationError)
            return False

    @staticmethod
    def validate_sector_schema_send(self, sending_json):
        try:
            validate(sending_json, schemas.sector_send_schema)
            return True
        except ValidationError:
            self.__app__.logger.error("sector send", ValidationError)
            return False

    @staticmethod
    def validate_rout_points(self, sending_json):
        try:
            validate(sending_json, schemas.send_rout_schema)
            return True
        except ValidationError:
            self.__app__.logger.error("rout points", ValidationError)
            return False


if __name__ == "__main__":
    app = Flask(__name__)
    request_agent = RequestAgent(app)
    app.run(host='0.0.0.0', port=4444, debug=True)
