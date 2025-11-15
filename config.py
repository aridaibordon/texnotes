from pathlib import Path


NOTE_PATH = Path.home() / "Documents" / "notes"
PAPER_PATH = Path.home() / "Documents" / "papers"
TEMPLATES_PATH = Path(__file__).parent / ".templates"

NOTE_TEMPLATE = TEMPLATES_PATH / "note.tex"
PAPER_TEMPLATE = TEMPLATES_PATH / "paper.tex"
