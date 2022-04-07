from requests import get
from constants.search_bar_constants import GOOGLE_SEARCH_URL


def search(testcase):
    response = get(f"{GOOGLE_SEARCH_URL}{testcase}")
    return response
