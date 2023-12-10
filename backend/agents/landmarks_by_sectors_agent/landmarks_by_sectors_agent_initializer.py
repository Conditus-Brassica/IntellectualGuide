from neo4j import AsyncGraphDatabase

from backend.agents.crud_agent.reader import Reader
from backend.agents.landmarks_by_sectors_agent.landmarks_by_sectors_agent import LandmarksBySectorsAgent

if LandmarksBySectorsAgent.landmarks_by_sectors_agent_exists():
    LANDMARKS_BY_SECTORS_AGENT = LandmarksBySectorsAgent.landmarks_by_sectors_agent_exists()
    print("Agent LandmarksBySectors was not created")  # TODO remove
else:
    driver = AsyncGraphDatabase.driver('bolt://localhost:7687', auth=("neo4j", "ostisGovno"))
    reader = Reader()
    LANDMARKS_BY_SECTORS_AGENT = LandmarksBySectorsAgent()
    print("LandmarksBySectors was created")  # TODO remove
