from src.agents.planner import planner_agent
from src.agents.summary_agent import summary_agent
from src.agents.report_agent import report_agent
from src.agents.scraper_agent import scraper_agent
from src.agents.search_agent import search_agent
from langgraph.graph import StateGraph
from langgraph.graph import START, END

from src.graph.state import ResearchState

from src.agents.planner import planner_agent
def planner_node(state):

    print("\nPlanner Running...\n")

    state["plan"] = planner_agent(
        state["topic"]
    )

    return state

def search_node(state):

    print("\nSearch Running...\n")

    state["urls"] = search_agent(
        state["topic"]
    )
  
    print("\n========== URLS ==========\n")
    print(state["urls"])
    return state
def scraper_node(state):

    print("\nScraper Running...\n")

    all_content = []

    for url in state["urls"]:

        print(f"\nScraping: {url}")

        try:

            data = scraper_agent(url)

            print(
                f"Content Length: {len(data['content'])}"
            )

            all_content.append(
                data["content"]
            )

        except Exception as e:

            print(
                f"Failed: {url}"
            )

            print(e)

    state["scraped_data"] = "\n\n".join(
        all_content
    )
    print("\nSCRAPED DATA LENGTH:")
    print(len(state["scraped_data"]))
    return state


def summary_node(state):

    print("\nSummary Running...\n")

    state["summary"] = summary_agent(
        state["scraped_data"]
    )
    print("\nFIRST 500 CHARS\n")
    print(state["scraped_data"][:500])
    return state

def report_node(state):

    print("\nReport Running...\n")

    state["report"] = report_agent(
        state["summary"]
    )

    return state

builder = StateGraph(
    ResearchState
)
builder.add_node(
    "planner",
    planner_node
)
builder.add_node(
    "search",
    search_node
)
builder.add_node(
    "scraper",
    scraper_node
)

builder.add_node(
    "summary",
    summary_node
)

builder.add_node(
    "report",
    report_node
)
builder.add_edge(
    START,
    "planner"
)

builder.add_edge(
    "planner",
    "search"
)
builder.add_edge(
    "search",
    "scraper"
)

builder.add_edge(
    "scraper",
    "summary"
)

builder.add_edge(
    "summary",
    "report"
)

builder.add_edge(
    "report",
    END
)
graph = builder.compile()