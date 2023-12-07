#Author: Vodohleb04
from typing import Dict

from backend.agents.recommendations_agent.pure_recommendations_agent import PureRecommendationsAgent


class RecommendationsAgent(PureRecommendationsAgent):

    _coefficients = {
        "": 0
    }

    async def _additive_classifier(self, ):
        pass

    async def get_recommendations_by_coordinates_and_categories(self, json_params: Dict):
        # TODO check params
        # TODO CRUD agent request
        # TODO Cash request
        pass
