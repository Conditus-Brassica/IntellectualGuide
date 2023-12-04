#Author: Vodohleb04
from abc import ABC, abstractmethod
from typing import Dict
from backend.command_bases import Sender


class PureRecommendationsAgent(Sender, ABC):
    """
    Pure abstract class of Recommendations agent. Provides methods for commands from the other agents.
    All work with kb provided by child classes of this class.

    All methods work asynchronously.
    """

    @abstractmethod
    async def get_recommendations(self, json_params: Dict):
        """
        Method to get recommendations from agent.

        :param json_params: Dict in form {
            "user_login": str,
            "current_latitude": float,
            "current_longitude": float,
            "current_name": str,
            "recommendations_amount": int
        }, where current_name is the name of given landmark
        :return: Coroutine
            List[
                {
                    recommended:
                }
            ]
        """
        raise NotImplementedError
