import unittest
from src.search_bar import search


class SearchTest(unittest.TestCase):

    def test_google_search_bar(self):
        testcase = "1"
        result = search(testcase)
        self.assertEqual(result.status_code, 200)


if __name__ == "__main__":
    unittest.main()
