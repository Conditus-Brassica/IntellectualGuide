#Author: Vodohleb04
from abc import ABC, abstractmethod
from .base_command import BaseCommand


class Sender(ABC):
    """
        Abstract class, that defines behaviour of classes, that can send commands to agents.
        Agent can be a sender.
    """

    @staticmethod
    async def send_command(command: BaseCommand):
        """
            Sends command to the target agent. Command defines by itself what agent is the target.
            Works asynchronously.
        """
        return await command.execute()

