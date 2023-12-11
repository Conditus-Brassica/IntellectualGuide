import asyncio
from pprint import pprint

from backend.broker.abstract_agents_broker import AbstractAgentsBroker
from backend.broker.agents_tasks.route_builder_task import build_route


async def main():
    param = {
        "categories_names": ['Музеи Витебской области', "Категория:Театры Бреста", 'Скверы Белоруссии'],
        "coordinates": [{"latitude":  53.871045, "longitude":  30.299173}, {"latitude": 52.63047029088026, "longitude": 29.731127278387117}],
        "user_login": "",
        "start_end_points": {"coordinates": [{
            "latitude": 53.13069674685768,
            "longitude": 25.967160840243956
        },
            {
                "latitude": 53.871045,
                "longitude": 30.299173
            }]}
    }

    task = asyncio.create_task(AbstractAgentsBroker.call_agent_task(
        build_route, param
    ))

    res = await task
    res2 = res.return_value

    pprint(res2[1])


asyncio.run(main())
