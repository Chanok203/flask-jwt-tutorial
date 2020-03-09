from app import db
from passlib.hash import pbkdf2_sha256 as sha256


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        user = cls.query.filter_by(username=username).first()
        return user

    @classmethod
    def return_all(cls):
        def to_json(u):
            return {"username": u.username, "password": u.password_hash}

        user_list = cls.query.all()
        user_list = list(map(lambda u: to_json(u), user_list))
        return {"users": user_list}

    @classmethod
    def delete_all(cls):
        try:
            num_rows_deleted = db.session.query(cls).delete()
            db.session.commit()
            return {"message": "%d row(s) deleted" % (num_rows_deleted)}
        except:
            return {"message": "Something went wrong"}

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)


class RevokedTokenModel(db.Model):
    __tablename__ = "revoked_tokens"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    jti = db.Column(db.String(120), index=True, unique=True, nullable=False)

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)
