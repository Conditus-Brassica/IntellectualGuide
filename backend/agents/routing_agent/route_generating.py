from pprint import pprint

import openrouteservice as ors

import asyncio

from pure_route_generating_agent import PureRoutingAgent
import api_key


class RoutingAgent(PureRoutingAgent):
    """
    Agent for finding route points.
    Usage: when you need to create optimized
    route between several points.

    Uses api_key in api_key.py
    """

    def __init__(self):
        self.__client__ = ors.Client(key=api_key.__key__)
        self.__landmarks = []

    async def get_optimized_route(self, landmark_list: list):
        """
        Method finds all optimized route points for provided points.
        :param landmark_list: [[latitude: float, longitude: float], ...]
        :return: Route points, landmarks in route order
        """
        self.__landmarks = landmark_list

        self.__landmarks = self.__reverse_coordinates(self.__landmarks)
        route = await self.__create_optimized_route()[0]
        route = self.__reverse_coordinates(route)

        return route

    async def get_optimized_route_main_points(self, landmark_list: list):
        """
        Method finds all optimized route points for provided points.
        Return one point per 30 km.
        :param landmark_list: [[latitude: float, longitude: float], ...]
        :return: Route points, landmarks in route order
        """
        self.__landmarks = landmark_list

        self.__landmarks = self.__reverse_coordinates(self.__landmarks)
        route = await self.__create_optimized_route()

        main_points = []
        k = 0
        for i in route:
            if k == 130:
                main_points.append(i)  # 130 - points every 30 km of route
                k = 0
            k += 1

        main_points = self.__reverse_coordinates(main_points)

        if len(route) < 130:
            main_points.append(route[0])
            main_points.append(route[-1])

        return main_points

    @staticmethod
    def __reverse_coordinates(coordinates_list: list):
        """
        Method revere coordinates because of osm (longitude, latitude),
        but normally it should be (latitude, longitude).
        :param coordinates_list:
        :return: list of reversed coordinates
        """
        coordinates_list = \
            [list(reversed(coord)) for coord in coordinates_list]

        return coordinates_list

    async def __create_optimized_route(self):
        """
        Interaction with OpenRoutService API
        :return:
        """
        route = self.__client__.directions(
            coordinates=self.__landmarks,
            profile='driving-car',
            format='geojson',
            validate=False,
            optimize_waypoints=True
        )
        # await asyncio.sleep(5)
        return route['features'][0]['geometry']['coordinates']


# async def main():
#     a = RoutingAgent()
#     res = asyncio.create_task(
#         a.get_route_optimized([[52.19797604067352, 24.43870667812846], [54.490638791728756, 30.4701524897013],
#                                [53.93429515309309, 27.113365683855704], [53.8602548114542, 30.38039883179099],
#                                [54.490638791728756, 25.85681447311136]]))
#
#     res1 = asyncio.create_task(
#         a.get_route_optimized([[52.19797604067352, 24.43870667812846], [54.490638791728756, 30.4701524897013],
#                                [53.93429515309309, 27.113365683855704], [53.8602548114542, 30.38039883179099],
#                                [54.490638791728756, 25.85681447311136]]))
#
#     res2 = asyncio.create_task(
#         a.get_route_optimized([[52.19797604067352, 24.43870667812846], [54.490638791728756, 30.4701524897013],
#                                [53.93429515309309, 27.113365683855704], [53.8602548114542, 30.38039883179099],
#                                [54.490638791728756, 25.85681447311136]]))
#
#     res3 = asyncio.create_task(
#         a.get_route_optimized([[52.19797604067352, 24.43870667812846], [54.490638791728756, 30.4701524897013],
#                                [53.93429515309309, 27.113365683855704], [53.8602548114542, 30.38039883179099],
#                                [54.490638791728756, 25.85681447311136]]))
#
#     res4 = asyncio.create_task(
#         a.get_route_optimized([[52.19797604067352, 24.43870667812846], [54.490638791728756, 30.4701524897013],
#                                [53.93429515309309, 27.113365683855704], [53.8602548114542, 30.38039883179099],
#                                [54.490638791728756, 25.85681447311136]]))
#
#     print(await res)
#     print(await res1)
#     print(await res2)
#     print(await res3)
#     print(await res4)
#
#
# asyncio.run(main())

# async def main():
#     a = RoutingAgent()
#     res = asyncio.create_task(a.get_optimized_route_main_points(
#         [[52.19797604067352, 24.43870667812846], [54.490638791728756, 30.4701524897013],
#          [53.93429515309309, 27.113365683855704], [53.8602548114542, 30.38039883179099],
#          [54.490638791728756, 25.85681447311136]]))
#     print(len(await res))
#
#
# asyncio.run(main())
