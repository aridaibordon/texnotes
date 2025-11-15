import argparse

from datetime import datetime
from typing import Dict

import manager

from registry import Registry


func_map: Dict[str, Registry] = {
    "note": manager.note.registry,
    "paper": manager.paper.registry,
}


def main() -> None:
    parser = argparse.ArgumentParser(
        description="TexNotes: a note manager for your tex files."
    )
    subparsers = parser.add_subparsers(dest="command")

    # Daily notes manager
    note_p = subparsers.add_parser("note", help="daily notes manager")
    note_p.add_argument(
        "date",
        nargs="?",
        type=str,
        default=datetime.today().strftime("%d.%m.%Y"),
        help="note date in %%d.%%m.%%Y format",
    )

    note_f = note_p.add_mutually_exclusive_group()
    for registry_item in manager.note.registry:
        note_f.add_argument(
            *registry_item.flags, action="store_true", help=registry_item.help
        )

    # Paper manager
    paper_p = subparsers.add_parser("paper", help="academic papers manager")
    paper_p.add_argument("name", type=str, help="paper name")

    paper_f = paper_p.add_mutually_exclusive_group()
    for registry_item in manager.note.registry:
        paper_f.add_argument(
            *registry_item.flags, action="store_true", help=registry_item.help
        )

    args = parser.parse_args()
    print(args)
    for registry_item in func_map[args.command]:
        if getattr(args, registry_item.command):
            registry_item.func(args)


if __name__ == "__main__":
    main()
