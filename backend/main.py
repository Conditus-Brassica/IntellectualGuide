import asyncio
import random

import asyncio
import werkzeug.exceptions as wer_exp
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.datastructures import ImmutableMultiDict as imd

from backend.broker.broker_initializer import BROKER
from backend.db_categories import system_categories
from backend.broker.abstract_agents_broker import AbstractAgentsBroker
from backend.broker.agents_tasks.landmarks_by_sectors_agent_tasks import get_landmarks_in_sector_task

from backend.broker.agents_tasks.route_builder_task import build_route
from backend.broker.abstract_agents_broker import AbstractAgentsBroker
from backend.agents.crud_agent.crud_initializer import CRUD_AGENT




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
        async def get_sector_points():
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
                return wer_exp.BadRequest().code

            map_sectors_result = await AbstractAgentsBroker.call_agent_task(
                    get_landmarks_in_sector_task,
                )

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
        async def get_route():
            """
            Method for getting list of routing points.
            return: jsonify response
            """
            received = request.args
            gotten_json = imd.to_dict(received)
            print(gotten_json['start'][0])
            print("gotten jason   ", gotten_json)
            if gotten_json is None:
                self.__app__.logger.error("get_rout() returned BadRequest")
                return wer_exp.BadRequest()

            # TODO: task calling

            param = dict()
            param['user_login'] = ""
            param['start_end_points'] = {
                "coordinates": [
                    {"latitude": float((gotten_json['start'].split(','))[0]),
                     "longitude": float((gotten_json['start'].split(','))[1])},
                    {"latitude": float((gotten_json['finish'].split(','))[0]),
                     "longitude": float((gotten_json['finish'].split(','))[1])}
                ]
            }

            if len(gotten_json['catigories']) != 0:
                print("cats to send ", gotten_json['catigories'].lower().split(','))
                categories = self.__convert_categories_to(gotten_json['catigories'].split(','))
                param['categories_names'] = [i.lower() for i in categories]
            else:
                curr = self.__generate_cats()
                for i in range(len(curr)):
                    curr[i] = curr[i].lower()
                param['categories_names'] = curr

            print("param ", param)


            task = asyncio.create_task(
                AbstractAgentsBroker.call_agent_task(
                    build_route, param
                )
            )

            res = await task

            res = res.return_value

            print("res ", res)

            route = list()
            for i in res[0]['coordinates']:
                route.append([i['latitude'], i['longitude']])

            points = list()
            for i in res[1]:
                points.append({"name": i['recommendation']['name'],
                               "latlng": [i['recommendation']['latitude'], i['recommendation']['longitude']]})

            return jsonify({'route': route, 'points': points})

        @self.__app__.route("/api/v1/map/categories", methods=['GET'])
        def get_categories():
            lst = list()
            for value in system_categories.values():
                if value not in lst:
                    lst.append(value)
            print(lst)
            return lst

    def __convert_categories_to(self, curr_list_cat):
        """
        From front categories to system
        :return:
        """
        keys = system_categories.keys()

        system_cat_result = list()

        for i in keys:
            for j in curr_list_cat:
                if system_categories[i] == j:
                    system_cat_result.append(i)

        return system_cat_result

    def __convert_categories_from(self):
        """
        From system to front categories
        :return:
        """

    def __generate_cats(self):
        lst = list()
        for i in system_categories.keys():
            lst.append(i)

        random.shuffle(lst)

        lst = lst[:random.randint(5, len(lst) - 1)]

        return lst


async def main():
    await BROKER.startup()
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
    request_agent = RequestAgent(app)
    app.run(host="0.0.0.0", port=4444, debug=True)
    await BROKER.shutdown()
    await CRUD_AGENT.close()

if __name__ == "__main__":
    asyncio.run(main())


