# Author: Vodohleb04
from typing import Dict
from backend.command_bases.base_command import BaseCommand
from backend.agents.crud_agent.pure_crud_classes.pure_crud_agent import PureCRUDAgent


class RecommendationsByCoordinatesAndCategoriesCommand(BaseCommand):
    """
    Command to get recommendations by coordinates and categories from PureCRUDAgent children classes.
    """

    def __init__(self, crud_agent: PureCRUDAgent, json_params: Dict):
        """
        Creates Command to get recommendations by coordinates and categories from PureCRUDAgent children classes.

        :param crud_agent: PureCRUDAgent child class entity to get from
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
        """
        self._json_params = json_params
        super().__init__(crud_agent)

    async def execute(self):
        """
        Execute command to get recommendations by coordinates and categories from PureCRUDAgent children classes.
        Works asynchronously.

        :return: Coroutine
            List[
                Dict[
                    recommended_landmark: Dict | None,
                    recommendation_category_is_main: True | None,
                    category: Dict | None,
                    user_account: Dict | None,
                    wish_ref: Dict | None,
                    visited_ref: Dict | None;
                ]
            ]
        """
        return await self._target_agent.find_recommendations_for_coordinates_and_categories(self._json_params)
