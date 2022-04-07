from selenium import webdriver
from src.abstract_browser import Browser


class ChromeBrowser(Browser):
    def __init__(self, driver_path):
        super().__init__(driver_path)

    def setup_driver(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
