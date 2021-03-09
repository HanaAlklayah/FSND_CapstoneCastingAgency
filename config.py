import os
SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_USER = os.getenv('DB_USER', 'hana')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'Zz112233')
DB_NAME = os.getenv('DB_NAME', 'capstone')
SQLALCHEMY_DATABASE_URI = "postgres://hana@localhost:5432/capstone"
#SQLALCHEMY_DATABASE_URI = "postgres://udmpzxltmuanpe:084bcd808663331d481defbbe8b523d5f33d3a5c824a35d3c7c8c952037f396c@ec2-54-198-252-9.compute-1.amazonaws.com:5432/d89e85rrscf61l"