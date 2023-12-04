# Author: Vodohleb04
from typing import Dict
from backend.command_bases.base_command import BaseCommand
from backend.agents.crud_agent.pure_crud_classes.pure_crud_agent import PureCRUDAgent


class LandmarksInMapSectorsCommand(BaseCommand):
    """
    Command to get landmarks that located in given map sectors from PureCRUDAgent children classes.
    """

    def __init__(self, crud_agent: PureCRUDAgent, json_params: Dict):
        """
        Creates Command to get landmarks that located in given map sectors from PureCRUDAgent children classes.

        :param crud_agent: PureCRUDAgent child class entity to get from
        :param json_params: Dict in form {"sector_names": List[str], "optional_limit": int | None}
        """
        self._json_params = json_params
        super().__init__(crud_agent)

    async def execute(self):
        """
        Execute command to get landmarks that located in given map sectors from PureCRUDAgent children classes.
        Works asynchronously.

        :return: Coroutine
            List [
                {
                    "landmark": Dict | None,
                    "sector": Dict | None
                }
            ]
        """
        return await self._target_agent.get_landmarks_in_map_sectors(self._json_params)
