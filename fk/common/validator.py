import wtforms
from flask import request
from wtforms.validators import DataRequired, Email, EqualTo, Length
from exts import redis_client
from werkzeug.security import check_password_hash
from models import Admin


class AdminForm(wtforms.Form):
    username = wtforms.StringField(validators=[DataRequired(message="用户名不能为空")])
    nickname = wtforms.StringField(validators=[DataRequired(message="昵称不能为空")])
    password = wtforms.StringField(
        validators=[DataRequired(message="密码不能为空"), Length(min=6, max=20, message="密码长度必须介于6到20之间")])

    def validate_username(self, field):
        if Admin.query.filter_by(username=field.data).first():
            raise wtforms.ValidationError("用户名已存在")


class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[DataRequired(message="用户名不能为空")])
    password = wtforms.StringField(
        validators=[DataRequired(message="密码不能为空"), Length(min=6, max=20, message="密码长度必须介于6到20之间")])
    code = wtforms.StringField(validators=[DataRequired(message="验证码不能为空")])

    def validate_code(self, field):
        uid = request.cookies.get('uuid')
        captcha = redis_client.get(uid)
        codes = field.data
        if codes.lower() != captcha:
            raise wtforms.ValidationError("验证码错误")

    def validate_username(self, field):
        if not Admin.query.filter_by(username=field.data).first():
            raise wtforms.ValidationError("用户名不存在")

    def validate_password(self, field):
        admin = Admin.query.filter_by(username=self.username.data).first()
        if not admin or not check_password_hash(admin.password, field.data):
            raise wtforms.ValidationError("密码错误")
