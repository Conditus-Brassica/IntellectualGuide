#Author: Vodohleb04
from abc import ABC, abstractmethod


class BaseCommand(ABC):
    """
        Basic abstract class of command, that defines general behaviour of commands
    """

    def __init__(self, target_agent):
        """
            __init__ method of command.
            target_agent: Any - agent, whose method will be called in BaseCommand.execute()
        """
        self._target_agent = target_agent

    @abstractmethod
    async def execute(self):
        """
            Pure abstract method to run target function of command
            target function must be async, call it with async
        """
        raise NotImplementedError
