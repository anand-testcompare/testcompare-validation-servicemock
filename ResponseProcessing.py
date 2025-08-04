__author__ = "Anand Pant"
__copyright__ = "Copyright (C) 2025 Anand Pant"
__license__ = "MIT"
__version__ = "0.0.1"


import json
from flask import Flask, jsonify, Response, request

class ResponseProcessing:
    def __init__(self):
        # TODO: this will be used in producing unauthorized scenarios
        self.messages = {
            "json": {
                "unauthorized": 'PROHIBITED: contact the TestCompare team to request authorization for the specified input',
                "other": 'UNKNOWN: Generic failure or unhandled operation. Contact the TestCompare team for details.',
            },
            "xml": {
                "unauthorized": '<env:Envelope xmlns:env="http://schemas.xmlsoap.org/soap/envelope/"><env:Body><env:Fault><faultcode>env:.PROHIBITED</faultcode><faultstring>contact the TestCompare team to request a contractID be added to the allowed list.</faultstring></env:Fault></env:Body></env:Envelope>',
                "other": '<env:Envelope xmlns:env="http://schemas.xmlsoap.org/soap/envelope/"><env:Body><env:Fault><faultcode>env:.UNKNOWN</faultcode><faultstring>Generic failure or unhandled operation. Contact the TestCompare team for details.</faultstring></env:Fault></env:Body></env:Envelope>',
            },
        }

    def createResponseJson(self, respObj):
        resp = Response(
            json.dumps(respObj["body"]),
            status=respObj["status_code"],
            mimetype='application/json',
        )
        return resp

    def otherError(self, form):
        if form == 'json':
            return Response(
                json.dumps(
                    {
                        "error": {
                            "code": 500,
                            "message": self.messages['json']['other'],
                        }
                    }
                ),
                status=500,
                mimetype='application/json',
            )
        else:
            return Response(
                self.messages['xml']['other'],
                status=500,
                mimetype='application/xml',
            )
