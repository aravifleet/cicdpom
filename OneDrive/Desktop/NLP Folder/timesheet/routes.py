#timesheet/routes.py

from flask import Blueprint, request, jsonify
from nlp_engine.task_handler import add_timesheet, update_timesheet, delete_timesheet, view_timesheet

timesheet_bp = Blueprint('timesheet', __name__)

@timesheet_bp.route('/add', methods=['POST'])
def add_entry():
    data = request.get_json()
    name = data.get('name')
    emp_id = data.get('emp_id')
    tasks = data.get('tasks')
    total_hours = data.get('total_hours')
    reason = data.get('reason')

    add_timesheet(name, emp_id, tasks, total_hours, reason)

    return jsonify({"message": "Timesheet entry added successfully!"}), 200

@timesheet_bp.route('/update', methods=['PUT'])
def update_entry():
    data = request.get_json()
    emp_id = data.get('emp_id')
    update_timesheet(emp_id)

    return jsonify({"message": "Timesheet entry updated successfully!"}), 200

@timesheet_bp.route('/delete', methods=['DELETE'])
def delete_entry():
    data = request.get_json()
    emp_id = data.get('emp_id')
    delete_timesheet(emp_id)

    return jsonify({"message": "Timesheet entry deleted successfully!"}), 200

@timesheet_bp.route('/view', methods=['GET'])
def view_entry():
    data = request.args
    emp_id = data.get('emp_id')
    result = view_timesheet(emp_id)

    return jsonify(result), 200
