from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from auth.models import register_user, login_user


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/timesheetDB"
mongo = PyMongo(app)

app.mongo = mongo

@app.route('/')
def home():
    return "Welcome to the User Management System!"

@app.route('/register', methods=['POST'])
def register():
    return jsonify(register_user())  # Call the function without any arguments

@app.route('/login', methods=['POST'])
def login():
    return jsonify(login_user())  # Call the function without any arguments

if __name__ == '__main__':
    app.run(debug=True)
