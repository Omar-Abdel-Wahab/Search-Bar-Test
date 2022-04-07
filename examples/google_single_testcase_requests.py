from src.google_search_requests import search

if __name__ == "__main__":
    response = search("something")
    print(response.url)
    print(response.ok)
    print(response.status_code)
