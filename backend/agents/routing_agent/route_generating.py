import openrouteservice as ors

import api_key


class RoutingAgent:
    def __init__(self):
        self.__client__ = ors.Client(key=api_key.__key__)
        self.__landmarks__ = []

    def set_points(self, points_list: list):
        self.__landmarks__ = points_list

        self.__landmarks__ = self.__reverse_coordinates__(self.__landmarks__)
        route = self.__create_optimized_route__()
        route = self.__reverse_coordinates__(route)

        return route

    @staticmethod
    def __reverse_coordinates__(coordinates_list: list):
        """
        Method revere coordinates because of osm (longitude, latitude),
        But normally it should be (latitude, longitude)
        :param coordinates_list:
        :return: list of reversed coordinates
        """
        coordinates_list = \
            [list(reversed(coord)) for coord in coordinates_list]
        return coordinates_list

    def __create_optimized_route__(self):
        route = self.__client__.directions(
            coordinates=self.__landmarks__,
            profile='driving-car',
            format='geojson',
            validate=False,
            optimize_waypoints=True
        )

        return route['features'][0]['geometry']['coordinates']
