import unittest
import urllib.parse
from search_test import *

SITE_RESULT_BASE_URL = "https://www.google.com/search?q="


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.google_bar = SearchTest(TESTCASES_FILE_PATH, WEB_DRIVER_FILE_PATH, SITE_URL)
        self.google_bar.driver_setup()

    def test_google_search_bar(self):
        self.google_bar.extract_testcases()
        self.google_bar.get_site()
        for search_bar_testcase in self.google_bar.testcases:
            self.google_bar.test_single_testcase(search_bar_testcase)
            self.assertIn(f"{SITE_RESULT_BASE_URL}{urllib.parse.quote_plus(search_bar_testcase)}",
                          self.google_bar.driver.current_url)

    def tearDown(self):
        self.google_bar.driver.close()


if __name__ == "__main__":
    unittest.main()
