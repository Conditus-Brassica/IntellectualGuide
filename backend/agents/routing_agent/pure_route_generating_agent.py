from abc import ABC, abstractmethod


class PureRoutingAgent(ABC):
    """
    Agent for finding route points.
    Usage: when you need to create optimized
    route between several points.

    Uses api_key in api_key.py
    """

    __single_routing_agent = None

    @classmethod
    def get_route_generating_agent(cls):
        """
        Method to take route generating agent object. Returns None in case when route generating agent is not exists.
        :return: None | PureRoutingAgent
        """
        return cls.__single_routing_agent

    @classmethod
    def routing_agent_exists(cls) -> bool:
        """
        Method to check if route generating agent exists.
        :return: Boolean
        """
        if cls.__single_routing_agent:
            return True
        else:
            return False

    @abstractmethod
    async def get_optimized_route(self, landmark_list: list):
        """
        Method finds all optimized route points for provided points.
        :param landmark_list: [[latitude: float, longitude: float], ...]
        :return: Route points, landmarks in route order
        """
        raise NotImplementedError

    @abstractmethod
    async def __create_optimized_route(self):
        """
        Interaction with OpenRoutService API
        :return:
        """
        raise NotImplementedError
