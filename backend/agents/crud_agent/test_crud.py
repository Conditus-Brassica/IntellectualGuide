import asyncio
import json
from crud_commands import *
from pprint import pprint
from backend.agents.crud_agent.reader import Reader
from neo4j import AsyncGraphDatabase
from crud_agent import CRUDAgent
from backend.agents.crud_agent.crud_commands_fabric import CRUDCommandsFabric
from backend.broker import *


if __name__ == '__main__':

    #async def test(login, password):
    async def test():
        #async with AsyncGraphDatabase.driver('bolt://localhost:7687', auth=(login, password)) as driver:
        #    reader = Reader()
        #    crud = CRUDAgent(reader, driver, 'neo4j')

            # command1 = CRUDCommandsFabric.create_categories_of_region_command(
            #     crud, {"region_name": "Мядзельскі раён"}
            # )
            # command2 = CRUDCommandsFabric.create_landmarks_in_map_sectors_command(
            #     crud, {"map_sectors_names": ["a1", "a2", "g2"], "optional_limit": 3}
            # )
            # command3 = CRUDCommandsFabric.create_landmarks_refers_to_categories_command(
            #     crud,
            #     {"categories_names": ["озёра мядельского района", "национальные парки белоруссии"], "optional_limit": 3}
            # )
            # command4 = CRUDCommandsFabric.create_landmarks_by_coordinates_command(
            #     crud,
            #     {"coordinates": [{"longitude": 26.91887917, "latitude": 54.84001}, {"longitude": 26.8629, "latitude":54.955}, {"longitude":26.8684 , "latitude":54.9683}], "optional_limit": 3}
            # )
            # command5 = CRUDCommandsFabric.create_landmarks_by_names_command(
            #     crud,
            #     {"landmark_names": ["свирь", "рудаково", "нарочь"], "optional_limit": 3}
            # )
            # command6 = CRUDCommandsFabric.create_landmarks_of_categories_in_region_command(
            #     crud,
            #     {"region_name": "Мядзельскі раён", "categories_names": ["национальные парки белоруссии"]}
            # )
            # command7 = CRUDCommandsFabric.create_landmarks_by_region_command(
            #     crud, {"region_name": "Мядзел", "optional_limit": 3}
            # )
            # command8 = CRUDCommandsFabric.create_recommendations_for_landmark_by_region_command(
            #     crud,
            #     {"user_login": "user", "current_latitude": 54.8964, "current_longitude": 26.8922, "current_name": "рудаково (озеро)", "amount_of_recommendations": 10}
            # )
            # command9 = CRUDCommandsFabric.create_map_sectors_of_points_command(
            #     crud,
            #     {"coordinates_of_points": [{"latitude": 55.7,"longitude": 26.7}, {"latitude":55.61639,"longitude":26.70833}, {"latitude":55.39417,"longitude":26.62722}], "optional_limit": 1}
            # )
            # command10 = CRUDCommandsFabric.create_landmarks_of_categories_in_map_sectors_command(
            #     crud,
            #     {"map_sectors_names": ["a8", "h4"], "categories_names": ["историко-культурные ценности республики беларусь", "заказники белоруссии", "озёра поставского района"], "optional_limit": 1}
            # )
            # command11 = CRUDCommandsFabric.create_recommendations_by_coordinates_and_categories_command(
            #     crud,
            #     {
            #         "coordinates_of_points": [
            #             {
            #                 "latitude": 55.19861,
            #                 "longitude": 27.41694
            #             },
            #             {
            #                 "latitude": 54.1275,
            #                 "longitude": 25.36306
            #             }
            #         ],
            #         "categories_names": ["озёра поставского района"],
            #         # ["историко-культурные ценности республики беларусь", "озёра поставского района"],
            #         "user_login": "user",
            #         "amount_of_recommendations_for_point": 3,
            #         "optional_limit": 6
            #     }
            # )
            # command11_2 = CRUDCommandsFabric.create_recommendations_by_coordinates_and_categories_command(
            #     crud, {
            #         "coordinates_of_points": [
            #             {
            #                 "latitude": 55.19861,
            #                 "longitude": 27.41694
            #             },
            #             {
            #                 "latitude": 54.1275,
            #                 "longitude": 25.36306
            #             }
            #         ],
            #         "categories_names": ["озёра поставского района"],
            #         # ["историко-культурные ценности республики беларусь", "озёра поставского района"],
            #         "user_login": "user",
            #         "amount_of_recommendations_for_point": 3,
            #         "optional_limit": 6
            #     }
            # )
            # task11 = asyncio.create_task(command11.execute())
            # task12 = asyncio.create_task(command11_2.execute())
            #
            # task1 = asyncio.create_task(command1.execute())
            # task2 = asyncio.create_task(command2.execute())
            # task3 = asyncio.create_task(command3.execute())
            # task4 = asyncio.create_task(command4.execute())
            # task5 = asyncio.create_task(command5.execute())
            # task6 = asyncio.create_task(command6.execute())
            # task7 = asyncio.create_task(command7.execute())
            # task8 = asyncio.create_task(command8.execute())
            # task9 = asyncio.create_task(command9.execute())
            # task10 = asyncio.create_task(command10.execute())

        await BROKER.startup()

        task_result1 = asyncio.create_task(BROKER.call_agent_task(categories_of_region_task, {"region_name": "Мядзельскі раён"}))
        task_result2 = asyncio.create_task(BROKER.call_agent_task(landmarks_in_map_sectors_task,
                                                    {"map_sectors_names": ["a1", "a2", "g2"], "optional_limit": 3}))
        task_result3 = asyncio.create_task(BROKER.call_agent_task(landmarks_refers_to_categories_task, {
            "categories_names": ["озёра мядельского района", "национальные парки белоруссии"], "optional_limit": 3}))
        task_result4 = asyncio.create_task(BROKER.call_agent_task(landmarks_by_coordinates_task, {
            "coordinates": [{"longitude": 26.91887917, "latitude": 54.84001},
                            {"longitude": 26.8629, "latitude": 54.955}, {"longitude": 26.8684, "latitude": 54.9683}],
            "optional_limit": 3}))
        task_result5 = asyncio.create_task(BROKER.call_agent_task(landmarks_by_names_task,
                                                    {"landmark_names": ["свирь", "рудаково", "нарочь"],
                                                     "optional_limit": 3}))
        task_result6 = asyncio.create_task(BROKER.call_agent_task(landmarks_of_categories_in_region_task,
                                                    {"region_name": "Мядзельскі раён",
                                                     "categories_names": ["национальные парки белоруссии"]}))
        task_result7 = asyncio.create_task(BROKER.call_agent_task(landmarks_by_region_task,
                                                    {"region_name": "Мядзел", "optional_limit": 3}))
        task_result8 = asyncio.create_task(BROKER.call_agent_task(recommendations_for_landmark_by_region_task,
                                                    {"user_login": "user", "current_latitude": 54.8964,
                                                     "current_longitude": 26.8922, "current_name": "рудаково (озеро)",
                                                     "amount_of_recommendations": 10}))
        task_result9 = asyncio.create_task(BROKER.call_agent_task(map_sectors_of_points_task, {
            "coordinates_of_points": [{"latitude": 55.7, "longitude": 26.7},
                                      {"latitude": 55.61639, "longitude": 26.70833},
                                      {"latitude": 55.39417, "longitude": 26.62722}], "optional_limit": 1}))
        task_result10 = asyncio.create_task(BROKER.call_agent_task(landmarks_of_categories_in_map_sectors_task,
                                                     {"map_sectors_names": ["a8", "h4"], "categories_names": [
                                                         "историко-культурные ценности республики беларусь",
                                                         "заказники белоруссии", "озёра поставского района"],
                                                      "optional_limit": 1}))
        task_result11 = asyncio.create_task(BROKER.call_agent_task(
            recommendations_by_coordinates_and_categories_task,
            {
                "coordinates_of_points": [
                    {
                        "latitude": 55.19861,
                        "longitude": 27.41694
                    },
                    {
                        "latitude": 54.1275,
                        "longitude": 25.36306
                    }
                ],
                "categories_names": ["озёра поставского района"],
                # ["историко-культурные ценности республики беларусь", "озёра поставского района"],
                "user_login": "user",
                "amount_of_recommendations_for_point": 3,
                "optional_limit": 6
            }
        ))
        task_result11_2 = asyncio.create_task(BROKER.call_agent_task(
            recommendations_by_coordinates_and_categories_task,
            {
                "coordinates_of_points": [
                    {
                        "latitude": 55.19861,
                        "longitude": 27.41694
                    },
                    {
                        "latitude": 54.1275,
                        "longitude": 25.36306
                    }
                ],
                "categories_names": ["озёра поставского района"],
                # ["историко-культурные ценности республики беларусь", "озёра поставского района"],
                "user_login": "user",
                "amount_of_recommendations_for_point": 3,
                "optional_limit": 6
            }
        ))

        res1 = await task_result1
        res2 = await task_result2
        res3 = await task_result3
        res4 = await task_result4
        res5 = await task_result5
        res6 = await task_result6
        res7 = await task_result7
        res8 = await task_result8
        res9 = await task_result9
        res10 = await task_result10
        res11 = await task_result11
        res11_2 = await task_result11_2


        # task_result1 = await BROKER.call_agent_task(categories_of_region_task, {"region_name": "Мядзельскі раён"})
        # task_result2 = await BROKER.call_agent_task(landmarks_in_map_sectors_task, {"map_sectors_names": ["a1", "a2", "g2"], "optional_limit": 3})
        # task_result3 = await BROKER.call_agent_task(landmarks_refers_to_categories_task, {"categories_names": ["озёра мядельского района", "национальные парки белоруссии"], "optional_limit": 3})
        # task_result4 = await BROKER.call_agent_task(landmarks_by_coordinates_task, {"coordinates": [{"longitude": 26.91887917, "latitude": 54.84001}, {"longitude": 26.8629, "latitude":54.955}, {"longitude":26.8684 , "latitude":54.9683}], "optional_limit": 3})
        # task_result5 = await BROKER.call_agent_task(landmarks_by_names_task, {"landmark_names": ["свирь", "рудаково", "нарочь"], "optional_limit": 3})
        # task_result6 = await BROKER.call_agent_task(landmarks_of_categories_in_region_task, {"region_name": "Мядзельскі раён", "categories_names": ["национальные парки белоруссии"]})
        # task_result7 = await BROKER.call_agent_task(landmarks_by_region_task, {"region_name": "Мядзел", "optional_limit": 3})
        # task_result8 = await BROKER.call_agent_task(recommendations_for_landmark_by_region_task, {"user_login": "user", "current_latitude": 54.8964, "current_longitude": 26.8922, "current_name": "рудаково (озеро)", "amount_of_recommendations": 10})
        # task_result9 = await BROKER.call_agent_task(map_sectors_of_points_task, {"coordinates_of_points": [{"latitude": 55.7,"longitude": 26.7}, {"latitude":55.61639,"longitude":26.70833}, {"latitude":55.39417,"longitude":26.62722}], "optional_limit": 1})
        # task_result10 = await BROKER.call_agent_task(landmarks_of_categories_in_map_sectors_task, {"map_sectors_names": ["a8", "h4"], "categories_names": ["историко-культурные ценности республики беларусь", "заказники белоруссии", "озёра поставского района"], "optional_limit": 1})
        # task_result11 = await BROKER.call_agent_task(
        #     recommendations_by_coordinates_and_categories_task,
        #     {
        #         "coordinates_of_points": [
        #             {
        #                 "latitude": 55.19861,
        #                 "longitude": 27.41694
        #             },
        #             {
        #                 "latitude": 54.1275,
        #                 "longitude": 25.36306
        #             }
        #         ],
        #         "categories_names": ["озёра поставского района"],
        #         # ["историко-культурные ценности республики беларусь", "озёра поставского района"],
        #         "user_login": "user",
        #         "amount_of_recommendations_for_point": 3,
        #         "optional_limit": 6
        #     }
        # )
        # task_result11_2 = await BROKER.call_agent_task(
        #     recommendations_by_coordinates_and_categories_task,
        #     {
        #         "coordinates_of_points": [
        #             {
        #                 "latitude": 55.19861,
        #                 "longitude": 27.41694
        #             },
        #             {
        #                 "latitude": 54.1275,
        #                 "longitude": 25.36306
        #             }
        #         ],
        #         "categories_names": ["озёра поставского района"],
        #         # ["историко-культурные ценности республики беларусь", "озёра поставского района"],
        #         "user_login": "user",
        #         "amount_of_recommendations_for_point": 3,
        #         "optional_limit": 6
        #     }
        # )
        # pprint(task_result11.return_value)
        # pprint(task_result11_2.return_value)
        #
        # pprint(task_result1.return_value)
        # pprint(task_result2.return_value)
        # pprint(task_result3.return_value)
        # pprint(task_result4.return_value)
        # pprint(task_result5.return_value)
        # pprint(task_result6.return_value)
        # pprint(task_result7.return_value)
        # pprint(task_result8.return_value)
        # pprint(task_result9.return_value)
        # pprint(task_result10.return_value)

        pprint(res11.return_value)
        pprint(res11_2.return_value)

        pprint(res1.return_value)
        pprint(res2.return_value)
        pprint(res3.return_value)
        pprint(res4.return_value)
        pprint(res5.return_value)
        pprint(res6.return_value)
        pprint(res7.return_value)
        pprint(res8.return_value)
        pprint(res9.return_value)
        pprint(res10.return_value)

        await BROKER.shutdown()


    # with open("basic_login.json", 'r') as fout:
    #     basic_login = json.load(fout)
    #


    asyncio.run(test())
    #asyncio.run(test(basic_login["login"], basic_login["password"]))
