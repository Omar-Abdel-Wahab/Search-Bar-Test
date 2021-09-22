import unittest
import search_test
import urllib.parse


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.google_bar = search_test.SearchTest("testcases.txt", "./chromedriver.exe", "https://www.google.com")
        self.google_bar.driver_setup()

    def test_google_search_bar(self):
        self.google_bar.extract_testcases()
        self.google_bar.get_site()
        for search_bar_testcase in self.google_bar.testcases:
            self.google_bar.test_single_testcase(search_bar_testcase)
            self.assertIn(f"https://www.google.com/search?q={urllib.parse.quote_plus(search_bar_testcase)}",
                          self.google_bar.driver.current_url)

    def tearDown(self):
        self.google_bar.driver.close()


if __name__ == "__main__":
    unittest.main()
