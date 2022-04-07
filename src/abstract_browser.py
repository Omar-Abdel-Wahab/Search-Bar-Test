from abc import ABC, abstractmethod
from selenium.webdriver.common.keys import Keys


class Browser(ABC):
    def __init__(self, driver_path):
        self._driver_path = driver_path
        self._driver = None
        self.setup_driver()

    @abstractmethod
    def setup_driver(self):
        pass

    def search(self, url, testcase):
        self.load_search_page(url)
        self.submit_query(testcase)

    def load_search_page(self, url):
        self._driver.get(url)

    def submit_query(self, testcase):
        search_bar = self._driver.find_element_by_tag_name('input')
        search_bar.clear()
        search_bar.send_keys(testcase)
        search_bar.send_keys(Keys.RETURN)
