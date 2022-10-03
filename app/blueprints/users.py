import uuid

from flask import Blueprint, request, jsonify
from app.models import Users
from app import bcrypt, db

users = Blueprint('users', __name__, url_prefix='/')


@users.route('users', methods=['GET'])
def get_list_of_users():
    data = []
    for row in Users.query.all():
        data.append(row.serializer())
    return jsonify(message='Get All Users', data=data)


@users.route('users', methods=['POST'])
def create_user():
    posted = {}
    for key, value in request.form.items():
        if key == 'password':
            posted[key] = bcrypt.generate_password_hash(password=value).decode('utf-8')
        else:
            posted[key] = value

    user = Users(uuid=str(uuid.uuid4()), name=posted['name'], email=posted['email'], password=posted['password']);

    db.session.add(user)
    db.session.commit()

    return jsonify(message='User successfully created!'), 201


@users.route('users/<uuid:id>', methods=['GET'])
def get_user_by_uuid(id):
    user = Users.query.filter_by(uuid=str(id)).first()

    if user:
        return jsonify(user.serializer()), 200

    return jsonify(message='User Not found'), 404


@users.route('users/<uuid:id>', methods=['PUT'])
def update_user_by_uuid(id):
    user = Users.query.filter_by(uuid=str(id)).first()

    if user:
        user.name = request.form['name']
        db.session.commit()

        return jsonify(message='User successfully updated!'), 200

    return jsonify(message='User Not found'), 404


@users.route('users/<uuid:id>', methods=['DELETE'])
def delete_user_by_uuid(id):
    user = Users.query.filter_by(uuid=str(id)).first()

    if user:
        db.session.delete(user)
        db.session.commit()

        return jsonify(message='User successfully deleted'), 200

    return jsonify(message='User Not found'), 404

