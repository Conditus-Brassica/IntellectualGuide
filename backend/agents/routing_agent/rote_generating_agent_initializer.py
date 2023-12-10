from backend.agents.routing_agent.route_generating import RoutingAgent

if RoutingAgent.routing_agent_exists():
    ROUTING_AGENT = RoutingAgent.get_route_generating_agent()
    print("RoutingAgent wasn't created")
else:
    ROUTING_AGENT = RoutingAgent()
    print("RoutingAgent wasn created")
