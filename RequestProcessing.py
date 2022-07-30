__author__ = "Anand Pant"
__copyright__ = "Copyright (C) 2021 Anand Pant"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "anand@protrader.gg"

import json


def listDifference(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif


def typeManipulation(output, data):
    for responseObj in output:
        for k, v in responseObj.items():
            for row in data:
                if isinstance(v, list):
                    typeManipulation(output=v, data=data)
                elif isinstance(v, dict):
                    pass
                else:
                    k = row['data']


class RequestProcessing:
    def __init__(self, body, data=[]):
        self.body = body
        self.data = data

    def generateResponseFlatBasicAuth(self, authorization):
        try:
            username = authorization["username"]
            password = authorization["password"]
        except Exception as e:
            username = ""
            password = ""
            print(e)

        print("Username:", username)
        print("Password:", password)
        if username != "im_a_user" or password != "im_a_password":
            return {
                "body": {
                    "error_message": "401 Basic Auth Check Failed: Invalid Username or Password"
                },
                "status_code": 401
            }
        else:
            return self.generateResponseFlat()

    def generateResponseFlatXAPIKey(self, headers):
        try:
            header_key = headers["x-api-key"]
        except Exception as e:
            header_key = ""
            print(e)

        print("X-API-Key:", header_key)
        if header_key != "012345abcde":
            return {
                "body": {
                    "error_message": "401 X-API-Key Check Failed: Invalid Key or Value"
                },
                "status_code": 401
            }
        else:
            return self.generateResponseFlat()

    def generateResponseFlat(self):
        # TODO: build logic to handle multiple input types
        # print(type(self.body))
        # if isinstance(self.body, dict):
        #     self.body = [self.body]
        # elif isinstance(self.body, list):
        #     return "Unhandled input type"
        try:
            bodyKeys = list(set(self.body.keys()))
            dataKeys = list(set(self.data[0].keys()))
            print(bodyKeys, dataKeys)

            differenceKeys = listDifference(bodyKeys, dataKeys)
            print(differenceKeys)
            if len(differenceKeys) >= len(dataKeys):
                return {"body": [], "status_code": 400}

            filtered = self.data

            print(self.body)
            print(self.data)

            for key, value in self.body.items():
                filtered = [x for x in filtered if x[key] == value]
            if len(filtered) == 0:
                return {"body": [], "status_code": 404}
            elif len(filtered) >= 1:
                return {"body": filtered, "status_code": 200}
        except Exception as e:
            return {"body": str(e), "status_code": 500}

    def generateResponse(self, structure={}):
        data = self.generateResponseFlat()
        body = data['body']
        # print(json.dumps(body, indent=4))
        print(structure)

        if data['status_code'] == 200:
            typeManipulation(output=structure, data=body)

        return data

    def generateResponseStatic(self, position):
        respObj = [
            {
                "body": {
                    "memberId": 1,
                    "firstName": "Billy",
                    "lastName": "Bob",
                },
                "status_code": 200,
            },
            {
                "body": {"memberId": 1, "fName": "Billy", "lName": "Bob"},
                "status_code": 200,
            },
        ]
        return respObj[position]

    def generate_response_static_claim(self):
        respObj = {
            "body": [
                {
                    "claimNumber": "abc1234",
                    "memberId": 1,
                    "claimLines": [
                        {
                            "line": 1,
                            "procedureCore": "027004Z"
                        },
                        {
                            "line": 2,
                            "procedureCore": "02700DZ"
                        },
                        {
                            "line": 3,
                            "procedureCore": "02700TZ"
                        }
                    ]
                },
                {
                    "claimNumber": "cba4321",
                    "memberId": 1,
                    "claimLines": [
                        {
                            "line": 1,
                            "procedureCore": "997004Z"
                        },
                        {
                            "line": 2,
                            "procedureCore": "99700DZ"
                        }
                    ]
                }
            ],
            "status_code": 200,
        }

        return respObj
