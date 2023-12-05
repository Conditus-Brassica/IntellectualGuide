#Author: Vodohleb04
import asyncio
from typing import Dict, List
from jsonschema import ValidationError, validate
from neo4j import AsyncDriver
from aiologger.loggers.json import JsonLogger
from backend.agents.crud_agent.pure_crud_classes import PureCRUDAgent, PureReader
from backend.agents.crud_agent.param_json_validation import *


logger = JsonLogger.with_default_handlers(
    level="DEBUG",
    serializer_kwargs={'ensure_ascii': False},
)


class CRUDAgent(PureCRUDAgent):

    def __init__(self, reader: PureReader, async_kb_driver: AsyncDriver, knowledgebase_name: str):
        """
        :param knowledgebase_name: name of knowledgebase to query
        """
        self._reader = reader
        self._kb_driver = async_kb_driver
        self._knowledgebase_name = knowledgebase_name

    async def get_categories_of_region(self, json_params: Dict):
        async def session(region_name: str, optional_limit: int = None):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_categories_of_region(session, region_name, optional_limit)

        try:
            validate(json_params, get_categories_of_region_json)
            json_params["optional_limit"] = json_params.get("optional_limit", None)
            return await asyncio.shield(session(json_params["region_name"], json_params["optional_limit"]))
        except ValidationError as ex:
            await logger.info(f"Validation error on json, args: {ex.args[0]}, json_params: {json_params}")
            raise ValidationError

    async def get_landmarks_in_map_sectors(self, json_params: Dict):
        async def session(map_sectors_names: List[str], optional_limit: int = None):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_landmarks_in_map_sectors(session, map_sectors_names, optional_limit)

        try:
            validate(json_params, get_landmarks_in_map_sectors_json)
            json_params["optional_limit"] = json_params.get("optional_limit", None)
            return await asyncio.shield(session(json_params["map_sectors_names"], json_params["optional_limit"]))
        except ValidationError as ex:
            await logger.info(f"get_landmarks_in_map_sectors. "
                              f"Validation error on json, args: {ex.args[0]}, json_params: {json_params}")
            raise ValidationError

    async def get_landmarks_refers_to_categories(self, json_params: Dict):
        async def session(map_sectors_names: List[str], optional_limit: int = None):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_landmarks_refers_to_categories(
                    session, map_sectors_names, optional_limit
                )

        try:
            validate(json_params, get_landmarks_refers_to_categories_json)
            json_params["optional_limit"] = json_params.get("optional_limit", None)
            return await asyncio.shield(session(json_params["categories_names"], json_params["optional_limit"]))
        except ValidationError as ex:
            await logger.info(f"get_landmarks_refers_to_categories. "
                              f"Validation error on json, args: {ex.args[0]}, json_params: {json_params}")
            raise ValidationError

    async def get_landmarks_by_coordinates(self, json_params: Dict):
        async def session(coordinates: List[Dict[str, float]], optional_limit: int = None):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_landmarks_by_coordinates(session, coordinates, optional_limit)

        try:
            validate(json_params, get_landmarks_by_coordinates_json)
            json_params["optional_limit"] = json_params.get("optional_limit", None)
            return await asyncio.shield(session(json_params["coordinates"], json_params["optional_limit"]))
        except ValidationError as ex:
            await logger.info(f"get_landmarks_by_coordinates. "
                              f"Validation error on json, args: {ex.args[0]}, json_params: {json_params}")
            raise ValidationError

    async def get_landmarks_by_names(self, json_params: Dict):
        async def session(landmark_names: List[str], optional_limit: int = None):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_landmarks_by_names(session, landmark_names, optional_limit)

        try:
            validate(json_params, get_landmarks_by_names_json)
            json_params["optional_limit"] = json_params.get("optional_limit", None)
            return await asyncio.shield(session(json_params["landmark_names"], json_params["optional_limit"]))
        except ValidationError as ex:
            await logger.info(f"get_landmarks_by_names. "
                              f"Validation error on json, args: {ex.args[0]}, json_params: {json_params}")
            raise ValidationError

    async def get_landmarks_of_categories_in_region(self, json_params: Dict):
        async def session(region_name: str, categories_names: List[str], optional_limit: int = None):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_landmarks_of_categories_in_region(
                    session, region_name, categories_names, optional_limit
                )

        try:
            validate(json_params, get_landmarks_of_categories_in_region_json)
            json_params["optional_limit"] = json_params.get("optional_limit", None)
            return await asyncio.shield(
                session(json_params["region_name"], json_params["categories_names"], json_params["optional_limit"])
            )
        except ValidationError as ex:
            await logger.info(f"get_landmarks_of_categories_in_region. "
                              f"Validation error on json, args: {ex.args[0]}, json_params: {json_params}")
            raise ValidationError

    async def get_landmarks_by_region(self, json_params: Dict):
        async def session(region_name: str, optional_limit: int = None):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_landmarks_by_region(session, region_name, optional_limit)

        try:
            validate(json_params, get_landmarks_by_region_json)
            json_params["optional_limit"] = json_params.get("optional_limit", None)
            return await asyncio.shield(session(json_params["region_name"], json_params["optional_limit"]))
        except ValidationError as ex:
            await logger.info(f"get_landmarks_by_region. "
                              f"Validation error on json, args: {ex.args[0]}, json_params: {json_params}")
            raise ValidationError

    async def get_recommendations_for_landmark_by_region(self, json_params: Dict):
        async def session(
                user_login: str,
                current_latitude: float,
                current_longitude: float,
                current_name: str,
                amount_of_recommendations: int
        ):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_recommendations_for_landmark_by_region(
                    session, user_login, current_latitude, current_longitude, current_name, amount_of_recommendations
                )

        try:
            validate(json_params, get_recommendations_for_landmark_by_region_json)
            return await asyncio.shield(
                session(
                    json_params["user_login"], json_params["current_latitude"], json_params["current_longitude"],
                    json_params["current_name"], json_params["amount_of_recommendations"]
                )
            )
        except ValidationError as ex:
            await logger.info(f"get_recommendations_for_landmark_by_region. "
                              f"Validation error on json, args: {ex.args[0]}, json_params: {json_params}")
            raise ValidationError

    async def get_map_sectors_of_points(self, json_params: Dict):
        async def session(coordinates_of_points: List[Dict[str, float]], optional_limit: int = None):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_map_sectors_of_points(session, coordinates_of_points, optional_limit)

        try:
            # TODO validate(json_params, get_landmarks_by_region_json)
            json_params["optional_limit"] = json_params.get("optional_limit", None)
            return await asyncio.shield(session(json_params["coordinates_of_points"], json_params["optional_limit"]))
        except ValidationError as ex:
            await logger.info(f"get_map_sectors_of_points. "
                              f"Validation error on json, args: {ex.args[0]}, json_params: {json_params}")

    async def get_landmarks_of_categories_in_map_sectors(self, json_params: Dict):
        async def session(map_sectors_names: List[str], categories_names: List[str], optional_limit: int = None):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_landmarks_of_categories_in_map_sectors(
                    session, map_sectors_names, categories_names, optional_limit
                )

        try:
            # TODO validate(json_params, get_landmarks_by_region_json)
            json_params["optional_limit"] = json_params.get("optional_limit", None)
            return await asyncio.shield(
                session(
                    json_params["map_sectors_names"], json_params["categories_names"], json_params["optional_limit"]
                )
            )
        except ValidationError as ex:
            await logger.info(f"get_landmarks_of_categories_in_map_sectors. "
                              f"Validation error on json, args: {ex.args[0]}, json_params: {json_params}")

    async def get_recommendations_by_coordinates_and_categories(self, json_params: Dict):
        async def session(
                coordinates_of_points: List[Dict[str, float]],
                categories_names: List[str],
                user_login: str,
                amount_of_recommendations: int
        ):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_recommendations_by_coordinates_and_categories(
                    session, coordinates_of_points, categories_names, user_login, amount_of_recommendations
                )

        try:
            # TODO validate(json_params, get_recommendations_for_landmark_by_region_json)
            return await asyncio.shield(
                session(
                    json_params["coordinates_of_points"], json_params["categories_names"], json_params["user_login"],
                    json_params["amount_of_recommendations"]
                )
            )
        except ValidationError as ex:
            await logger.info(f"get_recommendations_by_coordinates_and_categories. "
                              f"Validation error on json, args: {ex.args[0]}, json_params: {json_params}")
            raise ValidationError
