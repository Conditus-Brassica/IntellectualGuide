# import asyncio
import json
from aiologger.loggers.json import JsonLogger
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from backend.agents import PureCRUDAgent, CRUDCommandsFabric
from backend.agents.get_landmarks_in_sector.get_landmarks_commands_fabric import GetLandmarksInSectorCommandsFabric
from backend.agents.get_landmarks_in_sector.squares_params_json_validation import *
from backend.command_bases import Sender, BaseCommand

logger = JsonLogger.with_default_handlers(
    level="DEBUG",
    serializer_kwargs={'ensure_ascii': False},
)


class GetLandmarksInSectors(Sender):
    LAT_DIFFERENCE = 0.312
    LONG_DIFFERENCE = 0.611

    def __init__(self, Agent: PureCRUDAgent):
        self.squares_in_sector = {"sector_names": [], "map_sector_names": []}
        self.crud = Agent
        self.cache = {}
        self.result = {}
        self.full_cache = {}

    async def get_landmarks_in_sector(self, coords_of_square: dict):
        # Check if format of dictionary is right using validator
        await self.__validation(coords_of_square)

        self.__get_sectors_of_map(coords_of_square)
        self.squares_in_sector.pop("map_sectors_names")
        if not self.full_cache:
            self.result = await self.send_command(GetLandmarksInSectorCommandsFabric.create_landmarks_in_map_sectors_command(self.crud,
                                                                            self.squares_in_sector))
        return self.result


    async def get_landmarks_by_categories_in_sector(self, coords_of_square: dict, categories: list[str]):
        await self.__validation(coords_of_square)

        self.__get_sectors_of_map(coords_of_square)
        self.squares_in_sector.pop("sector_names")
        self.squares_in_sector["categories_names"] = categories
        if not self.full_cache:
            self.result = await self.send_command(
                GetLandmarksInSectorCommandsFabric.create_landmarks_of_categories_in_map_sectors_command(self.crud, self.squares_in_sector))
        return self.result

    async def send_command(self, command: BaseCommand):
        await command.execute()

    def __get_sectors_of_map(self, coords_of_square: dict):
        # Cash
        if len(self.cache) != 0:
            if (self.cache["TL"]["longitude"] <= coords_of_square["TL"]["longitude"] < coords_of_square["BR"]["longitude"] <=
                self.cache["BR"]["longitude"]) and (
                    self.cache["BR"]["latitude"] <= coords_of_square["BR"]["latitude"] < coords_of_square["TL"]["latitude"] <=
                    self.cache["TL"]["latitude"]):  # Cash using, first occurrence: when new square fully in the old square
                self.full_cache = True
            else:
                coords_of_squares = self.__partial_cash_handling(coords_of_square)
                for element in coords_of_squares:
                    self.__get_squares_in_sector(element)
        else:  # No cash at all
            self.__get_squares_in_sector(coords_of_square)

    def __get_squares_in_sector(self, coords_of_square: dict):
        data = json.load(open("new_squares.json"))
        for element in data:
            if (coords_of_square["TL"]["longitude"] - self.LONG_DIFFERENCE <= element["TL"]["longitude"] <
                element["BR"]["longitude"] <=
                coords_of_square["BR"]["longitude"] + self.LONG_DIFFERENCE) and (
                    coords_of_square["BR"]["latitude"] - self.LAT_DIFFERENCE <= element["BR"]["latitude"] <
                    element["TL"]["latitude"] <=
                    coords_of_square["TL"]["latitude"] + self.LAT_DIFFERENCE):
                self.squares_in_sector["map_sectors_names"].append(element["name"])
                self.squares_in_sector["sector_names"].append(element["name"])
        self.cache = coords_of_square

    # Еще один вид кэша, при котором новый квадрат частично совпадает со старым
    # Uncomplete
    def __partial_cash_handling(self, coords_of_square: dict) -> list:
        tick = 0
        test_coords = []
        if self.cache["TL"]["longitude"] <= coords_of_square["TL"]["longitude"]:
            tick += 1
            pass
        if coords_of_square["BR"]["longitude"] <= self.cache["BR"]["longitude"]:
            pass
        if self.cache["BR"]["latitude"] <= coords_of_square["BR"]["latitude"]:
            pass
        if coords_of_square["TL"]["latitude"] <= self.cache["TL"]["latitude"]:
            pass
        if tick == 0:
            return [coords_of_square]

    async def __validation(self, coords_of_square: dict):
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
