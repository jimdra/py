from werkzeug.datastructures import MultiDict, ImmutableMultiDict

from common.util import Captcha
from flask import Blueprint, jsonify, request, session, make_response
from werkzeug.security import check_password_hash, generate_password_hash
from common.validator import AdminForm, LoginForm
from models import Admin
from exts import db, redis_client
import shortuuid

bp = Blueprint("user", __name__, url_prefix="/users")


@bp.route("/login", methods=["POST"])
def login():
    json = request.json
    form = LoginForm(ImmutableMultiDict(json))
    if form.validate():
        return jsonify({"code": 0, "message": "登录成功", "data": form.data})
    errors = ''
    for field, error in form.errors.items():
        errors += error[0]+';'
    return jsonify({"code": 1, "message": errors, "data": {}})


@bp.route('/code')
def login_code():
    image, codes = Captcha().get_verify_code(num=4, is_base64=True)
    uid = shortuuid.uuid()
    res = make_response(jsonify({'code': 0, 'message': '', 'data': image}))
    res.set_cookie('uuid', uid, samesite='None', secure=True)
    redis_client.set(uid, codes.lower(), ex=120)
    return res


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
