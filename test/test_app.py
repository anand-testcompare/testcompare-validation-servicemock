__author__ = "Anand Pant"
__copyright__ = "Copyright (C) 2025 Anand Pant"
__license__ = "MIT"
__version__ = "0.0.1"


import unittest
import requests


class TestApp(unittest.TestCase):
    def test_executeTestCaseREST(self):
        url = 'http://127.0.0.1:5000/'

        data = requests.request(method='GET', url=url)
        self.assertEqual(data.status_code, 200)
        self.assertEqual(data.text, '{"test": "SUC"}')

if __name__ == '__main__':
    unittest.main()
