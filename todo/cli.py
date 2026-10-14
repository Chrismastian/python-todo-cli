import argparse
from todo import core


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple todo list CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="Show all todos")

    p_add = sub.add_parser("add", help="Add a new todo")
    p_add.add_argument("text", help="Todo text")

    p_done = sub.add_parser("done", help="Mark a todo as done")
    p_done.add_argument("id", type=int, help="Todo ID")

    p_del = sub.add_parser("delete", help="Delete a todo")
    p_del.add_argument("id", type=int, help="Todo ID")

    args = parser.parse_args()
    todos = core.load()

    if args.command == "list":
        if not todos:
            print("(empty)")
        for t in todos:
            status = "x" if t["done"] else " "
            print(f"[{status}] {t['id']}. {t['text']}")
    elif args.command == "add":
        todos = core.add(todos, args.text)
        core.save(todos)
        print(f"Added: {args.text}")
    elif args.command == "done":
        core.done(todos, args.id)
        core.save(todos)
        print(f"Done: {args.id}")
    elif args.command == "delete":
        core.delete(todos, args.id)
        core.save(todos)
        print(f"Deleted: {args.id}")


if __name__ == "__main__":
    main()
