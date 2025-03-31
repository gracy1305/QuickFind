import requests

def get_search_results(query, category, start, api_key, cse_id):
    base_url = "https://www.googleapis.com/customsearch/v1"
    
    # Define category-specific parameters
    search_params = {
        "q": query,
        "cx": cse_id,
        "key": api_key,
        "start": start,
        "num": 10  # Number of results per page
    }

    if category == "images":
        search_params["searchType"] = "image"
    elif category == "videos":
        search_params["q"] += " site:youtube.com"
    elif category == "news":
        search_params["q"] += " site:news.google.com"

    response = requests.get(base_url, params=search_params)
    data = response.json()

    results = []
    next_start, previous_start = None, None

    if "items" in data:
        for item in data["items"]:
            result = {
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet"),
                "image": item["pagemap"]["cse_thumbnail"][0]["src"] if "pagemap" in item and "cse_thumbnail" in item["pagemap"] else None
            }
            results.append(result)

        # Pagination logic
        if "queries" in data:
            if "nextPage" in data["queries"]:
                next_start = data["queries"]["nextPage"][0]["startIndex"]
            if "previousPage" in data["queries"]:
                previous_start = data["queries"]["previousPage"][0]["startIndex"]

    return results, next_start, previous_start
