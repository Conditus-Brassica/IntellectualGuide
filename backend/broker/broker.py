from taskiq_redis import ListQueueBroker, RedisAsyncResultBackend


class Broker:

    __instances_amount = 0
    broker = None

    @classmethod
    def __class_init__(cls, broker: ListQueueBroker):
        cls.broker = broker

    def __init__(self, broker: ListQueueBroker):
        if self.__instances_amount == 0:
            self.__class_init__(broker)
            self.__instances_amount += 1
        else:
            raise RuntimeError("Broker can have only one instance")


if __name__ == '__main__':
    broker = ListQueueBroker(
        url="redis://localhost:6379"
    ).with_result_backend(RedisAsyncResultBackend(redis_url="redis://localhost:6379"))
    br = Broker(broker)
