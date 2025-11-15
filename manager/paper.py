import subprocess

from dataclasses import dataclass
from pathlib import Path

from config import PAPER_PATH
from registry import Registry


registry = Registry()


@dataclass
class PaperArgs:
    command: str
    name: str


def get_paper_layout(root: str) -> dict:
    return {
        root: ["create_figures.py", "main.tex", "references.bib"],
        f"{root}/data": [],
        f"{root}/figures": [],
    }


@registry.add(flags=["-c", "--create"], help="create new paper")
def create_paper(args: PaperArgs) -> None:
    path = PAPER_PATH / args.name
    layout = get_paper_layout(path.resolve())

    for folder, files in layout.items():
        path = Path(folder)
        path.mkdir(parents=True)

        for file in files:
            fpath = path / file
            fpath.touch()


@registry.add(flags=["--compile"], help="compile paper")
def compile_paper(args: PaperArgs):
    path = PAPER_PATH / args.name
    if not path.is_dir():
        raise NotADirectoryError(f"{path} is not a directory.")

    subprocess.run(
        [
            "latexmk",
            "-pdf",
            "-interaction=nonstopmode",
            f"-outdir={path}",
            str(path / "main.tex"),
        ]
    )

    subprocess.run(
        [
            "latexmk",
            "-c",
            f"-outdir={path}",
            str(path / "main.tex"),
        ]
    )
