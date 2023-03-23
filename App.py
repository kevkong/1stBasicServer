from flask import Flask, jsonify, request, logging
import sqlite3
import sys

app = Flask(__name__)

# Create a new SQLite database and table
conn = sqlite3.connect('todos.db')
conn.execute('CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY, title TEXT NOT NULL, completed INTEGER NOT NULL)')
conn.close()

# Define the API endpoints
@app.route('/todos', methods=['GET'])
def get_todos():
    conn = sqlite3.connect('todos.db')
    cur = conn.cursor()
    cur.execute('SELECT id, title, completed FROM todos')
    todos = cur.fetchall()
    conn.close()
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    todo = request.get_json()
    conn = sqlite3.connect('todos.db')
    conn.execute('INSERT INTO todos (title, completed) VALUES (?, ?)', (todo['title'], todo['completed']))
    conn.commit()
    conn.close()
    return '', 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    conn = sqlite3.connect('todos.db')
    conn.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()
    return '', 204

@app.route('/todos/<int:todo_id>/completed', methods=['PUT'])
def mark_todo_completed(todo_id):
    conn = sqlite3.connect('todos.db')
    conn.execute('UPDATE todos SET completed = 1 WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()
    return '', 204

# Run the app
if __name__ == '__main__':
    app.run()
