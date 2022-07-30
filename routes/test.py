__author__ = "Anand Pant"
__copyright__ = "Copyright (C) 2021 Anand Pant"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "anand@protrader.gg"

import json
from app import app
from flask import request


# example route
@app.route('/', methods=['GET'])
def GET_test():
    response = app.response_class(
        response=json.dumps({"test": "SUC"}),
        status=200,
        mimetype='application/json',
    )
    return response


@app.route('/v1/is/false', methods=['GET'])
def GET_v1_is_false():
    response = app.response_class(
        response=json.dumps(True),
        status=200,
        mimetype='application/json',
    )
    return response


@app.route('/v1/field/blank', methods=['GET'])
def GET_v1_field_blank():
    body = request.args

    has_params = False
    if len(body.keys()) > 0:
        has_params = True

    response = app.response_class(
        response=json.dumps(has_params),
        status=200,
        mimetype='application/json',
    )

    return response
