__author__ = "Anand Pant"
__copyright__ = "Copyright (C) 2021 Anand Pant"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "anand@protrader.gg"


import unittest
import requests
import json


class TestDSMember(unittest.TestCase):
    def test_POST_v1_search_member(self):
        url = "http://127.0.0.1:5000/v1/search/member"

        body = {"memberId": "1"}
        data = requests.request(method="POST", json=body, url=url)
        print("status_code:", data.status_code)
        print("data:", data.text)

        self.assertEqual(data.status_code, 200)
        self.assertEqual(
            json.loads(data.text),
            [{"memberId": "1", "firstName": "Billy", "lastName": "Bob"}],
            msg=data.text
        )
    def test_GET_v1_search_member_SUC(self):
        url = "http://127.0.0.1:5000/v1/search/member"

        body = {"memberId": "1"}
        data = requests.request(method="GET", params=body, url=url)
        print("status_code:", data.status_code)
        print("data:", data.text)

        self.assertEqual(data.status_code, 200)
        self.assertEqual(
            json.loads(data.text),
            [{"memberId": "1", "firstName": "Billy", "lastName": "Bob"}],
            msg=data.text
        )
    def test_GET_v1_search_member_DNF(self):
        url = "http://127.0.0.1:5000/v1/search/member"

        body = {"memberId": "9"}
        data = requests.request(method="GET", params=body, url=url)
        print("status_code:", data.status_code)
        print("data:", data.text)

        self.assertEqual(data.status_code, 404)
        self.assertEqual(
            json.loads(data.text),
            [],
            msg=data.text
        )