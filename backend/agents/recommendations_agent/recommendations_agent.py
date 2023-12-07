# Author: Vodohleb04
from typing import Dict, List

from backend.agents.recommendations_agent.pure_recommendations_agent import PureRecommendationsAgent


class RecommendationsAgent(PureRecommendationsAgent):

    @staticmethod
    def _categories_overlay(
            user_categories_preference: Dict[str, int], categories_list: List[str], preference_unifier: float
    ):
        result_coefficient = 0
        i = 0
        while i < len(categories_list):
            result_coefficient += user_categories_preference.get(categories_list[i], 0) / preference_unifier
            i += 1
        return result_coefficient

    @staticmethod
    def _additive_super_criteria(
            user_categories_preference: Dict[str, int],
            main_categories_names: List[str],
            subcategories_names: List[str],
            distance: float,
            wish_to_visit: bool,
            visited_amount: int,
            coefficients: Dict[str, float],
            params_unifier: Dict[str, float]
    ) -> float:
        return (
                RecommendationsAgent._categories_overlay(
                    user_categories_preference, main_categories_names, params_unifier["user_categories_preference"]
                )
                * coefficients["main_categories_names"] / params_unifier["user_categories_preference"] +
                RecommendationsAgent._categories_overlay(
                    user_categories_preference, subcategories_names, params_unifier["user_categories_preference"]
                )
                * coefficients["subcategories_names"] / params_unifier["user_categories_preference"] +
                distance
                * coefficients["distance"] / params_unifier["distance"] +
                wish_to_visit
                * coefficients["wish_to_visit"] / params_unifier["wish_to_visit"] +
                visited_amount
                * coefficients["visited_amount"] / params_unifier["visited_amount"]
        )

    def get_recommendations_by_coordinates_and_categories(self, json_params: Dict):
        # TODO check params
        # TODO CRUD agent request
        # TODO Cash request
        # TODO count unifier values
        # TODO define most needed
        pass

