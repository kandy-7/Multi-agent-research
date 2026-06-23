from src.tools.search_tool import search_web


def search_agent(topic):

    urls = search_web(
        topic,
        max_results=3
    )

    return urls