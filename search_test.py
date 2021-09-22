from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SearchTest:
    def __init__(self, file_path, driver_path, site):
        self.file_path = file_path
        self.driver_path = driver_path
        self.site = site

    @staticmethod
    def is_test_case(line):
        if line.startswith("\n") or line.startswith("#"):
            return False
        return True

    def driver_setup(self):
        try:
            driver = webdriver.Chrome(self.driver_path)
            driver.get(self.site)
        except Exception as e:
            print(e)
        else:
            return driver

    def extract_test_cases(self):
        try:
            with open(self.file_path, encoding="utf-8") as file:
                lines = file.readlines()
                test_cases = [line.rstrip() for line in lines if self.is_test_case(line)]
                test_cases = [test_case if test_case != "Null" else "" for test_case in test_cases]
        except Exception as e:
            print(e)
        else:
            return test_cases

    def test(self):
        driver = self.driver_setup()
        test_cases = self.extract_test_cases()
        try:
            for test_case in test_cases:
                search_bar = driver.find_element_by_name("q")
                search_bar.clear()
                search_bar.send_keys(test_case)
                search_bar.send_keys(Keys.RETURN)
            driver.close()
        except Exception as e:
            print(e)


if __name__ == "__main__":

    google_test = SearchTest("test_cases.txt", "./chromedriver.exe", "https://www.google.com")
    google_test.test()
