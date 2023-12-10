from abc import abstractmethod
from typing import Dict


class PURELandmarksBySectorsAgent:
    """
        Pure abstract class of Recommendations agent. Provides methods for commands from the other agents.
        All work with kb provided by child classes of this class.

        All methods work asynchronously.
        """

    _single_landmarks_agent = None

    @abstractmethod
    def get_landmarks_by_sectors_agent(self):
        """
        Method to take landmarks by sectors agent object. Returns None in case when landmarks by sectors agent is not exists.
        :return: None | PURELandmarksBySectorsAgent
        """
        raise NotImplementedError

    @abstractmethod
    def landmarks_by_sectors_agent_exists(self) -> bool:
        """Method to check if landmarks by sectors agent object already exists"""

        raise NotImplementedError

    @abstractmethod
    async def get_landmarks_in_sector(self, json_params: Dict):
        """
        # TODO Fill this
        """
        raise NotImplementedError

    @abstractmethod
    async def get_landmarks_by_categories_in_sector(self, json_params: Dict):
        """
        # TODO Fill this
        """
        raise NotImplementedError

