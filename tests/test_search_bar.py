import unittest
from unittest.mock import patch

from constants.search_bar_constants import GOOGLE_SEARCH_URL
from src.search_bar import search


class SearchTest(unittest.TestCase):

    def test_positive_one_digit(self):
        testcase = "1"
        with patch("src.search_bar.get") as mocked_get:
            mocked_get.return_value.status_code = 200

            result = search(testcase)
            mocked_get.assert_called_with(f"{GOOGLE_SEARCH_URL}{testcase}")

            self.assertEqual(result.status_code, 200)


if __name__ == "__main__":
    unittest.main()
