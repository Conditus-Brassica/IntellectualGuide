from backend.broker.abstract_broker import AbstractBroker
from backend.agents.crud_agent.pure_crud_classes import PureCRUDAgent


@AbstractBroker.broker
async def landmarks_by_region_task(json_params: Dict):
    """

    :param json_params:
    :return:
    """
    return await PureCRUDAgent.get_landmarks_by_region(json_params)
