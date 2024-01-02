import base64
import random
import string
from common.util import Captcha
from io import BytesIO

from flask import Blueprint, jsonify, make_response

bp = Blueprint("user", __name__, url_prefix="/users")


@bp.route("/login")
def login():
    return "Login here"


@bp.route('/code')
def login_code():
    image, codes = Captcha().get_verify_code(num=4, is_base64=True)

    return jsonify({'code': 0, 'message': '', 'data': image})
