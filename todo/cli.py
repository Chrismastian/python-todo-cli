import argparse
from todo import core


def main() -> None:
    parser = argparse.ArgumentParser(description="Todo list CLI sederhana")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="Tampilkan semua todo")

    p_add = sub.add_parser("add", help="Tambah todo baru")
    p_add.add_argument("text", help="Isi todo")

    p_done = sub.add_parser("done", help="Tandai todo selesai")
    p_done.add_argument("id", type=int, help="ID todo")

    p_del = sub.add_parser("delete", help="Hapus todo")
    p_del.add_argument("id", type=int, help="ID todo")

    args = parser.parse_args()
    todos = core.load()

    if args.command == "list":
        if not todos:
            print("(kosong)")
        for t in todos:
            status = "x" if t["done"] else " "
            print(f"[{status}] {t['id']}. {t['text']}")
    elif args.command == "add":
        todos = core.add(todos, args.text)
        core.save(todos)
        print(f"Ditambah: {args.text}")
    elif args.command == "done":
        core.done(todos, args.id)
        core.save(todos)
        print(f"Selesai: {args.id}")
    elif args.command == "delete":
        core.delete(todos, args.id)
        core.save(todos)
        print(f"Dihapus: {args.id}")


if __name__ == "__main__":
    main()
