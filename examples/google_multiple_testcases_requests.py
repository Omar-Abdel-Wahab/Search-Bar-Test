from src.google_search_requests import search


def search_testcases(testcases):
    for testcase in testcases:
        search_result = search(testcase)
        print(search_result.url)
        print(search_result.ok)
        print(search_result.status_code)


if __name__ == "__main__":
    testcases_to_search = ["1", "85", "word", "wordd", "Hi there!"]
    search_testcases(testcases_to_search)
