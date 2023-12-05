from typing import Dict
from backend.agents.get_landmarks_in_sector import GetLandmarksInSectorsAgent
from backend.agents.get_landmarks_in_sector.get_landmarks_in_sectors_commands.get_landmarks_by_categories_in_sector import \
    LandmarksOfCategoriesInUserViewCommand
from backend.agents.get_landmarks_in_sector.get_landmarks_in_sectors_commands.get_landmarks_in_sector import \
    LandmarksInUserViewCommand


class GetLandmarksInSectorCommandsFabric:
    """Fabric used to create commands for Agent"""

    @staticmethod
    def create_get_landmarks_in_sector_command(get_landmarks_in_sectors_agent: GetLandmarksInSectorsAgent, json_params: Dict) \
            -> LandmarksInUserViewCommand:
        """
        Creates command to get landmarks that located in given map sectors from
        getLandmarksInSectorsAgent.

        :param get_landmarks_in_sectors_agent: PureCRUDAgent child class entity to get from
        :param json_params: # TODO Fill
        """
        return LandmarksInUserViewCommand(get_landmarks_in_sectors_agent, json_params)

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