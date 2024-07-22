from flask import Blueprint, request, jsonify
import requests
from config import Config

task_bp = Blueprint('task', __name__)

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    user_id = data['user_id']
    user_response = requests.get(f"{Config.USER_SERVICE_URL}/users/{user_id}")
    if user_response.status_code == 404:
        return jsonify({'message': 'User not found'}), 404
    # Here you would add the task creation logic
    return jsonify({'message': 'Task created'}), 201
