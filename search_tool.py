from googleapiclient.discovery import build

GOOGLE_API_KEY = "A-------YOUR GOOGLE API KEY--------o"
SEARCH_ENGINE_ID = "c-------YOUR CSE ID------------"

def google_search(query, num_results=5):
    service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    res = service.cse().list(q=query, cx=SEARCH_ENGINE_ID, num=num_results).execute()
    search_items = res.get("items", [])
    
    results = []
    for item in search_items:
        results.append({
            "title": item["title"],
            "snippet": item["snippet"],
            "link": item["link"]
        })
    return results
