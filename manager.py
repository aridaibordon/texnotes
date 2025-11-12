import shutil

from datetime import datetime
from pathlib import Path

from config import NOTES_FOLDER


def get_note_path(date: datetime) -> Path:
    return NOTES_FOLDER / date.strftime("%Y.%m.%d")


def create_note(date: datetime) -> None:
    note_path = get_note_path(date)
    note_path.mkdir(parents=True)

    template_path = NOTES_FOLDER / "template.tex"
    shutil.copy(template_path, note_path / "main.tex")


def delete_note(date: datetime) -> None:
    note_path = get_note_path(date)
    shutil.rmtree(note_path)


def clear_notes() -> None:
    """Remove auxiliary tex files from notes folder"""
    for note_path in NOTES_FOLDER.iterdir():
        if note_path.is_file() or note_path.name.startswith("."):
            continue

        for path in note_path.iterdir():
            if path.is_dir() or path.name.endswith(("bib", "pdf", "tex")):
                continue

            path.unlink()


func_map = {
    "create_note": create_note,
    "delete_note": delete_note,
    "clear_notes": clear_notes,
}
