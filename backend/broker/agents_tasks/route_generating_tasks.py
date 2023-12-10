from backend.broker.broker_initializer import BROKER
from backend.agents.routing_agent.rote_generating_agent_initializer import ROUTING_AGENT


@BROKER.task
async def get_optimized_route_task(landmark_list: list):
    """
    Method finds all optimized route points for provided points.
    :param landmark_list: [[latitude: float, longitude: float], ...]
    :return: Route points, landmarks in route order
    """
    return await ROUTING_AGENT.get_optimized_route(landmark_list)


@BROKER.task
async def get_optimized_route_main_points_task(landmark_list: list):
    """
    Method finds all optimized route points for provided points.
    Return one point per 30 km.
    :param landmark_list: [[latitude: float, longitude: float], ...]
    :return: Route points, landmarks in route order
    """
    return await ROUTING_AGENT.get_optimized_route_main_points(landmark_list)
