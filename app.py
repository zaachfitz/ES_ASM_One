# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:21:07 2020

@author: zachf
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {
        "student_id": "100769868",
        "first_name": ["Zach"],
        "last_name": ["Fitzgerald"],
        "DOB": ["1997"],
        "amount_due": ["$2000"]
    },
    {
       "student_id": "100765643",
       "first_name": ["Bob"],
       "last_name": ["Jones"],
       "DOB": ["1999"],
       "amount_due": ["$1000"]
    }
]

@app.route('/students')
def hello():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    student = request.get_json()
    students.append(student)
    return {'id': len(students)}, 200

@app.route('/students/<int:index>', methods=['PUT'])
def update_student(index):
    student = request.get_json()
    students[index] = student
    return jsonify(students[index]), 200

@app.route('/students/<int:index>', methods=['DELETE'])
def delete_student(index):
    students.pop(index)
    return 'None', 200

app.run()