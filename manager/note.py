import shutil

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Callable, Dict

from config import NOTE_FOLDER, NOTE_TEMPLATE


@dataclass
class NoteArgs:
    command: str
    date: str


def get_note_path(date: datetime) -> Path:
    return NOTE_FOLDER / date.strftime("%Y.%m.%d")


def create_note(args: NoteArgs) -> None:
    date = datetime.strptime(args.date, "%d.%m.%Y").date()

    note_path = get_note_path(date)
    note_path.mkdir(parents=True)
    shutil.copy(NOTE_TEMPLATE, note_path / "main.tex")


def delete_note(args: NoteArgs) -> None:
    date = datetime.strptime(args.date, "%d.%m.%Y").date()

    note_path = get_note_path(date)
    shutil.rmtree(note_path)


def clear_notes(args: NoteArgs) -> None:
    """Remove auxiliary tex files from notes folder"""
    for note_path in NOTE_FOLDER.iterdir():
        if note_path.is_file() or note_path.name.startswith("."):
            continue

        for path in note_path.iterdir():
            if path.is_dir() or path.name.endswith(("bib", "pdf", "tex")):
                continue

            path.unlink()


func_map: Dict[str, Callable] = {
    "create_note": create_note,
    "delete_note": delete_note,
    "clear_notes": clear_notes,
}
