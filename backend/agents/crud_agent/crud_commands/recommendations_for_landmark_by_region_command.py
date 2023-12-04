# Author: Vodohleb04
from typing import Dict
from backend.command_bases.base_command import BaseCommand
from backend.agents.crud_agent.pure_crud_classes.pure_crud_agent import PureCRUDAgent


class RecommendationsForLandmarkByRegionCommand(BaseCommand):
    """
    Command to get recommendations for landmark by region from PureCRUDAgent children classes
    """

    def __init__(self, crud_agent: PureCRUDAgent, json_params: Dict):
        """
        Creates Command to get recommendations for landmark by region from PureCRUDAgent children classes

        :param crud_agent: PureCRUDAgent child class entity to get from
        :param json_params: Dict in form {
            "user_login": str,
            "current_latitude": float,
            "current_longitude": float,
            "current_name": str,
            "amount_of_recommendations": int
        }, where current_name is the name of given landmark
        """
        self._json_params = json_params
        super().__init__(crud_agent)

    async def execute(self):
        """
        Execute command to get recommendations for landmark by region from PureCRUDAgent children classes.
        Works asynchronously.

        :return: Coroutine
            List[
                Dict[
                    "recommendation": Dict | None,
                    "recommendation_landmark_category_ref": Dict | None,
                    "distance": float | None,
                    "current_landmark_category_ref": Dict | None,
                    "category": Dict | None,
                    "userAccount": Dict | None,
                    "wish_ref": Dict | None,
                    "visited_ref": Dict | None
                ]
            ]
        """
        return await self._target_agent.get_recommendations_for_landmark_by_region(self._json_params)
