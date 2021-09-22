from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SearchTest:
    def __init__(self, file_path, driver_path, site):
        self.file_path = file_path
        self.driver_path = driver_path
        self.site = site

    @staticmethod
    def is_testcase(line):
        if line.startswith("\n") or line.startswith("#"):
            return False
        return True

    def driver_setup(self):
        try:
            self.driver = webdriver.Chrome(self.driver_path)
        except Exception as e:
            print(e)

    def get_site(self):
        try:
            self.driver.get(self.site)
        except Exception as e:
            print(e)

    def extract_testcases(self):
        try:
            with open(self.file_path, encoding="utf-8") as file:
                lines = file.readlines()
                # Remove trailing whitespace from every testcase
                testcases = [line.rstrip() for line in lines if self.is_testcase(line)]
                # Replace "Null" keywords in the testcases.txt file with actual nulls
                self.testcases = [testcase if testcase != "Null" else "" for testcase in testcases]
        except Exception as e:
            print(e)

    def test_single_testcase(self, testcase):
        try:
            search_bar = self.driver.find_element_by_name("q")
            search_bar.clear()
            search_bar.send_keys(testcase)
            search_bar.send_keys(Keys.RETURN)
        except Exception as e:
            print(e)


def test_search_bar(search_bar):
    search_bar.driver_setup()
    search_bar.extract_testcases()
    search_bar.get_site()
    for search_bar_testcase in search_bar.testcases:
        search_bar.test_single_testcase(search_bar_testcase)
    search_bar.driver.close()


if __name__ == "__main__":

    google_bar = SearchTest("test_cases.txt", "./chromedriver.exe", "https://www.google.com")
    test_search_bar(google_bar)
