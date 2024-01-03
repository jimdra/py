import wtforms
from wtforms.validators import DataRequired, Email, EqualTo, Length

from models import Admin


class AdminForm(wtforms.Form):
    username = wtforms.StringField(validators=[DataRequired(message="用户名不能为空")])
    nickname = wtforms.StringField(validators=[DataRequired(message="昵称不能为空")])
    password = wtforms.StringField(
        validators=[DataRequired(message="密码不能为空"), Length(min=6, max=20, message="密码长度必须介于6到20之间")])

    def validate_username(self, field):
        if Admin.query.filter_by(username=field.data).first():
            raise wtforms.ValidationError("用户名已存在")
