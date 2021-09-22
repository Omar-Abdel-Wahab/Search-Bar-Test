from selenium import webdriver
from selenium.webdriver.common.keys import Keys

test_cases = ["1", "85", "-6", "-2749", "3.14159", "0", "experiment", "Experiment", "EXPERIMENT", "experimen",
              "experimentt", "تجربة", "", "I'm working from home",
              "Lorem Ipsum simply dummy text printing typesetting industry Lorem Ipsum industry's standard dummy text "
              "ever since 1500s unknown printer took paper Contrary popular belief Lorem Ipsum simply random text "
              "piece classical Latin", "There are many variations of passages of Lorem Ipsum available, but the "
                                       "majority have suffered alteration in some form, by injected humour, "
                                       "or randomised words which don't look even slightly believable. If you are "
                                       "going to use a passage of Lorem Ipsum, you need to be sure there isn't "
                                       "anything embarrassing hidden in the middle of text. All the Lorem Ipsum "
                                       "generators on the Internet tend to repeat predefined chunks as necessary, "
                                       "making this the first true generator on the Internet",
              "asdfghjkl", "?", "q", "&", "=", "site:wikipedia.org", "@", "https://www.google.com"]
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
