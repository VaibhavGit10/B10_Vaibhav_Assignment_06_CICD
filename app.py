from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv

# Load environment variables from .env (for local dev)
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Secure MongoDB connection using environment variables
MONGO_URI = os.environ.get("MONGO_URI")  # e.g. mongodb+srv://user:pass@cluster0.mongodb.net/
DB_NAME = os.environ.get("DB_NAME", "student_db")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
students_collection = db["students"]

# Convert MongoDB ObjectId to string
def serialize_student(student):
    return {
        "_id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"]
    }

# Routes
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Student Management System API!"}), 200

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "Missing 'name' or 'age'"}), 400
    student = {
        "name": data["name"],
        "age": data["age"]
    }
    result = students_collection.insert_one(student)
    student["_id"] = str(result.inserted_id)
    return jsonify(student), 201

@app.route('/students', methods=['GET'])
def get_students():
    students = [serialize_student(s) for s in students_collection.find()]
    return jsonify(students), 200

@app.route('/students/<string:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    try:
        student = students_collection.find_one({"_id": ObjectId(student_id)})
        if student:
            return jsonify(serialize_student(student)), 200
        return jsonify({"error": "Student not found"}), 404
    except:
        return jsonify({"error": "Invalid ID format"}), 400

@app.route('/students/<string:student_id>', methods=['DELETE'])
def delete_student(student_id):
    try:
        result = students_collection.delete_one({"_id": ObjectId(student_id)})
        if result.deleted_count:
            return jsonify({"message": "Student deleted successfully"}), 200
        return jsonify({"error": "Student not found"}), 404
    except:
        return jsonify({"error": "Invalid ID format"}), 400

@app.route('/students/name/<string:name>', methods=['GET'])
def get_student_by_name(name):
    students = students_collection.find({"name": {"$regex": f".*{name}.*", "$options": "i"}})
    student_list = [serialize_student(s) for s in students]
    if student_list:
        return jsonify(student_list), 200
    return jsonify({"error": "No students found with the given name"}), 404

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK"}), 200

# Run server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
