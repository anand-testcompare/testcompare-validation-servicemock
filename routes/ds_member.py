__author__ = "Anand Pant"
__copyright__ = "Copyright (C) 2021 Anand Pant"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "anand@protrader.gg"

from flask import request
from app import app
from ResponseProcessing import ResponseProcessing
from RequestProcessing import RequestProcessing
from FileHandler import FileHandler
import json


def basic_auth_check(username, password):
    print("Username:", username)
    print("Password:", password)
    if username != "im_a_user" or password != "im_a_password":
        response = app.response_class(
            response=json.dumps({"error_message": "401 Basic Auth Check Failed: Invalid Username or Password"}),
            status=401,
            mimetype='application/json',
        )
        return response
    else:
        response = app.response_class(
            response=json.dumps({}),
            status=200,
            mimetype='application/json',
        )
        return response


# Member
@app.route('/v1/search/member', methods=['POST'])
def POST_v1_search_member():
    body = request.json

    data = FileHandler.readCSV('./data/ds_member_v1.csv')
    reqProcessing = RequestProcessing(body=body, data=data)
    respObj = reqProcessing.generateResponseFlat()

    respProcessing = ResponseProcessing()

    return respProcessing.createResponseJson(respObj=respObj)


@app.route('/v1/search/member/auth/basic', methods=['POST'])
def POST_v1_search_member_auth_basic():
    body = request.json
    data = FileHandler.readCSV('./data/ds_member_v1.csv')
    reqProcessing = RequestProcessing(body=body, data=data)
    respObj = reqProcessing.generateResponseFlatBasicAuth(authorization=request.authorization)
    respProcessing = ResponseProcessing()

    return respProcessing.createResponseJson(respObj=respObj)


@app.route('/v1/search/member/auth/xapikey', methods=['POST'])
def POST_v1_search_member_auth_xapikey():
    body = request.json
    data = FileHandler.readCSV('./data/ds_member_v1.csv')
    reqProcessing = RequestProcessing(body=body, data=data)
    respObj = reqProcessing.generateResponseFlatXAPIKey(headers=request.headers)
    respProcessing = ResponseProcessing()

    return respProcessing.createResponseJson(respObj=respObj)


@app.route('/v1/search/member', methods=['GET'])
def GET_v1_search_member():
    body = request.args

    data = FileHandler.readCSV('./data/ds_member_v1.csv')
    reqProcessing = RequestProcessing(body=body, data=data)
    respObj = reqProcessing.generateResponseFlat()

    respProcessing = ResponseProcessing()

    return respProcessing.createResponseJson(respObj=respObj)


@app.route('/v2/search/member', methods=['POST'])
def POST_v2_search_member():
    body = request.json

    reqProcessing = RequestProcessing(body=body)
    respObj = reqProcessing.generateResponseStatic(1)

    respProcessing = ResponseProcessing()

    return respProcessing.createResponseJson(respObj=respObj)
