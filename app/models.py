from app import db


class Users(db.Model):
    """ User Model """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uuid = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(100))

    # @property
    # def password(self):
    #     raise AttributeError('password: write-only field')
    #
    # @password.setter
    # def password(self, password: str):
    #     self.password = bcrypt.generate_password_hash(
    #         password).decode('utf-8')
    #
    # def check_password(self, password):
    #     return bcrypt.check_password_hash(self.password, password)

    def __repr__(self):
        return "<Users '{}'>".format(self.name)

    def serializer(self):
        return {
            'uuid': self.uuid,
            'name': self.name,
            'email': self.email
        }
