from requests import get
from constants.search_bar_constants import GOOGLE_SEARCH_URL


def search(testcase):
    result = get(f"{GOOGLE_SEARCH_URL}{testcase}")
    return result


if __name__ == "__main__":
    search_result = search("something")
    print(search_result.url)
    print(search_result.ok)
    print(search_result.status_code)
