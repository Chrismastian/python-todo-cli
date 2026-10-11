"""Logika todo: baca/tulis JSON + operasi list of dict."""
import json
from pathlib import Path

DATA_FILE = Path("todo.json")


def load(path=DATA_FILE):
    if not path.exists():
        return []
    return json.loads(path.read_text("utf-8"))

def save(todos, path=DATA_FILE):
    path.write_text(json.dumps(todos, indent=2), "utf-8")


def add(todos, text):
    next_id = max((t["id"] for t in todos), default=0) + 1
    todos.append({"id": next_id, "text": text, "done": False})
    return todos


def done(todos, todo_id):
    for t in todos:
        if t["id"] == todo_id:
            t["done"] = True
            return todos
    raise ValueError("todo tidak ditemukan")


def delete(todos, todo_id):
    for i, t in enumerate(todos):
        if t["id"] == todo_id:
            todos.pop(i)
            return todos
    raise ValueError("todo tidak ditemukan")
