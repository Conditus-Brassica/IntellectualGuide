#Author: Vodohleb04
"""Commands fabric of CRUDAgent"""
from typing import Dict
from backend.agents.crud_agent.crud_commands import *
from backend.agents.crud_agent.pure_crud_classes import PureCRUDAgent


class CRUDCommandsFabric:
    """Fabric used to create commands for CRUDAgent"""

    @staticmethod
    def create_categories_of_region_command(crud_agent: PureCRUDAgent, json_params: Dict) -> CategoriesOfRegionCommand:
        """
        Creates Command to get landmarks categories of region from PureCRUDAgent children classes.

        :param crud_agent: PureCRUDAgent child class entity to get from
        :param json_params: Dict in form {"region_name": str, "optional_limit": int | None}
        :return: CategoriesOfRegionCommand for CRUD
        """
        return CategoriesOfRegionCommand(crud_agent, json_params)

    @staticmethod
    def create_landmarks_by_coordinates_command(
            crud_agent: PureCRUDAgent, json_params: Dict
    ) -> LandmarksByCoordinatesCommand:
        """
        Creates Command to get landmarks with given coordinates from PureCRUDAgent children classes.

        :param crud_agent: PureCRUDAgent child class entity to get from
        :param json_params: Dict in form {
            "coordinates": List [
                Dict [
                    "latitude": float,
                    "longitude": float
                ]
            ],
            "optional_limit": int | None
        }
        :return: LandmarksByCoordinatesCommand for CRUD
        """
        return LandmarksByCoordinatesCommand(crud_agent, json_params)

    @staticmethod
    def create_landmarks_by_names_command(crud_agent: PureCRUDAgent, json_params: Dict) -> LandmarksByNamesCommand:
        """
        Creates Command to get landmarks with the given names from PureCRUDAgent children classes.

        :param crud_agent: PureCRUDAgent child class entity to get from
        :param json_params: Dict in form {"landmark_names": List[str], "optional_limit": int | None}
        :return: LandmarksByNamesCommand for CRUD
        """
        return LandmarksByNamesCommand(crud_agent, json_params)

    @staticmethod
    def create_landmarks_by_region_command(crud_agent: PureCRUDAgent, json_params: Dict) -> LandmarksByRegionCommand:
        """
        Creates Command to get landmarks by region from PureCRUDAgent children classes.

        :param crud_agent: PureCRUDAgent child class entity to get from
        :param json_params: Dict in form {"region_name": str, "optional_limit": int | None}
        :return: LandmarksByRegionCommand for CRUD
        """
        return LandmarksByRegionCommand(crud_agent, json_params)

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
    def create_landmarks_of_categories_in_region_command(
            crud_agent: PureCRUDAgent, json_params: Dict
    ) -> LandmarksOfCategoriesInRegionCommand:
        """
        Creates Command to get landmarks that refer to any of the given categories and located in given region from
        PureCRUDAgent children classes.

        :param crud_agent: PureCRUDAgent child class entity to get from
        :param json_params: Dict in form {
                "region_name": str,
                "categories_names": List[str],
                "optional_limit": int | None
            }
        :return: LandmarksOfCategoriesInRegionCommand for CRUD
        """
        return LandmarksOfCategoriesInRegionCommand(crud_agent, json_params)

    @staticmethod
    def create_landmarks_refers_to_categories_command(
            crud_agent: PureCRUDAgent, json_params: Dict
    ) -> LandmarksRefersToCategoriesCommand:
        """
        Creates Command to get landmarks that refer to any of given categories from PureCRUDAgent children classes.

        :param crud_agent: PureCRUDAgent child class entity to get from
        :param json_params: Dict in form {"categories_names": List[str], "optional_limit": int | None}
        :return: LandmarksRefersToCategoriesCommand for CRUD
        """
        return LandmarksRefersToCategoriesCommand(crud_agent, json_params)

    @staticmethod
    def create_recommendations_for_landmark_by_region_command(
            crud_agent: PureCRUDAgent, json_params: Dict
    ) -> RecommendationsForLandmarkByRegionCommand:
        """
        Creates Command to get recommendations for landmark by region from PureCRUDAgent children classes.

        :param crud_agent: PureCRUDAgent child class entity to get from
        :param json_params: Dict in form {
            "user_login": str,
            "current_latitude": float,
            "current_longitude": float,
            "current_name": str,
            "amount_of_recommendations": int
        }, where current_name is the name of given landmark
        :return: RecommendationsForLandmarkByRegionCommand for CRUD
        """
        return RecommendationsForLandmarkByRegionCommand(crud_agent, json_params)

    @staticmethod
    def create_map_sectors_of_points_command(
        crud_agent: PureCRUDAgent, json_params: Dict
    ) -> MapSectorsOfPointsCommand:
        """
        Creates Command to get map sectors where given points are located from PureCRUDAgent children classes.

        :param crud_agent: PureCRUDAgent child class entity to get from
        :param json_params: Dict in form {
            "coordinates_of_points": List[
                Dict [
                    "longitude": float,
                    "latitude": float
                ]
            ],
            "optional_limit": int | None
        }
        :return: MapSectorsOfPointsCommand for CRUD
        """
        return MapSectorsOfPointsCommand(crud_agent, json_params)

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
