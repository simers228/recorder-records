""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper

search_val_global = ""

@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_record_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    """ recieved post requests for entry updates """
    data = request.get_json()
    try:
        if "status" in data:
            db_helper.update_status_entry(task_id)
            result = {'success': True, 'response': 'Status Updated'}
        elif "first_name" in data:
            db_helper.update_belt_entry(task_id, data)
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json()
    print("DATA: ", data)
    db_helper.insert_new_record(data['first_name'], data['last_name'], data['class_period'], data['current_belt'], data['student_teacher_id'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/")
def homepage():
    global search_val_global
    """ returns rendered homepage """
    items = []
    items = db_helper.fetch_records(search_val_global)
    search_val_global = ""
    teachers = db_helper.run_advanced_query()
    return render_template("index.html", items=items, teachers=teachers)

@app.route("/search/<path:search_val>/", methods=['POST'])
def search(search_val):
    global search_val_global
    search_val_global = search_val
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)
    return render_template("index.html")