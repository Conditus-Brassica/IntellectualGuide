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
    async def get_recommendations_by_coordinates_and_categories(self, json_params: Dict):
        """
        Method to get recommendations from agent.

        :param json_params: Dict in form {
             "coordinates_of_points": List [
                Dict [
                    "latitude": float,
                    "longitude": float
                ]
            ],
            "categories_names": List[str],
            "user_login": str,
            "amount_of_recommendations": int
        }, where current_name is the name of given landmark
        :return: Coroutine
            List[
                {recommendation: Dict | None}
            ]
        """
        raise NotImplementedError
