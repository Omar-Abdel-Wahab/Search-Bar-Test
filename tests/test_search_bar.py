import unittest
from unittest.mock import patch

from constants.search_bar_constants import GOOGLE_SEARCH_URL
from src.search_bar import search


@patch("src.search_bar.get")
class TestSearch(unittest.TestCase):

    def test_positive_one_digit(self, mocked_get):
        testcase = "1"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_positive_multi_digit(self, mocked_get):
        testcase = "85"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_negative_one_digit(self, mocked_get):
        testcase = "-6"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_negative_multi_digit(self, mocked_get):
        testcase = "-2749"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_float(self, mocked_get):
        testcase = "3.14159"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_zero(self, mocked_get):
        testcase = "0"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_one_character(self, mocked_get):
        testcase = "d"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_small_case_word(self, mocked_get):
        testcase = "experiment"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_capital_case_word(self, mocked_get):
        testcase = "Experiment"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_upper_case_word(self, mocked_get):
        testcase = "EXPERIMENT"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_missing_letter_from_word(self, mocked_get):
        testcase = "experimen"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_extra_letter_to_word(self, mocked_get):
        testcase = "experimentt"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_different_language(self, mocked_get):
        testcase = "تجربة"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_sentence(self, mocked_get):
        testcase = "I'm working from home"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_paragraph_word_limit(self, mocked_get):
        testcase = "Lorem Ipsum simply dummy text printing typesetting industry Lorem Ipsum industry's standard dummy" \
                   "text ever since 1500s unknown printer took paper Contrary popular belief Lorem Ipsum simply " \
                   "random text piece classical Latin text"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_paragraph_exceeding_word_limit(self, mocked_get):
        testcase = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered " \
                   "alteration in some form, by injected humour, or randomised words which don't look even slightly " \
                   "believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't " \
                   "anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the " \
                   "Internet tend to repeat predefined chunks as necessary, making this the first true generator on " \
                   "the Internet "
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_gibberish(self, mocked_get):
        testcase = "asdfghjkl"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_query_operator(self, mocked_get):
        testcase = "?q="
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_ampersand(self, mocked_get):
        testcase = "&"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_word_operator(self, mocked_get):
        testcase = "site:wikipedia.org"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_character_operator(self, mocked_get):
        testcase = "@wikipedia"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_url(self, mocked_get):
        testcase = "https://www.google.com"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_null(self, mocked_get):
        testcase = ""
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)

    def test_url_encoding(self, mocked_get):
        testcase = "https%3A%2F%2Fwww.google.com"
        mocked_get.return_value.status_code = 200

        result = search(testcase)

        mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")
        self.assertEqual(result.status_code, 200)


if __name__ == "__main__":
    unittest.main()
