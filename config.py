import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):

    SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s" % (
        os.environ["MYSQL_USER"],
        os.environ["MYSQL_PASSWORD"],
        os.environ["MYSQL_HOST"],
        os.environ["MYSQL_DATABASE"],
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ["SECRET_KEY"]
    JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]

    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]

    ADMINS = ["pathompatai_c@silpakorn.edu"]
