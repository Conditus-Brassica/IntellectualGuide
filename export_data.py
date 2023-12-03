#Author: Vodohleb04
import json
import asyncio
import aiologger
from typing import List
from neo4j import GraphDatabase


driver = GraphDatabase.driver('bolt://localhost:7687', auth=('neo4j', 'ostisGovno'))

result, summary, keys = driver.execute_query(
    """MATCH (n:Region WHERE n.name=$name) RETURN n""",
    name='Беларусь',
    database_='neo4j'
)
for node in result:
    print(node.data()["n"])


