__author__ = "Anand Pant"
__copyright__ = "Copyright (C) 2025 Anand Pant"
__license__ = "MIT"
__version__ = "0.0.1"

from flask import request
from app import app
from ResponseProcessing import ResponseProcessing
from RequestProcessing import RequestProcessing
from FileHandler import FileHandler


class Claims:
    def __init__(self, claimNumber):
        self.claimNumber = claimNumber


# Claim
@app.route('/v1/search/claim', methods=['POST'])
def POST_v1_search_claim():
    body = request.json

    data = FileHandler.readCSV('./data/ds_claim_v1.csv')
    reqProcessing = RequestProcessing(body=body, data=data)

    structure = [{
        "claimNumber": ("claimNumber", str),
        "memberId": ("memberId", int),
        "claimLines": [
            {
                "line": ("claimLine", int),
                "procedureCore": ("procedureCode", str)
            }
        ]
    }]
    respObj = reqProcessing.generateResponse(structure=structure)

    respProcessing = ResponseProcessing()


@app.route('/v2/search/claim', methods=['POST'])
def POST_v2_search_claim():
    body = request.json

    reqProcessing = RequestProcessing(body=body)
    respObj = reqProcessing.generate_response_static_claim()

    respProcessing = ResponseProcessing()

    return respProcessing.createResponseJson(respObj=respObj)
