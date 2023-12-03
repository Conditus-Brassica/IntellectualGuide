#Author: Vodohleb04
from typing import Dict
from abc import ABC, abstractmethod


class PureCRUDAgent(ABC):
    """
    Pure abstract class of CRUDAgent. Provides methods for commands from the other agents.
    All work with kb provided by child classes of this class.

    All methods work asynchronously.
    """

    @abstractmethod
    async def get_categories_of_region(self, json_params: Dict):
        """
        Returns from kb categories of region with included regions. Finds region by its name.
        Works asynchronously.

        :param json_params: Dict in form {"region_name": str, "optional_limit": int | None}
        :return: Coroutine
            List[
                {
                    "category": {"name": str} | None,
                    "located_at": {"name": str} | None
                }
            ]
        """
        raise NotImplementedError

    @abstractmethod
    async def get_landmarks_in_map_sectors(self, json_params: Dict):
        """
        Returns from kb landmarks, located in passed map sectors. Finds map sectors by their names.
        Works asynchronously.

        :param json_params: Dict in form {"sector_names": List[str], "optional_limit": int | None}
        :return: Coroutine
            List [
                {
                    "landmark": Dict | None,
                    "sector": Dict | None
                }
            ]
        """
        raise NotImplementedError

    @abstractmethod
    async def get_landmarks_refers_to_categories(self, json_params: Dict):
        """
        Returns from kb landmarks, that refers to given categories. Finds categories by their names
        Works asynchronously.

        :param json_params: Dict in form {"categories_names": List[str], "optional_limit": int | None}
        :return: Coroutine
            List [
                {
                    "landmark": Dict | None,
                    "category": Dict | None
                }
            ]
        """
        raise NotImplementedError

    @abstractmethod
    async def get_landmarks_by_coordinates(self, json_params: Dict):
        """
        Returns from kb landmarks with given coordinates.
        Works asynchronously.

        :param json_params: Dict in form {
                "coordinates": List [
                    Dict [
                        "latitude": float,
                        "longitude": float
                    ]
                ],
                "optional_limit": int | None
            }
        :return: Coroutine
            List [
                Dict["landmark": Dict | None]
            ]
        """
        raise NotImplementedError

    @abstractmethod
    async def get_landmarks_by_names(self, json_params: Dict):
        """
        Returns from kb landmarks with given names.
        Works asynchronously.

        :param json_params: Dict in form {"landmark_names": List[str], "optional_limit": int | None}
        :return: Coroutine
            List [
                Dict["landmark": Dict | None]
            ]
        """
        raise NotImplementedError

    @abstractmethod
    async def get_landmarks_of_categories_in_region(self, json_params: Dict):
        """
        Returns from kb landmarks, located in given region, that refer to given categories.
        Finds region by its name. Finds categories by their names.
        Works asynchronously.

        :param json_params: Dict in form {
                "region_name": str,
                "categories_names": List[str],
                "optional_limit": int | None
            }
        :return: Coroutine
            List [
                Dict[
                    "landmark": Dict | None,
                    "located_at": Dict | None,
                    "category": Dict | None
                ]
            ], where "located_at" is the region, where landmark is located
        """
        raise NotImplementedError

    @abstractmethod
    async def get_landmarks_by_region(self, json_params: Dict):
        """
        Returns from kb landmarks, located in region. Finds region by its name.
        Works asynchronously.

        :param json_params: Dict in form {"region_name": str, "optional_limit": int | None}
        :return: Coroutine
            List[
                Dict[
                    "landmark": Dict | None,
                    "located_at": Dict | None
                ]
            ],  where "located_at" is the region, where landmark is located
        """
        raise NotImplementedError

    @abstractmethod
    async def get_recommendations_for_landmark_by_region(self, json_params: Dict):
        """
            Returns recommended landmarks for given landmark and given user. Finds given landmark by its name and
            coordinates; finds user by his/her login. Returns recommended landmark, categories of recommended landmark,
            distance from current_landmark to recommended landmark in meters, category of the given landmark, node of
            the given User account, "wish" mark, if user left it on recommended landmark (else None), "visited" mark
            with the amount of visits, if user already visited this landmark (else None)/
            Works asynchronously.

            :param json_params: Dict in form {
                "user_login": str,
                "current_latitude": float,
                "current_longitude": float,
                "current_name": str,
                "amount_of_recommendations": int
            }, where current_name is the name of given landmark
            :return: Coroutine
            List[
                Dict[
                    "recommendation": Dict | None,
                    "recommendation_landmark_category_ref": Dict | None,
                    "distance": float | None,
                    "current_landmark_category_ref": Dict | None,
                    "category": Dict | None,
                    "userAccount": Dict | None,
                    "wish_ref": Dict | None,
                    "visited_ref": Dict | None
                ]
            ]
        """
        raise NotImplementedError



