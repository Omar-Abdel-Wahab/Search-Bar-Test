from src.requests.search_requests import search
from constants.search_bar_constants import GOOGLE_SEARCH_URL

if __name__ == "__main__":
    response = search(GOOGLE_SEARCH_URL, "something")
    print(response.url)
    print(response.ok)
    print(response.status_code)
