# python-todo-cli

[![CI](https://github.com/Chrismastian/python-todo-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/Chrismastian/python-todo-cli/actions/workflows/ci.yml)

A CLI todo list built while learning Python: file I/O (read/write JSON), list-of-dict data structures, `argparse`, `pytest`, and CI.

## Usage

```bash
python -m todo.cli add "learn python"
python -m todo.cli add "push repo"
python -m todo.cli list
python -m todo.cli done 1
python -m todo.cli delete 2
```

Data is stored in `todo.json` (created automatically).

## Development

```bash
pip install pytest
pytest
```

## Structure

```
todo/
  core.py   # pure logic: load/save JSON + list-of-dict operations
  cli.py    # argparse: reads terminal commands, calls core
tests/
  test_core.py
```
