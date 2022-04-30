from constants.search_bar_constants import GOOGLE_SEARCH_URL
from src.webdrivers.chrome_browser import ChromeBrowser


def search_testcases(testcases):
    for testcase in testcases:
        browser.search(testcase)


if __name__ == "__main__":
    testcases_to_search = ["1", "85", "word", "wordd", "Hi there!"]
    browser = ChromeBrowser("../drivers/chrome/chromedriver.exe")
    browser.load_search_page(GOOGLE_SEARCH_URL)
    search_testcases(testcases_to_search)
    browser.close()
