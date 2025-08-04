__author__ = "Anand Pant"
__copyright__ = "Copyright (C) 2025 Anand Pant"
__license__ = "MIT"
__version__ = "0.0.1"

import unittest
import requests
import json


class TestDSClaim(unittest.TestCase):
    def test_POST_v2_search_claim(self):
        url = "http://127.0.0.1:5000/v2/search/claim"

        body = {"memberId": "1"}
        data = requests.request(method="POST", json=body, url=url)
        self.assertEqual(data.status_code, 200)
        self.assertEqual(
            json.loads(data.text),
            [{"claimNumber": "abc1234", "memberId": 1,
              "claimLines": [{"line": 1, "procedureCore": "027004Z"},
                             {"line": 2, "procedureCore": "02700DZ"},
                             {"line": 3, "procedureCore": "02700TZ"}]},
             {"claimNumber": "cba4321", "memberId": 1,
              "claimLines": [{"line": 1, "procedureCore": "997004Z"},
                             {"line": 2, "procedureCore": "99700DZ"}]}],
            msg=data.text
        )
