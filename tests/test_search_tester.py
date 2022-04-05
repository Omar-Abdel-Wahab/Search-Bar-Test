import unittest
import urllib.parse
from src.search_tester import SearchTester
from constants.search_bar_constants import *


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.google_search_bar = SearchTester(TESTCASES_FILE_PATH, DRIVER_FILE_PATH, SITE_URL)
        self.google_search_bar.setup_driver()

    def test_google_search_bar(self):
        result_base_url = "https://www.google.com/search?q="
        self.google_search_bar.extract_testcases()
        self.google_search_bar.get_site()
        for search_bar_testcase in self.google_search_bar._testcases:
            self.google_search_bar.test_single_testcase(search_bar_testcase)
            self.assertIn(f"{result_base_url}{urllib.parse.quote_plus(search_bar_testcase)}",
                          self.google_search_bar.get_driver_current_url())

    def tearDown(self):
        self.google_search_bar.close_driver()


if __name__ == "__main__":
    unittest.main()
