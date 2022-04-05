from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
from constants.search_bar_constants import TESTCASES_FILE_PATH, DRIVER_FILE_PATH, SITE_URL


class SearchTester:
    def __init__(self, file_path, driver_path, site):
        self._file_path = file_path
        self._driver_path = driver_path
        self._site = site
        self._driver = None
        self._testcases = None
        # self._current_testcase = None

    def try_test_search_bar(self):
        try:
            self._test_search_bar()
        except Exception as e:
            self._handle_search_bar_exception(e)

    def _test_search_bar(self):
        self.setup_driver()
        self.extract_testcases()
        self.get_site()
        self.test_all_testcases()
        self.close_driver()

    @staticmethod
    def _handle_search_bar_exception(exception):
        logging.error(f'Error: {exception}', exc_info=True)
        quit()

    def setup_driver(self):
        self._driver = webdriver.Chrome(self._driver_path)

    def extract_testcases(self):
        null_keyword = "Null"
        with open(self._file_path, encoding="utf-8") as file:
            lines = file.readlines()
            # Remove trailing whitespace from every testcase
            testcases = [line.rstrip() for line in lines if self._is_testcase(line)]
            # Replace "Null" keywords in the testcases.txt file with actual nulls
            self._testcases = [testcase if testcase != null_keyword else "" for testcase in testcases]

    @staticmethod
    def _is_testcase(line):
        # Newline or a comment in the text file
        if line.startswith("\n") or line.startswith("#"):
            return False
        return True

    def get_site(self):
        self._driver.get(self._site)

    def test_all_testcases(self):
        for testcase in self._testcases:
            self.test_single_testcase(testcase)

    def test_single_testcase(self, testcase):
        query_element_name = "q"
        search_bar = self._driver.find_element_by_name(query_element_name)
        search_bar.clear()
        search_bar.send_keys(testcase)
        search_bar.send_keys(Keys.RETURN)

    def close_driver(self):
        self._driver.close()

    def get_driver_current_url(self):
        return self._driver.current_url


if __name__ == "__main__":

    google_search_bar = SearchTester(TESTCASES_FILE_PATH, DRIVER_FILE_PATH, SITE_URL)
    google_search_bar.try_test_search_bar()
