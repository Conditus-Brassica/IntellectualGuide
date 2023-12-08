from taskiq_redis import ListQueueBroker, RedisAsyncResultBackend

from pure_broker import PureBroker


class AgentsBroker(PureBroker):
    broker = ListQueueBroker(
        url="redis://localhost:6379"
    ).with_result_backend(RedisAsyncResultBackend(redis_url="redis://localhost:6379"))
