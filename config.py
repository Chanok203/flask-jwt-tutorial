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
