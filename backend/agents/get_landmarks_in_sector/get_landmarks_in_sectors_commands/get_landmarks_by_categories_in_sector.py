# Author: Meteorych
from typing import Dict

from backend.agents import PureCRUDAgent
from backend.agents.get_landmarks_in_sector import get_landmarks_in_sectors_agent, GetLandmarksInSectorsAgent
from backend.command_bases.base_command import BaseCommand


class LandmarksOfCategoriesInUserViewCommand(BaseCommand):
    """
    Command to get landmarks that located in given map sectors and refer to given categories by coordinates of user view's borders.
    """

    def __init__(self, get_landmarks_in_sectors: GetLandmarksInSectorsAgent, coords_of_square: Dict, categories: dict,
                 crud_agent: PureCRUDAgent):
        """
        Creates command to get landmarks that located in given map sectors and refer to given categories from
        getLandmarksInSectorsAgent.

        :param get_landmarks_in_sectors: getLandmarksInSectorsAgent child class entity to get from
        :param coords_of_square: Dict in form {
         "TL": {
             "latitude": Double,
             "longitude": Double
         },
         "BR": {
             "latitude": Double,
             "longitude": Double
         }
       }
        :param categories: Dict in form {
            "categories": List
        }
        :param crud_agent: PureCRUDAgent child class entity to get from
        """
        self._json_params1 = coords_of_square
        self._json_params2 = categories
        self.agent = crud_agent
        super().__init__(get_landmarks_in_sectors)

    async def execute(self):
        """
        Execute command to get landmarks that located in given map sectors and refer to given categories from
        getLandmarksInSectorsAgent.

        :return: Coroutine
            List[
                Dict[
                    "landmark": Dict | None,
                    "map_sector": Dict | None,
                    "category": Dict | None
                ]
            ]
        """
        return await self._target_agent.get_landmarks_of_categories_in_map_sectors(self._json_params1, self._json_params2, self.agent)
