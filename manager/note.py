import shutil

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from config import NOTE_PATH, NOTE_TEMPLATE
from registry import Registry


registry = Registry()


@dataclass
class NoteArgs:
    command: str
    date: str


def get_note_path(date: datetime) -> Path:
    return NOTE_PATH / date.strftime("%Y.%m.%d")


@registry.add(flags=["-c", "--create"], help="create new daily note")
def create_note(args: NoteArgs) -> None:
    date = datetime.strptime(args.date, "%d.%m.%Y").date()

    note_path = get_note_path(date)
    note_path.mkdir(parents=True)
    shutil.copy(NOTE_TEMPLATE, note_path / "main.tex")


@registry.add(flags=["-d", "--delete"], help="delete daily note")
def delete_note(args: NoteArgs) -> None:
    date = datetime.strptime(args.date, "%d.%m.%Y").date()

    note_path = get_note_path(date)
    shutil.rmtree(note_path)


@registry.add(flags=["-clr", "--clear"], help="clear auxiliary tex files")
def clear_notes(args: NoteArgs) -> None:
    """Remove auxiliary tex files from notes folder"""
    for note_path in NOTE_PATH.iterdir():
        if note_path.is_file() or note_path.name.startswith("."):
            continue

        for path in note_path.iterdir():
            if path.is_dir() or path.name.endswith(("bib", "pdf", "tex")):
                continue

            path.unlink()
