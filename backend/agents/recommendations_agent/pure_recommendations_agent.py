#Author: Vodohleb04
from abc import ABC, abstractmethod
from typing import Dict


class PureRecommendationsAgent(ABC):
    """
    Pure abstract class of Recommendations agent. Provides methods for commands from the other agents.
    All work with kb provided by child classes of this class.

    All methods work asynchronously.
    """

    _single_recommendations_agent = None

    @classmethod
    def get_recommendations_agent(cls):
        """
        Method to take recommendations agent object. Returns None in case when recommendations agent is not exists.
        :return: None | PureRecommendationsAgent
        """
        return cls._single_recommendations_agent

    @classmethod
    def recommendations_agent_exists(cls) -> bool:
        """Method to check if recommendations agent object already exists"""
        if cls._single_recommendations_agent:
            return True
        else:
            return False

    @abstractmethod
    async def find_recommendations_for_coordinates_and_categories(self, json_params: Dict):
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
            "amount_of_recommendations_for_point": int,
            "maximum_amount_of_recommendations": int,
            "optional_limit": int | None,
        }, where current_name is the name of given landmark
        :return: Coroutine
            List[
                {
                    recommendation: Dict | None
                }
            ]
        """
        raise NotImplementedError
