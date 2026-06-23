from typing import TypedDict

class ResearchState(TypedDict):
    topic: str
    plan: str
    urls: list
    scraped_data: str
    summary: str
    report: str
    sources: list