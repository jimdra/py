from werkzeug.datastructures import MultiDict, ImmutableMultiDict

from common.util import Captcha
from flask import Blueprint, jsonify, request, session, make_response
from werkzeug.security import check_password_hash, generate_password_hash
from common.validator import AdminForm, LoginForm
from models import Admin
from exts import db,redis_client
import shortuuid

bp = Blueprint("user", __name__, url_prefix="/users")


@bp.route("/login", methods=["POST"])
def login():
    json = request.json
    form = LoginForm(ImmutableMultiDict(json))
    if form.validate():
        return jsonify({"code": 0, "message": "登录成功"})
    return jsonify({"code": 1, "message": "登录失败", "data": form.errors})


@bp.route('/code')
def login_code():
    image, codes = Captcha().get_verify_code(num=4, is_base64=True)
    response = make_response()
    print(shortuuid.uuid())
    response.set_cookie('uuid', shortuuid.uuid())
    session['code'] = codes.lower()  # 转小写

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
