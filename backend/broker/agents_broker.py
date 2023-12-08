#import json
from typing import Dict
from taskiq_redis import ListQueueBroker, RedisAsyncResultBackend
from backend.agents.crud_agent import CRUDAgent, Reader
from neo4j import AsyncGraphDatabase


class AgentsBroker(ListQueueBroker):
    def __init__(self, crud: CRUDAgent, *args, **kwargs):
        self.crud = crud
        super().__init__(*args, **kwargs)

    async def shutdown(self) -> None:
        await self.crud.close()
        await super().shutdown()

    @staticmethod
    async def call_agent_task(agent_task, json_params: Dict):
        """
        Wrapper to call task using broker. Call tasks only using this method.
        Works asynchronously.

        :param agent_task: task to call (check broker/agents_tasks/... for available tasks)
        :param json_params: Dict with parameters for agent_task
        :return: agent_task.wait_result()
        """
        agent_task = await agent_task.kiq(json_params)
        return await agent_task.wait_result()


#with open("backend/broker/basic_login.json", 'r') as fout:
#basic_login = json.load(fout)
driver = AsyncGraphDatabase.driver('bolt://localhost:7687', auth=("neo4j", "ostisGovno"))
reader = Reader()
crud = CRUDAgent(reader, driver, 'neo4j')

BROKER = AgentsBroker(
    crud,
    url="redis://localhost:6379"
).with_result_backend(RedisAsyncResultBackend(redis_url="redis://localhost:6379"))

print("pank pank pank pank")
