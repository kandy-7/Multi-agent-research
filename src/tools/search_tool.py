from ddgs import DDGS


def search_web(query, max_results=5):

    urls = []

    blocked_sites = [
        "linkedin.com",
        "facebook.com",
        "instagram.com",
        "youtube.com",
        "twitter.com",
        "x.com"
    ]

    results = DDGS().text(
        query,
        max_results=max_results * 2
    )

    for result in results:

        url = result["href"]

        if any(
            site in url
            for site in blocked_sites
        ):
            continue

        print(url)

        urls.append(url)

        if len(urls) >= max_results:
            break

    return urls