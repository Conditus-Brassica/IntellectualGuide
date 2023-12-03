#Author: Vodohleb04
import asyncio
from typing import Dict, List
from neo4j import AsyncDriver
from backend.agents.crud_agent.pure_classes import PureCRUDAgent, PureReader


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

        # TODO Json parser

        return await asyncio.shield(session(json_params["region_name"], json_params["optional_limit"]))

    async def get_landmarks_in_map_sectors(self, json_params: Dict):
        async def session(sector_names: List[str], optional_limit: int = None):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_landmarks_in_map_sectors(session, sector_names, optional_limit)

        # TODO Json parser

        return await asyncio.shield(session(json_params["sector_names"], json_params["optional_limit"]))

    async def get_landmarks_refers_to_categories(self, json_params: Dict):
        async def session(sector_names: List[str], optional_limit: int = None):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_landmarks_refers_to_categories(session, sector_names, optional_limit)

        # TODO Json parser

        return await asyncio.shield(session(json_params["categories_names"], json_params["optional_limit"]))

    async def get_landmarks_by_coordinates(self, json_params: Dict):
        async def session(coordinates: List[Dict[str, float]], optional_limit: int = None):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_landmarks_by_coordinates(session, coordinates, optional_limit)

        # TODO Json parser

        return await asyncio.shield(session(json_params["coordinates"], json_params["optional_limit"]))

    async def get_landmarks_by_names(self, json_params: Dict):
        async def session(landmark_names: List[str], optional_limit: int = None):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_landmarks_by_names(session, landmark_names, optional_limit)

        # TODO Json parser

        return await asyncio.shield(session(json_params["landmark_names"], json_params["optional_limit"]))

    async def get_landmarks_of_categories_in_region(self, json_params: Dict):
        async def session(region_name: str, categories_names: List[str], optional_limit: int = None):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_landmarks_of_categories_in_region(
                    session, region_name, categories_names, optional_limit
                )

        # TODO Json parser

        return await asyncio.shield(
            session(json_params["region_name"], json_params["categories_names"], json_params["optional_limit"])
        )

    async def get_landmarks_by_region(self, json_params: Dict):
        async def session(region_name: str, optional_limit: int = None):
            async with self._kb_driver.session(database=self._knowledgebase_name) as session:
                return await self._reader.read_landmarks_by_region(session, region_name, optional_limit)

        # TODO Json parser

        return await asyncio.shield(session(json_params["region_name"], json_params["optional_limit"]))

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

        # TODO Json parser

        return await asyncio.shield(
            session(
                json_params["user_login"], json_params["current_latitude"], json_params["current_longitude"],
                json_params["current_name"], json_params["amount_of_recommendations"]
            )
        )


if __name__ == '__main__':
    from pprint import pprint
    from backend.agents.crud_agent.reader import Reader
    from neo4j import AsyncGraphDatabase

    async def test():

        async with AsyncGraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'ostisGovno')) as driver:
            reader = Reader()
            crud = CRUDAgent(reader, driver, 'neo4j')

            task1 = asyncio.create_task(crud.get_categories_of_region({"region_name": "Мядзельскі раён", "optional_limit": 3}))
            task2 = asyncio.create_task(crud.get_landmarks_in_map_sectors({"sector_names": ["a1", "a2"], "optional_limit": 3}))
            task3 = asyncio.create_task(crud.get_landmarks_refers_to_categories({"categories_names": ["озёра мядельского района", "национальные парки белоруссии"], "optional_limit": 3}))
            task4 = asyncio.create_task(crud.get_landmarks_by_coordinates({"coordinates": [{"longitude": 26.91887917, "latitude": 54.84001}, {"longitude": 26.8629, "latitude":54.955}, {"longitude":26.8684 , "latitude":54.9683}], "optional_limit": 3}))
            task5 = asyncio.create_task(crud.get_landmarks_by_names({"landmark_names": ["свирь", "рудаково", "нарочь"], "optional_limit": 3}))
            task6 = asyncio.create_task(crud.get_landmarks_of_categories_in_region({"region_name": "Мядзельскі раён", "categories_names": ["национальные парки белоруссии"], "optional_limit": 3}))
            task7 = asyncio.create_task(crud.get_landmarks_by_region({"region_name": "Мядзел", "optional_limit": 3}))
            task8 = asyncio.create_task(crud.get_recommendations_for_landmark_by_region(
                {"user_login": "user", "current_latitude": 54.8964, "current_longitude": 26.8922, "current_name": "рудаково (озеро)", "amount_of_recommendations": 10}
            ))

            pprint(await task1)
            pprint(await task2)
            pprint(await task3)
            pprint(await task4)
            pprint(await task5)
            pprint(await task6)
            pprint(await task7)
            pprint(await task8)

    asyncio.run(test())
