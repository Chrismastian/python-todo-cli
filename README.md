# python-todo-cli

[![CI](https://github.com/Chrismastian/python-todo-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/Chrismastian/python-todo-cli/actions/workflows/ci.yml)

Todo list berbasis CLI untuk belajar Python: file I/O (baca/tulis JSON), struktur data list of dict, `argparse`, `pytest`, dan CI.

## Cara pakai

```bash
python -m todo.cli add "belajar python"
python -m todo.cli add "push repo"
python -m todo.cli list
python -m todo.cli done 1
python -m todo.cli delete 2
```

Data disimpan di `todo.json` (dibuat otomatis).

## Development

```bash
pip install pytest
pytest
```

## Struktur

```
todo/
  core.py   # logika murni: load/save JSON + operasi list of dict
  cli.py    # argparse: baca perintah terminal, panggil core
tests/
  test_core.py
```
