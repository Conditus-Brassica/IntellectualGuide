#Author: Vodohleb04
from typing import Dict
from taskiq_redis import ListQueueBroker
from backend.agents.crud_agent import PureCRUDAgent


class AgentsBroker(ListQueueBroker):
    """
    Custom broker class to work with agents.
    Class is singleton.
    """
    __single_broker = None

    @classmethod
    def get_broker(cls):
        """
        Method to take broker object. Returns None in case when broker is not exists.
        :return: None | AgentsBroker
        """
        return cls.__single_broker

    @classmethod
    def broker_exists(cls) -> bool:
        """Method to check if broker object already exists"""
        if cls.__single_broker:
            return True
        else:
            return False

    def __init__(self, crud: PureCRUDAgent, *args, **kwargs):
        """
        Init method

        :param crud: child class of PureCRUDAgent
        """
        if not self.__single_broker:
            self.crud = crud
            super().__init__(*args, **kwargs)
            self.__single_broker = self

    async def shutdown(self) -> None:
        await self.crud.close()
        await super().shutdown()

    @staticmethod
    async def call_agent_task(agent_task, json_params: Dict):
        """
        Wrapper to call task using broker. Call tasks only using this function.
        Works asynchronously.

        :param agent_task: task to call (check broker/agents_tasks/... for available tasks). Takes only function name
        without arguments
        :param json_params: Dict with arguments to run the agent\'s function.
        :return: agent_task.wait_result(). Use return_value property to get result of agent_task
        """
        agent_task = await agent_task.kiq(json_params)
        return await agent_task.wait_result()

