import unittest
from unittest.mock import patch

from constants.search_bar_constants import GOOGLE_SEARCH_URL


class TestSearch(unittest.TestCase):

    @staticmethod
    def perform_test(testcase):
        with patch('src.webdrivers.chrome_browser.ChromeBrowser') as MockBrowser:
            browser = MockBrowser.return_value
            browser.setup_driver.return_value = 'Success'
            browser.load_search_page.return_value = GOOGLE_SEARCH_URL
            browser.search.return_value = testcase
            browser.driver.title = f'{testcase} - Google Search'

            browser.search(testcase)

            assert testcase in browser.driver.title

    def test_positive_one_digit(self):
        self.perform_test("1")

    def test_positive_multi_digit(self):
        self.perform_test("85")

    def test_negative_one_digit(self):
        self.perform_test("-6")

    def test_negative_multi_digit(self):
        self.perform_test("-2749")

    def test_float(self):
        self.perform_test("3.14159")

    def test_zero(self):
        self.perform_test("0")

    def test_one_character(self):
        self.perform_test("d")

    def test_small_case_word(self):
        self.perform_test("experiment")

    def test_capital_case_word(self):
        self.perform_test("Experiment")

    def test_upper_case_word(self):
        self.perform_test("EXPERIMENT")

    def test_missing_letter_from_word(self):
        self.perform_test("experimen")

    def test_extra_letter_to_word(self):
        self.perform_test("experimentt")

    def test_different_language(self):
        self.perform_test("تجربة")

    def test_sentence(self):
        self.perform_test("I'm working from home")

    def test_paragraph_word_limit(self):
        self.perform_test("Lorem Ipsum simply dummy text printing typesetting industry Lorem Ipsum industry's standard "
                          "dummy text ever since 1500s unknown printer took paper Contrary popular belief Lorem Ipsum "
                          "simply random text piece classical Latin")

    def test_paragraph_exceeding_word_limit(self):
        self.perform_test("There are many variations of passages of Lorem Ipsum available, but the majority have "
                          "suffered alteration in some form, by injected humour, or randomised words which don't look "
                          "even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be "
                          "sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum "
                          "generators on the Internet tend to repeat predefined chunks as necessary, making this the "
                          "first true generator on the Internet ")

    def test_gibberish(self):
        self.perform_test("asdfghjkl")

    def test_query_operator(self):
        self.perform_test("?q=")

    def test_ampersand(self):
        self.perform_test("&")

    def test_word_operator(self):
        self.perform_test("site:wikipedia.org")

    def test_character_operator(self):
        self.perform_test("@wikipedia")

    def test_url(self):
        self.perform_test("https://www.google.com")

    def test_null(self):
        self.perform_test("")

    def test_url_encoding(self):
        self.perform_test("https%3A%2F%2Fwww.google.com")


if __name__ == "__main__":
    unittest.main()
