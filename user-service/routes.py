from flask import Blueprint, request, jsonify
from models import User, db

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({'username': user.username, 'email': user.email})
    else:
        return jsonify({'message': 'User not found'}), 404
