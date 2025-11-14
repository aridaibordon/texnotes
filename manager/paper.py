import subprocess

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict

from config import PAPER_FOLDER


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


def create_paper(args: PaperArgs) -> None:
    path = PAPER_FOLDER / args.name
    layout = get_paper_layout(path.resolve())

    for folder, files in layout.items():
        path = Path(folder)
        path.mkdir(parents=True)

        for file in files:
            fpath = path / file
            fpath.touch()


def compile_paper(args: PaperArgs):
    path = PAPER_FOLDER / args.name
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


func_map: Dict[str, Callable] = {
    "create_paper": create_paper,
    "compile_paper": compile_paper,
}
