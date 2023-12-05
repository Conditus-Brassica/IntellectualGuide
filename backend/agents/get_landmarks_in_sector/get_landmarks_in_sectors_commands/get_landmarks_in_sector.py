# Author: Meteorych
from typing import Dict
from backend.agents.get_landmarks_in_sector import GetLandmarksInSectorsAgent
from backend.command_bases.base_command import BaseCommand

class LandmarksInUserViewCommand(BaseCommand):
    """
    Command to get landmarks that located in given map sectors from PureCRUDAgent children classes.
    """

    def __init__(self, get_landmarks_in_sectors: GetLandmarksInSectorsAgent, json_params: Dict):
        """
        Creates command to get landmarks that located in given map sectors from
        getLandmarksInSectorsAgent.

        :param get_landmarks_in_sectors: GetLandmarksInSectorsAgent entity to get from
        :param json_params: # TODO Fill
        """
        self._json_params = json_params
        super().__init__(get_landmarks_in_sectors)

    async def execute(self):
        """
        Execute command to get landmarks that located in given map sectors from
        getLandmarksInSectorsAgent.

        :return: Coroutine
            List [
                {
                    # TODO Fill
                }
            ], where categories_names are categories of landmark
        """
        return await self._target_agent.get_landmarks_in_map_sectors(self._json_params)
