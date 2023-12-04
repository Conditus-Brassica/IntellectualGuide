# Author: Vodohleb04
from typing import Dict
from backend.command_bases.base_command import BaseCommand
from backend.agents.crud_agent.pure_classes.pure_crud_agent import PureCRUDAgent


class LandmarksByRegionCommand(BaseCommand):
    """
    Command to get landmarks by region from PureCRUDAgent children classes.
    """

    def __init__(self, crud_agent: PureCRUDAgent, json_params: Dict):
        """
        Creates Command to get landmarks by region from PureCRUDAgent children classes.

        :param crud_agent: PureCRUDAgent child class entity to get from
        :param json_params: Dict in form {"region_name": str, "optional_limit": int | None}
        """
        self._json_params = json_params
        super().__init__(crud_agent)

    async def execute(self):
        """
        Execute command to get landmarks by region from PureCRUDAgent children classes.
        Works asynchronously.

        :return: Coroutine
            List[
                Dict[
                    "landmark": Dict | None,
                    "located_at": Dict | None
                ]
            ],  where "located_at" is the region, where landmark is located
        """
        return await self._target_agent.get_landmarks_by_region(self._json_params)
