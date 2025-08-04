__author__ = "Anand Pant"
__copyright__ = "Copyright (C) 2025 Anand Pant"
__license__ = "MIT"
__version__ = "0.0.1"


from flask import Flask

app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)
