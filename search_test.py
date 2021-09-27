from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging

TESTCASES_FILE_PATH = "testcases.txt"
WEB_DRIVER_FILE_PATH = "chromedriver.exe"
SITE_URL = "https://www.google.com"
QUERY_ELEMENT_NAME = "q"
NULL_KEYWORD = "Null"


class SearchTest:
    def __init__(self, file_path, driver_path, site):
        self.file_path = file_path
        self.driver_path = driver_path
        self.site = site

    @staticmethod
    def is_testcase(line):
        # Newline or a comment in the text file
        if line.startswith("\n") or line.startswith("#"):
            return False
        return True

    def driver_setup(self):
        self.driver = webdriver.Chrome(self.driver_path)

    def get_site(self):
        self.driver.get(self.site)

    def extract_testcases(self):
        with open(self.file_path, encoding="utf-8") as file:
            lines = file.readlines()
            # Remove trailing whitespace from every testcase
            testcases = [line.rstrip() for line in lines if self.is_testcase(line)]
            # Replace "Null" keywords in the testcases.txt file with actual nulls
            self.testcases = [testcase if testcase != NULL_KEYWORD else "" for testcase in testcases]

    def test_single_testcase(self, testcase):
        search_bar = self.driver.find_element_by_name(QUERY_ELEMENT_NAME)
        search_bar.clear()
        search_bar.send_keys(testcase)
        search_bar.send_keys(Keys.RETURN)

    def driver_close(self):
        self.driver.close()

    def test_search_bar(self):
        try:
            self.driver_setup()
            self.extract_testcases()
            self.get_site()
            for testcase in self.testcases:
                self.test_single_testcase(testcase)
            self.driver_close()
        except Exception as e:
            logging.error(f'Error: {e}', exc_info=True)
            quit()


if __name__ == "__main__":

    google_bar = SearchTest(TESTCASES_FILE_PATH, WEB_DRIVER_FILE_PATH, SITE_URL)
    google_bar.test_search_bar()
