# Author: Vodohleb04
"""Tasks to work with crud agent. Use broker to run tasks"""
from typing import Dict
from backend.broker.agents_broker import BROKER


@BROKER.task
async def categories_of_region_task(json_params: Dict):
    """
    Kick this task to get the categories of the region.
    Works asynchronously.

    :param json_params: Dict in form {
            "region_name": str,
            "optional_limit": int | None
        }
    :return: Coroutine
        List[
            {
                "category": {"name": str} | None,
                "located_at": {"name": str} | None
            }
        ]
    """
    return await BROKER.crud.get_categories_of_region(json_params)


@BROKER.task
async def landmarks_in_map_sectors_task(json_params: Dict):
    """
    Kick this task to get landmarks, located in passed map sectors. Finds map sectors by their names.
    Works asynchronously.

    :param json_params: Dict in form {
            "map_sectors_names": List[str],
            "optional_limit": int | None
        }
    :return: Coroutine
        List [
            {
                "landmark": Dict | None,
                "sector": Dict | None,
                "categories_names": List[str] | [] (empty list)
            }
        ], where categories_names are categories of landmark
    """
    return await BROKER.crud.get_landmarks_in_map_sectors(json_params)


@BROKER.task
async def landmarks_refers_to_categories_task(json_params: Dict):
    """
    Kick this task to get landmarks, that refers to given categories. Finds categories by their names.
    Works asynchronously.

    :param json_params: Dict in form {
            "categories_names": List[str],
            "optional_limit": int | None
        }
    :return: Coroutine
        List [
            {
                "landmark": Dict | None,
                "category": Dict | None
            }
        ]
    """
    return await BROKER.crud.get_landmarks_refers_to_categories(json_params)


@BROKER.task
async def landmarks_by_coordinates_task(json_params: Dict):
    """
    Kick this task to get landmarks with the given coordinates.
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
            Dict[
                "landmark": Dict | None,
                "categories_names": List[str] | [] (empty list)
            ]
        ],  where categories_names are categories of landmark
    """
    return await BROKER.crud.get_landmarks_by_coordinates(json_params)


@BROKER.task
async def landmarks_by_names_task(json_params: Dict):
    """
    Kick this task to get landmarks with given names.
    Works asynchronously.

    :param json_params: Dict in form {
            "landmark_names": List[str],
            "optional_limit": int | None
        }
    :return: Coroutine
        List [
            Dict[
                "landmark": Dict | None,
                "categories_names": List[str] | [] (empty list)
            ]
        ],  where categories_names are categories of landmark
    """
    return await BROKER.crud.get_landmarks_by_names(json_params)


@BROKER.task
async def landmarks_of_categories_in_region_task(json_params: Dict):
    """
    Kick this task to get landmarks, located in given region, that refer to given categories.
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
    return await BROKER.crud.get_landmarks_of_categories_in_region(json_params)


@BROKER.task
async def landmarks_by_region_task(json_params: Dict):
    """
    Kick this task to get landmarks, located in region. Finds region by its name.
    Works asynchronously.

    :param json_params: Dict in form {
            "region_name": str,
            "optional_limit": int | None
        }
    :return: Coroutine
        List[
            Dict[
                "landmark": Dict | None,
                "located_at": Dict | None,
                "categories_names": List[str] | [] (empty list)
            ]
        ],  where "located_at" is the region, where landmark is located, categories_names are categories of landmark
    """
    return await BROKER.crud.get_landmarks_by_region(json_params)


@BROKER.task
async def recommendations_for_landmark_by_region_task(json_params: Dict):
    """
    Kick this task to get recommended landmarks for given landmark and given user. Finds given landmark by its name and
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
            "main_categories_names": List[str] | [] (empty list),
            "subcategories_names": List[str] | [] (empty list),
            "distance": float | None,
            "user_account": Dict | None,
            "wish_to_visit": bool | None,
            "visited_amount": int | None
        ]
    ]
    """
    return await BROKER.crud.get_recommendations_for_landmark_by_region(json_params)


@BROKER.task
async def map_sectors_of_points_task(json_params: Dict):
    """
    Kick this task to get map sectors where given points are located.
    Works asynchronously.

    :param json_params: Dict in form {
        "coordinates_of_points": List[
            Dict [
                "longitude": float,
                "latitude": float
            ]
        ],
        "optional_limit": int | None
    }
    :return: Coroutine
    List[
        Dict[
            "of_point": Dict ["longitude": float, "latitude": float]
            "map_sector": Dict | None,
        ]
    ]
    """
    return await BROKER.crud.get_map_sectors_of_points(json_params)


@BROKER.task
async def landmarks_of_categories_in_map_sectors_task(json_params: Dict):
    """
    Kick this task to get landmarks that refer to the given categories and are located in the given map sectors.
    Finds map sectors by names. Finds categories by names.
    Works asynchronously.

    :param json_params: Dict in form {
        "map_sectors_names": List[str],
        "categories_names": List[str],
        "optional_limit": int | None
    }
    :return: Coroutine
    List[
        Dict[
            "landmark": Dict | None,
            "map_sector": Dict | None,
            "category": Dict | None
        ]
    ]
    """
    return await BROKER.crud.get_landmarks_of_categories_in_map_sectors(json_params)


@BROKER.task
async def recommendations_by_coordinates_and_categories_task(json_params: Dict):
    """
    Kick this task to get recommended landmarks for given user, given coordinates and given categories. Finds given
    landmark by its name and coordinates; finds user by his/her login. Returns recommended landmark, categories of
    recommended landmark, node of the given User account, "wish" mark, if user left it on recommended landmark
    (else None), "visited" mark with the amount of visits, if user already visited this landmark (else None)/
    Works asynchronously.

    :param json_params: Dict in form {
        "coordinates_of_points": List [
            Dict [
                "latitude": float,
                "longitude": float
            ]
        ],
        "categories_names": List[str],
        "user_login": str,
        "amount_of_recommendations_for_point": int
        "optional_limit": int | None
    }, where current_name is the name of given landmark
    :return: Coroutine
    List[
        Dict[
            "recommendation": Dict | None,
            "main_categories_names": List[str] | [] (empty list),
            "subcategories_names": List[str] | [] (empty list),
            "distance": float | None,
            "user_account": Dict | None,
            "wish_to_visit": bool | None,
            "visited_amount": int | None
        ]
    ]
    """
    return await BROKER.crud.get_recommendations_by_coordinates_and_categories(json_params)
