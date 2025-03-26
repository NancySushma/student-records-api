from flask import Flask, jsonify, request

app = Flask(__name__)

students = []

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    if isinstance(data, list):
        students.extend(data)
    else:
        students.append(data)

    return jsonify({'message': 'Student(s) added'}), 201

@app.route('/students/<int:index>', methods=['PUT'])
def update_student(index):
    data = request.get_json()
    students[index] = data
    return jsonify({'message': 'Student updated'})

@app.route('/students/<int:index>', methods=['DELETE'])
def delete_student(index):
    students.pop(index)
    return jsonify({'message': 'Student deleted'})

@app.route('/students', methods=['DELETE'])
def clear_students():
    students.clear()
    return jsonify({'message': 'All students deleted'})

if __name__ == '__main__':
    app.run(debug=True)