from src.agents.planner import planner_agent
from src.graph.workflow import graph
query = input(
    "Research Topic: "
)
result = planner_agent(query)
result = graph.invoke(
    {
        "topic":
        query
    }
)

print("\nFINAL STATE\n")

print(result)