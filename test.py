from src.tools.search_tool import search_web

urls = search_web(
    "IT recruitments in India",
    max_results=3
)

print("\nFOUND URLS\n")

print(urls)