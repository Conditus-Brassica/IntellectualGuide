import asyncio
import json

from aiologger.loggers.json import JsonLogger
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from backend.agents.landmarks_by_sectors_agent.pure_landmarks_by_sectors_agent import PURELandmarksBySectorsAgent
from backend.broker.abstract_agents_broker import AbstractAgentsBroker
from backend.broker.agents_tasks.crud_agent_tasks import landmarks_of_categories_in_map_sectors_task, landmarks_in_map_sectors_task
from backend.agents.landmarks_by_sectors_agent.squares_params_json_validation import *

logger = JsonLogger.with_default_handlers(
    level="DEBUG",
    serializer_kwargs={'ensure_ascii': False},
)


class LandmarksBySectorsAgent(PURELandmarksBySectorsAgent):
    LAT_DIFFERENCE = 0.312
    LONG_DIFFERENCE = 0.611

    single_landmarks_agent = None

    def __init__(self):
        self._squares_in_sector = {"map_sector_names": []}
        self._cache = {}
        self._result = {}

    async def get_landmarks_in_sector(self, jsom_params: dict):
        # Check if format of dictionary is right using validator
        await self._coords_of_square_validation(jsom_params)
        self._get_sectors_in_sector(jsom_params)
        # Comparing with cache, then updating of cache
        self._squares_in_sector[0] = [i for i in self._squares_in_sector[0] not in self._cache[0]]
        self._set_cache()
        if len(self._cache["map_sector_names"]) != 0:
            landmarks_sectors_async_task = asyncio.create_task(
                AbstractAgentsBroker.call_agent_task(
                    landmarks_in_map_sectors_task,
                    self._squares_in_sector
                )
            )
            result_task = await landmarks_sectors_async_task
            self._result = result_task.return_value
        return self._result

    async def get_landmarks_by_categories_in_sector(self, jsom_params: dict):
        await self._coords_of_square_with_categories_validation(jsom_params)
        self._get_sectors_in_sector(jsom_params)
        self._squares_in_sector[0] = [i for i in self._squares_in_sector[0] not in self._cache[0]]
        self._squares_in_sector.update(jsom_params["categories_names"])
        self._set_cache()
        if len(self._cache["map_sector_names"]) != 0:
            landmarks_sectors_categories_async_task = asyncio.create_task(
                AbstractAgentsBroker.call_agent_task(
                    landmarks_of_categories_in_map_sectors_task, self._squares_in_sector
                )
            )
            result_task = await landmarks_sectors_categories_async_task
            self._result = result_task.return_value
        return self._result

    def _set_cache(self):
        self._cache["map_sector_names"].append(self._squares_in_sector[0])
        # To have only unique elements
        self._cache["map_sector_names"] = list(set(self._cache["map_sector_names"]))
        if len(self._cache.get("map_sector_names", [])) > 60:
            # Truncate the cache to the desired size
            self._cache["map_sector_names"] = self._cache["map_sector_names"][-60:]

    def _get_sectors_in_sector(self, coords_of_sector: dict):
        data = json.load(open("new_squares.json"))
        for element in data:
            if (coords_of_sector["TL"]["longitude"] - self.LONG_DIFFERENCE <= element["TL"]["longitude"] <
                element["BR"]["longitude"] <=
                coords_of_sector["BR"]["longitude"] + self.LONG_DIFFERENCE) and (
                    coords_of_sector["BR"]["latitude"] - self.LAT_DIFFERENCE <= element["BR"]["latitude"] <
                    element["TL"]["latitude"] <=
                    coords_of_sector["TL"]["latitude"] + self.LAT_DIFFERENCE):
                self._squares_in_sector["map_sectors_names"].append(element["name"])

    @staticmethod
    async def _coords_of_square_validation(jsom_params: dict):
        try:
            validate(jsom_params, get_coords_of_map_sectors_json)
        except ValidationError as e:
            await logger.info(
                f"Validation error on json, args: {e.args[0]}, json_params: {get_coords_of_map_sectors_json}")
            raise ValidationError

    @staticmethod
    async def _coords_of_square_with_categories_validation(json_params: dict):
        try:
            validate(json_params, get_categories_of_landmarks_json)
        except ValidationError as e:
            await logger.info(
                f"Validation error on json, args: {e.args[0]}, json_params: {get_categories_of_landmarks_json}")
            raise ValidationError

    @classmethod
    def get_landmarks_by_sectors_agent(cls):
        """
        Method to take landmarks by sectors agent object. Returns None in case when landmarks by sectors agent is not exists.
        :return: None | PURELandmarksBySectorsAgent
        """
        return cls._single_landmarks_agent

    @classmethod
    def landmarks_by_sectors_agent_exists(cls) -> bool:
        """Method to check if landmarks by sectors agent object already exists"""
        if cls._single_landmarks_agent:
            return True
        else:
            return False


# async def tescom():
#     test_class = GetLandmarksInSectorsAgent()
#     test_dict = {
#         "TL": {
#             "latitude": 56.232289,
#             "longitude": 23.690447875
#         },
#         "BR": {
#             "latitude": 53.113400874999996,
#             "longitude": 25.5222235
#         }
#     }
#     await test_class.landmarks_by_sectors_agent(test_dict)
#     await test_class.landmarks_by_sectors_agent(test_dict)
#
# task = asyncio.create_task(tescom())
# asyncio.run(tescom())
