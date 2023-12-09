from taskiq_redis import RedisAsyncResultBackend
from neo4j import AsyncGraphDatabase
from backend.agents.crud_agent import CRUDAgent, Reader
from .agents_broker import AgentsBroker


#with open("backend/broker/basic_login.json", 'r') as fout:
#basic_login = json.load(fout)


if AgentsBroker.broker_exists():
    BROKER = AgentsBroker.get_broker()
    print("Broker wasn't created")  # TODO remove
else:
    driver = AsyncGraphDatabase.driver('bolt://localhost:7687', auth=("neo4j", "ostisGovno"))
    reader = Reader()
    crud = CRUDAgent(reader, driver, 'neo4j')
    BROKER = AgentsBroker(
        crud,
        url="redis://localhost:6379"
    ).with_result_backend(RedisAsyncResultBackend(redis_url="redis://localhost:6379"))
    print("Broker was created")  # TODO remove
