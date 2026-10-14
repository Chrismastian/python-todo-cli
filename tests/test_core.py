import pytest
from pathlib import Path
from todo import core


def test_load_empty():
    """File does not exist yet -> empty list."""
    result = core.load(Path("__test_missing.json"))
    assert result == []


def test_add():
    todos = []
    todos = core.add(todos, "learn python")
    assert len(todos) == 1
    assert todos[0]["text"] == "learn python"
    assert todos[0]["done"] is False
    assert todos[0]["id"] == 1

    todos = core.add(todos, "push repo")
    assert len(todos) == 2
    assert todos[1]["id"] == 2


def test_done():
    todos = [{"id": 1, "text": "coffee", "done": False}]
    core.done(todos, 1)
    assert todos[0]["done"] is True


def test_done_not_found():
    with pytest.raises(ValueError):
        core.done([], 99)


def test_delete():
    todos = [
        {"id": 1, "text": "a", "done": False},
        {"id": 2, "text": "b", "done": True},
    ]
    core.delete(todos, 1)
    assert len(todos) == 1
    assert todos[0]["id"] == 2


def test_delete_not_found():
    with pytest.raises(ValueError):
        core.delete([], 99)
