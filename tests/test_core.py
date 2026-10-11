import pytest
from pathlib import Path
from todo import core


def test_load_empty():
    """File belum ada -> list kosong."""
    result = core.load(Path("__test_tidak_ada.json"))
    assert result == []


def test_add():
    todos = []
    todos = core.add(todos, "belajar python")
    assert len(todos) == 1
    assert todos[0]["text"] == "belajar python"
    assert todos[0]["done"] is False
    assert todos[0]["id"] == 1

    todos = core.add(todos, "push repo")
    assert len(todos) == 2
    assert todos[1]["id"] == 2


def test_done():
    todos = [{"id": 1, "text": "kopi", "done": False}]
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
