from constants.search_bar_constants import GOOGLE_SEARCH_URL
from src.chrome_browser import ChromeBrowser

if __name__ == "__main__":
    browser = ChromeBrowser("../drivers/chrome/chromedriver.exe")
    browser.load_search_page(GOOGLE_SEARCH_URL)
    browser.search("1")
    browser.close()
