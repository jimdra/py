# 配置数据库连接
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'fk_admin'
USERNAME = 'root'
PASSWORD = ''
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 配置密钥
SECRET_KEY = 'your_secret_key'

# 配置Redis连接
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = 'password'
REDIS_URL = "redis://:{}@{}:{}/0".format(REDIS_PASSWORD, REDIS_HOST, REDIS_PORT)
