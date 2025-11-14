import argparse

from datetime import datetime
from typing import Callable, Dict

import manager


DEFAULT_COMMAND = "note"

func_map: Dict[str, Dict[str, Callable]] = {
    "note": manager.note.func_map,
    "paper": manager.paper.func_map,
}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="TexNotes: a note manager for your tex files."
    )
    subparsers = parser.add_subparsers(dest="command")

    # Daily notes manager
    note_p = subparsers.add_parser("note", help="Daily notes manager")
    note_p.add_argument(
        "date",
        nargs="?",
        type=str,
        default=datetime.today().strftime("%d.%m.%Y"),
        help="note date in %%d.%%m.%%Y format",
    )

    note_f = note_p.add_mutually_exclusive_group()
    note_f.add_argument(
        "-c",
        "--create-note",
        action="store_true",
        help="create new daily note",
    )
    note_f.add_argument(
        "-d",
        "--delete-note",
        action="store_true",
        help="delete daily note",
    )
    note_f.add_argument(
        "-clr",
        "--clear-notes",
        action="store_true",
        help="clear auxiliary tex files",
    )

    # Paper manager
    paper_p = subparsers.add_parser("paper", help="Academic papers manager")
    paper_p.add_argument("name", type=str, help="paper name")

    paper_f = paper_p.add_mutually_exclusive_group()
    paper_f.add_argument(
        "-c",
        "--create-paper",
        action="store_true",
        help="create new academic paper",
    )
    paper_f.add_argument(
        "--compile-paper",
        action="store_true",
        help="create new academic paper",
    )

    args = parser.parse_args()
    for name, func in func_map[args.command].items():
        if getattr(args, name):
            func(args)


if __name__ == "__main__":
    main()
