# Author: Meteorych
"""Tasks to work with agent to get landmarks in sectors. Use broker to run tasks"""
from typing import Dict
from ..broker_initializer import BROKER


@BROKER.task
async def get_landmarks_in_sector(json_params: Dict):
    """
        :param json_params: Dict in form {
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
    return await BROKER.sectors_agent.get_categories_of_region(json_params)


@BROKER.task
async def get_landmarks_by_categories_in_sector(json_params: Dict):
    """
    Kick this task to get landmarks, located in passed map sectors. Finds map sectors by their names.
        :param json_params: Dict in form {
            "coordinates": # TODO Fill
        }
        :return: LandmarksByCoordinatesCommand for CRUD
    """
    return await BROKER.sectors_agent.get_landmarks_in_map_sectors(json_params)
