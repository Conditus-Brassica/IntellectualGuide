from typing import Dict

from backend.agents import PureCRUDAgent
from backend.agents.landmarks_by_sectors_agent import GetLandmarksInSectorsAgent
from backend.agents.landmarks_by_sectors_agent.get_landmarks_in_sectors_commands.get_landmarks_by_categories_in_sector import \
    LandmarksOfCategoriesInUserViewCommand
from backend.agents.landmarks_by_sectors_agent.get_landmarks_in_sectors_commands.get_landmarks_in_sector import \
    LandmarksInUserViewCommand


class GetLandmarksInSectorCommandsFabric:
    """Fabric used to create commands for Agent"""

    @staticmethod
    def create_get_landmarks_in_sector_command(get_landmarks_in_sectors_agent: GetLandmarksInSectorsAgent, coords_of_square: Dict,
                                               crud_agent: PureCRUDAgent) \
            -> LandmarksInUserViewCommand:
        """
        Creates command to get landmarks that located in given map sectors from
        getLandmarksInSectorsAgent.

        :param get_landmarks_in_sectors_agent: Get landmarks in sectors agent
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
        :param crud_agent: PureCRUDAgent child class entity to get from
        """
        return LandmarksInUserViewCommand(get_landmarks_in_sectors_agent, coords_of_square, crud_agent)

    @staticmethod
    def create_get_landmarks_by_categories_in_sector_command(
            get_landmarks_in_sectors_agent: GetLandmarksInSectorsAgent, json_params: Dict
    ) -> LandmarksOfCategoriesInUserViewCommand:
        """
        Creates Command to get landmarks with given coordinates from PureCRUDAgent children classes.

        :param get_landmarks_in_sectors_agent: PureCRUDAgent child class entity to get from
        :param json_params: Dict in form {
            "coordinates": # TODO Fill
        }
        :return: LandmarksByCoordinatesCommand for CRUD
        """
        return LandmarksOfCategoriesInUserViewCommand(get_landmarks_in_sectors_agent, json_params)
