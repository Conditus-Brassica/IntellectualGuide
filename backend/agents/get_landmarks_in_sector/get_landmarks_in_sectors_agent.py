# import asyncio
import json
from aiologger.loggers.json import JsonLogger
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from backend.agents import PureCRUDAgent, CRUDCommandsFabric
from backend.agents.get_landmarks_in_sector.squares_params_json_validation import *
from backend.command_bases import Sender, BaseCommand

logger = JsonLogger.with_default_handlers(
    level="DEBUG",
    serializer_kwargs={'ensure_ascii': False},
)


class GetLandmarksInSectorsAgent(Sender):
    LAT_DIFFERENCE = 0.312
    LONG_DIFFERENCE = 0.611

    def __init__(self, ):
        self.squares_in_sector = {"map_sector_names": []}
        self.cache = {}
        self.result = {}
        self.full_cache = False

    async def get_landmarks_in_sector(self, coords_of_square: dict, agent: PureCRUDAgent):
        # Check if format of dictionary is right using validator
        await self.__coords_of_square_validation(coords_of_square)
        self.__get_sectors_in_sector(coords_of_square)
        # Comparing with cache, then updating of cache
        self.squares_in_sector[0] = [i for i in self.squares_in_sector[0] not in self.cache[0]]
        self.cache["map_sector_names"].append(self.squares_in_sector[0])
        if not self.full_cache:
            self.result = await self.send_command(
                CRUDCommandsFabric.create_landmarks_in_map_sectors_command(agent, self.squares_in_sector))
        return self.result

    async def get_landmarks_by_categories_in_sector(self, coords_of_square: dict, categories: dict,
                                                    agent: PureCRUDAgent):
        await self.__categories_validation(categories)
        await self.__coords_of_square_validation(coords_of_square)
        self.__get_sectors_in_sector(coords_of_square)
        self.squares_in_sector[0] = [i for i in self.squares_in_sector[0] not in self.cache[0]]
        self.cache["map_sector_names"].append(self.squares_in_sector[0])
        self.squares_in_sector.update(categories)

        self.cache = self.squares_in_sector
        if not self.full_cache:
            self.result = await self.send_command(
                CRUDCommandsFabric.create_landmarks_of_categories_in_map_sectors_command(agent, self.squares_in_sector))
        return self.result

    async def send_command(self, command: BaseCommand):
        await command.execute()


    def __get_sectors_in_sector(self, coords_of_square: dict):
        data = json.load(open("new_squares.json"))
        for element in data:
            if (coords_of_square["TL"]["longitude"] - self.LONG_DIFFERENCE <= element["TL"]["longitude"] <
                element["BR"]["longitude"] <=
                coords_of_square["BR"]["longitude"] + self.LONG_DIFFERENCE) and (
                    coords_of_square["BR"]["latitude"] - self.LAT_DIFFERENCE <= element["BR"]["latitude"] <
                    element["TL"]["latitude"] <=
                    coords_of_square["TL"]["latitude"] + self.LAT_DIFFERENCE):
                self.squares_in_sector["map_sectors_names"].append(element["name"])


    async def __categories_validation(self, categories: dict):
        try:
            validate(categories, get_categories_of_landmarks_json)
        except ValidationError as e:
            await logger.info(
                f"Validation error on json, args: {e.args[0]}, json_params: {get_categories_of_landmarks_json}")
            raise ValidationError

    async def __coords_of_square_validation(self, coords_of_square: dict):
        try:
            validate(coords_of_square, get_coords_of_map_sectors_json)
        except ValidationError as e:
            await logger.info(
                f"Validation error on json, args: {e.args[0]}, json_params: {get_coords_of_map_sectors_json}")
            raise ValidationError

        self.__get_sectors_of_map(coords_of_square)

# async def tescom():
#     test_class = GetLandmarksInSector()
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
#     await test_class.get_landmarks(test_dict)
#
# task = asyncio.create_task(tescom())
# asyncio.run(tescom())
