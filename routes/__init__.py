from flask import Blueprint

routes = Blueprint('routes', __name__)

from .ds_member import *
from .ds_claim import *
from .test import *
