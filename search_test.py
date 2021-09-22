from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def is_test_case(line):
    if line.startswith("\n") or line.startswith("#"):
        return False
    return True


with open("test_cases.txt", encoding='utf-8') as file:
    lines = file.readlines()
    test_cases = [line.rstrip() for line in lines if is_test_case(line)]
    null_indices = [index for index, keyword in enumerate(test_cases) if keyword == "Null"]
    test_cases = [test_case if test_case != "Null" else '' for test_case in test_cases]


# for test_case in test_cases:
#     print(test_case)

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.google.com")
print(driver.title)
for test_case in test_cases:
    search_bar = driver.find_element_by_name("q")
    search_bar.clear()
    search_bar.send_keys(test_case)
    search_bar.send_keys(Keys.RETURN)

# print(driver.current_url)
# driver.close()
