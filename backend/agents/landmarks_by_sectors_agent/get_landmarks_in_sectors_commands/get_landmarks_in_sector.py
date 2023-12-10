# Author: Meteorych
from typing import Dict

from backend.agents import PureCRUDAgent
from backend.agents.landmarks_by_sectors_agent import GetLandmarksInSectorsAgent
from backend.command_bases.base_command import BaseCommand

class LandmarksInUserViewCommand(BaseCommand):
    """
    Command to get landmarks that located in given map sectors from PureCRUDAgent children classes.
    """

    def __init__(self, get_landmarks_in_sectors: GetLandmarksInSectorsAgent, coords_of_square: Dict, agent: PureCRUDAgent):
        """
        Creates command to get landmarks that located in given map sectors from
        getLandmarksInSectorsAgent.

        :param get_landmarks_in_sectors: GetLandmarksInSectorsAgent entity to get from
        :param coords_of_square: Dict in form {
        "TL": {
            "latitude": double,
            "longitude": double
        },
        "BR": {
            "latitude": double,
            "longitude": double
        }
      }
        """
        self._json_params = coords_of_square
        self.agent = agent
        super().__init__(get_landmarks_in_sectors)

    async def execute(self):
        """
        Execute command to get landmarks that located in given map sectors from
        getLandmarksInSectorsAgent.

        :return: Coroutine
            List [
                {
                    "landmark": Dict | None,
                    "sector": Dict | None,
                    "categories_names": List[str] | [] (empty list)
                }
            ], where categories_names are categories of landmark
        """
        return await self._target_agent.get_landmarks_in_map_sectors(self._json_params, self.agent)
