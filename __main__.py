import argparse

from datetime import datetime

from manager import func_map


def main() -> None:
    parser = argparse.ArgumentParser(
        description="TexNotes: a note manager for your daily tex files."
    )
    parser.add_argument(
        "date",
        nargs="?",
        type=str,
        default=datetime.today().strftime("%d.%m.%Y"),
        help="note date in %%d.%%m.%%Y format",
    )

    flags = parser.add_mutually_exclusive_group()
    flags.add_argument(
        "-c", "--create_note", action="store_true", help="create new note"
    )
    flags.add_argument("-d", "--delete-note", action="store_true", help="delete note")
    flags.add_argument(
        "-clr", "--clear-notes", action="store_true", help="clear auxiliary tex files"
    )

    args = parser.parse_args()
    date = datetime.strptime(args.date, "%d.%m.%Y").date()

    for name, func in func_map.items():
        if getattr(args, name):
            func(date)


if __name__ == "__main__":
    main()
