from abc import ABC, abstractmethod
from selenium.webdriver.common.keys import Keys


class Browser(ABC):
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None
        self.setup_driver(driver_path)

    @abstractmethod
    def setup_driver(self, driver_path):
        pass

    def search(self, url, testcase):
        self.load_search_page(url)
        self.submit_query(testcase)

    def load_search_page(self, url):
        self.driver.get(url)

    def submit_query(self, testcase):
        search_bar = self.driver.find_element_by_tag_name('input')
        search_bar.clear()
        search_bar.send_keys(testcase)
        search_bar.send_keys(Keys.RETURN)
