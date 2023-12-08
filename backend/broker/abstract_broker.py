from taskiq_redis import ListQueueBroker, RedisAsyncResultBackend
from abc import ABC, abstractmethod


class AbstractBroker(ABC):
    broker = ListQueueBroker(
        url="redis://localhost:6379"
    ).with_result_backend(RedisAsyncResultBackend(redis_url="redis://localhost:6379"))
    # @classmethod
    # @abstractmethod
    # def method(cls):
    #     raise NotImplementedError
    pass
