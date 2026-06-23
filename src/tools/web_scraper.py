import requests
from bs4 import BeautifulSoup


def scrape_page(url):

    headers = {
        "User-Agent":
        "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    title = soup.title.text \
        if soup.title else ""

    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()

    content = soup.get_text(
        separator=" ",
        strip=True
    )

    return {
        "title": title,
        "content": content[:5000]
    }