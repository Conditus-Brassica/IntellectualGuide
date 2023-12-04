import asyncio
from crud_commands import *
from pprint import pprint
from backend.agents.crud_agent.reader import Reader
from neo4j import AsyncGraphDatabase
from crud_agent import CRUDAgent
from backend.agents.crud_agent.crud_commands_fabric import CRUDCommandsFabric



if __name__ == '__main__':

    async def test():

        async with AsyncGraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'ostisGovno')) as driver:
            reader = Reader()
            crud = CRUDAgent(reader, driver, 'neo4j')



            command1 = CRUDCommandsFabric.create_categories_of_region_command(crud, {"region_name": "Мядзельскі раён"})
            command2 = CRUDCommandsFabric.create_landmarks_in_map_sectors_command(crud, {"sector_names": ["a1", "a2"], "optional_limit": 3})
            command3 = CRUDCommandsFabric.create_landmarks_refers_to_categories_command(crud, {"categories_names": ["озёра мядельского района", "национальные парки белоруссии"], "optional_limit": 3})
            command4 = CRUDCommandsFabric.create_landmarks_by_coordinates_command(crud, {"coordinates": [{"longitude": 26.91887917, "latitude": 54.84001}, {"longitude": 26.8629, "latitude":54.955}, {"longitude":26.8684 , "latitude":54.9683}], "optional_limit": 3})
            command5 = CRUDCommandsFabric.create_landmarks_by_names_command(crud, {"landmark_names": ["свирь", "рудаково", "нарочь"], "optional_limit": 3})
            command6 = CRUDCommandsFabric.create_landmarks_of_categories_in_region_command(crud, {"region_name": "Мядзельскі раён", "categories_names": ["национальные парки белоруссии"]})
            command7 = CRUDCommandsFabric.create_landmarks_by_region_command(crud, {"region_name": "Мядзел", "optional_limit": 3})
            command8 = CRUDCommandsFabric.create_recommendations_for_landmark_by_region_command(crud, {"user_login": "user", "current_latitude": 54.8964, "current_longitude": 26.8922, "current_name": "рудаково (озеро)", "amount_of_recommendations": 10})
            command9 = CRUDCommandsFabric.create_map_sectors_of_points_command(crud, {
                "coordinates_of_points": [{"latitude": 55.7,"longitude": 26.7}, {"latitude":55.61639,"longitude":26.70833}, {"latitude":55.39417,"longitude":26.62722}]
            })
            command10 = CRUDCommandsFabric.create_landmarks_of_categories_in_map_sectors_command(
                crud, {"map_sectors_names": ["a8", "h4"], "categories_names": ["историко-культурные ценности республики беларусь", "заказники белоруссии", "озёра поставского района"]}
            )

            task1 = asyncio.create_task(command1.execute())
            task2 = asyncio.create_task(command2.execute())
            task3 = asyncio.create_task(command3.execute())
            task4 = asyncio.create_task(command4.execute())
            task5 = asyncio.create_task(command5.execute())
            task6 = asyncio.create_task(command6.execute())
            task7 = asyncio.create_task(command7.execute())
            task8 = asyncio.create_task(command8.execute())
            task9 = asyncio.create_task(command9.execute())
            task10 = asyncio.create_task(command10.execute())

            pprint(await task1)
            pprint(await task2)
            pprint(await task3)
            pprint(await task4)
            pprint(await task5)
            pprint(await task6)
            pprint(await task7)
            pprint(await task8)
            pprint(await task9)
            pprint(await task10)

    asyncio.run(test())
