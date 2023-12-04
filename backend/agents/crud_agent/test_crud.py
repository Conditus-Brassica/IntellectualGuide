import asyncio
from crud_commands import *
from pprint import pprint
from backend.agents.crud_agent.reader import Reader
from neo4j import AsyncGraphDatabase
from crud_agent import CRUDAgent


if __name__ == '__main__':

    async def test():

        async with AsyncGraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'ostisGovno')) as driver:
            reader = Reader()
            crud = CRUDAgent(reader, driver, 'neo4j')

            command1 = CategoriesOfRegionCommand(crud, {"region_name": "Мядзельскі раён"})
            command2 = LandmarksInMapSectorsCommand(crud, {"sector_names": ["a1", "a2"], "optional_limit": 3})
            command3 = LandmarksRefersToCategoriesCommand(crud, {"categories_names": ["озёра мядельского района", "национальные парки белоруссии"], "optional_limit": 3})
            command4 = LandmarksByCoordinatesCommand(crud, {"coordinates": [{"longitude": 26.91887917, "latitude": 54.84001}, {"longitude": 26.8629, "latitude":54.955}, {"longitude":26.8684 , "latitude":54.9683}], "optional_limit": 3})
            command5 = LandmarksByNamesCommand(crud, {"landmark_names": ["свирь", "рудаково", "нарочь"], "optional_limit": 3})
            command6 = LandmarksOfCategoriesInRegionCommand(crud, {"region_name": "Мядзельскі раён", "categories_names": ["национальные парки белоруссии"]})
            command7 = LandmarksByRegionCommand(crud, {"region_name": "Мядзел", "optional_limit": 3})
            command8 = RecommendationsForLandmarkByRegionCommand(crud, {"user_login": "user", "current_latitude": 54.8964, "current_longitude": 26.8922, "current_name": "рудаково (озеро)", "amount_of_recommendations": 10})

            task1 = asyncio.create_task(command1.execute())
            task2 = asyncio.create_task(command2.execute())
            task3 = asyncio.create_task(command3.execute())
            task4 = asyncio.create_task(command4.execute())
            task5 = asyncio.create_task(command5.execute())
            task6 = asyncio.create_task(command6.execute())
            task7 = asyncio.create_task(command7.execute())
            task8 = asyncio.create_task(command8.execute())

            pprint(await task1)
            pprint(await task2)
            pprint(await task3)
            pprint(await task4)
            pprint(await task5)
            pprint(await task6)
            pprint(await task7)
            pprint(await task8)

    asyncio.run(test())
