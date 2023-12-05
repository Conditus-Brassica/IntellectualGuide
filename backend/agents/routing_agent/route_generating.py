import openrouteservice as ors

import api_key


class RoutingAgent:
    """
    Agent for finding route points.
    Usage: when you need to create optimized
    route between several points.
    """
    def __init__(self):
        self.__client__ = ors.Client(key=api_key.__key__)
        self.__landmarks__ = []

    def set_points(self, points_list: list):
        """
        Method finds all route points for provided points.
        :param points_list: [[latitude: float, longitude: float], ...]
        :return:
        """
        self.__landmarks__ = points_list

        self.__landmarks__ = self.__reverse_coordinates__(self.__landmarks__)
        route = self.__create_optimized_route__()
        route = self.__reverse_coordinates__(route)

        return route

    @staticmethod
    def __reverse_coordinates__(coordinates_list: list):
        """
        Method revere coordinates because of osm (longitude, latitude),
        but normally it should be (latitude, longitude).
        :param coordinates_list:
        :return: list of reversed coordinates
        """
        coordinates_list = \
            [list(reversed(coord)) for coord in coordinates_list]
        return coordinates_list

    def __create_optimized_route__(self):
        """
        Interaction with OpenRoutService API
        :return:
        """
        route = self.__client__.directions(
            coordinates=self.__landmarks__,
            profile='driving-car',
            format='geojson',
            validate=False,
            optimize_waypoints=True
        )

        return route['features'][0]['geometry']['coordinates']
