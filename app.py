__author__ = "Anand Pant"
__copyright__ = "Copyright (C) 2021 Anand Pant"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "anand@protrader.gg"


from flask import Flask

app = Flask(__name__)

from routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
