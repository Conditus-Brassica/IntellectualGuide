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


class GetLandmarksInSector(Sender):
    LAT_DIFFERENCE = 0.312
    LONG_DIFFERENCE = 0.611

    def __init__(self, Agent: PureCRUDAgent):
        self.crud = Agent
        self.cache = {}

    async def get_landmarks(self, coords_of_square: dict):
        # Check if format of dictionary is right using validator
        try:
            validate(coords_of_square, get_coords_of_map_sectors_json)
        except ValidationError as e:
            await logger.info(
                f"Validation error on json, args: {e.args[0]}, json_params: {get_coords_of_map_sectors_json}")
            raise ValidationError

        sectors_in_view = {}
        # Cash
        if len(self.cache) != 0:
            for element in self.cache:
                if (element["TL"]["longitude"] <= coords_of_square["TL"]["longitude"] < coords_of_square["BR"]["longitude"] <=
                        element["BR"]["longitude"]) and (
                        element["BR"]["latitude"] <= coords_of_square["BR"]["latitude"] < coords_of_square["TL"]["latitude"] <=
                        element["TL"]["latitude"]):  # Cash using, first occurrence: when new square fully in the old square
                    sectors_in_view = self.cache
                elif (self.cache is None):  # Еще один вид кэша, при котором новый квадрат частично совпадает со старым
                    sectors_in_view = None
        else:  # No cash at all
            sectors_in_view = self.__get_squares_in_sector(coords_of_square)
        result = await self.send_command(CRUDCommandsFabric.create_landmarks_in_map_sectors_command(self.crud, sectors_in_view))
        return result

    async def send_command(self, command: BaseCommand):
        await command.execute()

    def __get_squares_in_sector(self, coords_of_square: dict):
        sectors_in_view = {"sector_names": []}
        data = json.load(open("new_squares.json"))
        for element in data:
            if (coords_of_square["TL"]["longitude"] - self.LONG_DIFFERENCE <= element["TL"]["longitude"] <
                element["BR"]["longitude"] <=
                coords_of_square["BR"]["longitude"] + self.LONG_DIFFERENCE) and (
                    coords_of_square["BR"]["latitude"] - self.LAT_DIFFERENCE <= element["BR"]["latitude"] <
                    element["TL"]["latitude"] <=
                    coords_of_square["TL"]["latitude"] + self.LAT_DIFFERENCE):
                sectors_in_view["sector_names"].append(element["name"])
        self.cache = sectors_in_view
        return sectors_in_view


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
