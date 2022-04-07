from src.google_search_requests import search

if __name__ == "__main__":
    search_result = search("something")
    print(search_result.url)
    print(search_result.ok)
    print(search_result.status_code)
