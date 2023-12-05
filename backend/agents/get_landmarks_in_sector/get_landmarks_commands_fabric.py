from typing import Dict
from backend.agents.crud_agent.crud_commands import *
from backend.agents.crud_agent.pure_crud_classes import PureCRUDAgent


class GetLandmarksInSectorCommandsFabric:
    """Fabric used to create commands for Agent"""
    @staticmethod
    def create_landmarks_in_map_sectors_command(
            crud_agent: PureCRUDAgent, json_params: Dict
    ) -> LandmarksInMapSectorsCommand:
        """
        Creates Command to get landmarks that located in given map sectors from PureCRUDAgent children classes.

        :param crud_agent: PureCRUDAgent child class entity to get from
        :param json_params: Dict in form {"sector_names": List[str], "optional_limit": int | None}
        :return: LandmarksInMapSectorsCommand for CRUD
        """
        return LandmarksInMapSectorsCommand(crud_agent, json_params)

    @staticmethod
    def create_landmarks_of_categories_in_map_sectors_command(
        crud_agent: PureCRUDAgent, json_params: Dict
    ) -> LandmarksOfCategoriesInMapSectorsCommand:
        """
        Creates Command to get landmarks that located in given map sectors and refer to given categories from
        PureCRUDAgent children classes.

        :param crud_agent: PureCRUDAgent child class entity to get from
        :param json_params: Dict in form {
                "map_sectors_names": List[str],
                "categories_names": List[str],
                "optional_limit": int | None
        }
        :return: MapSectorsOfPointsCommand for CRUD
        """
        return LandmarksOfCategoriesInMapSectorsCommand(crud_agent, json_params)