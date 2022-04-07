from src.requests.search_requests import search
from constants.search_bar_constants import GOOGLE_SEARCH_URL


def search_testcases(testcases):
    for testcase in testcases:
        response = search(GOOGLE_SEARCH_URL, testcase)
        print(response.url)
        print(response.ok)
        print(response.status_code)


if __name__ == "__main__":
    testcases_to_search = ["1", "85", "word", "wordd", "Hi there!"]
    search_testcases(testcases_to_search)
