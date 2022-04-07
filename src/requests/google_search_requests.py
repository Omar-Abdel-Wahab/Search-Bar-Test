from requests import get


def search(url, testcase):
    response = get(f"{url}{testcase}")
    return response
