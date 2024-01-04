from werkzeug.datastructures import MultiDict, ImmutableMultiDict

from common.util import Captcha
from flask import Blueprint, jsonify, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from common.validator import AdminForm
from models import Admin
from exts import db

bp = Blueprint("user", __name__, url_prefix="/users")


@bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    yzm = request.json.get("code")
    if username == 'admin':
        return jsonify({'code': 0, 'message': '登录成功', 'data': {'token': '1234567890'}})

    return jsonify({'code': 1, 'message': '用户名或密码错误', 'data': {}})


@bp.route('/code')
def login_code():
    image, codes = Captcha().get_verify_code(num=4, is_base64=True)
    session['code'] = codes
    return jsonify({'code': 0, 'message': '', 'data': image})


@bp.route('/add', methods=["POST"])
def add():
    json = request.json
    form = AdminForm(ImmutableMultiDict(json))
    if form.validate():
        username = form.username.data
        nickname = form.nickname.data
        password = form.password.data
        admin = Admin(username=username, nickname=nickname, password=generate_password_hash(password))
        db.session.add(admin)
        db.session.commit()
        return jsonify({'code': 0, 'message': '添加成功', 'data': {}})
    return jsonify({'code': 1, 'message': '参数错误', 'data': form.errors})
