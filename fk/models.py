from datetime import datetime

from exts import db


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True, comment='用户名')
    nickname = db.Column(db.String(50), nullable=False, comment='昵称')
    password = db.Column(db.String(200), nullable=False, comment='密码')
    avatar = db.Column(db.String(100), nullable=True, comment='头像')
    email = db.Column(db.String(100), nullable=True, comment='邮箱')
    mobile = db.Column(db.String(11), nullable=True, comment='手机号')
    create_time = db.Column(db.DateTime, default=datetime.now(), comment='创建时间')
    update_time = db.Column(db.DateTime, nullable=True, comment='更新时间')
    login_time = db.Column(db.DateTime, nullable=True, comment='登录时间')
    status = db.Column(db.Integer, default=1, comment='状态(1:正常, 2:禁用)')
