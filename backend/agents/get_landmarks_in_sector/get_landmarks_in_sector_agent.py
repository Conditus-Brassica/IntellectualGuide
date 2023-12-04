import json
from abc import ABC, abstractmethod
from typing import Dict

from aiologger.loggers.json import JsonLogger
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from backend.agents.crud_agent.crud_commands_fabric import CRUDCommandsFabric
from backend.agents import PureCRUDAgent
from backend.agents.get_landmarks_in_sector.squares_params_json_validation import *
from backend.command_bases import Sender, BaseCommand

from backend.agents.crud_agent import crud_agent

logger = JsonLogger.with_default_handlers(
    level="DEBUG",
    serializer_kwargs={'ensure_ascii': False},
)


class GetLandmarksInSector(Sender):
    LAT_DIFFERENCE = 0.31188881249999
    LONG_DIFFERENCE = 0.610591875

    def __init__(self, Agent: PureCRUDAgent):
        self.crud = Agent
        self.sectors_in_view = {}
        self.cache = {}

    async def get_landmarks(self, coords_of_square: dict):
        # Check if format of dictionary is right using validator
        try:
            validate(coords_of_square, get_coords_of_map_sectors_json)
        except ValidationError as e:
            await logger.info(
                f"Validation error on json, args: {e.args[0]}, json_params: {get_coords_of_map_sectors_json}")
            raise ValidationError

        if self.cache is not None:
            if (self.cache["TL"]["longitude"] <= coords_of_square["TL"]["longitude"] < coords_of_square["BR"]["longitude"] <=
                self.cache["BR"]["longitude"] + self.LONG_DIFFERENCE) and (
                    self.cache["BR"]["latitude"] <= coords_of_square["BR"]["latitude"] < coords_of_square["TL"]["latitude"] <=
                    self.cache["TL"]["latitude"]):  # Использование кэша, первый случай: когда новый квадрат полностью находится внутри старого
                pass
            elif (self.cache is None):  # Еще один вид кэша, при котором новый квадрат частично совпадает со старым
                pass
        else:  # Кэш задействовать невозможно
            self.sectors_in_view = {}
            self.get_squares_in_sector(coords_of_square)

        await self.send_command(CRUDCommandsFabric.create_landmarks_in_map_sectors_command(self.crud, self.sectors_in_view))

    async def send_command(self, command: BaseCommand):
        await command.execute()

    def get_squares_in_sector(self, coords_of_square: dict):
        data = json.load(open("new_squares.json"))
        for element in data:
            if (coords_of_square["TL"]["longitude"] - self.LONG_DIFFERENCE <= element["TL"]["longitude"] <
                element["BR"]["longitude"] <=
                coords_of_square["BR"]["longitude"] + self.LONG_DIFFERENCE) and (
                    coords_of_square["BR"]["latitude"] - self.LAT_DIFFERENCE <= element["BR"]["latitude"] <
                    element["TL"]["latitude"] <=
                    coords_of_square["TL"]["latitude"] + self.LAT_DIFFERENCE):
                self.sectors_in_view["sector_names"].append(element["name"])
