from dataclasses import dataclass, field
from typing import Callable, List


@dataclass
class RegistryItem:
    flags: list[str]
    func: Callable
    help: str

    def __post_init__(self):
        for flag in self.flags:
            if not flag.startswith("--"):
                continue

            self.command = flag[2:].replace("-", "_")


@dataclass
class Registry:
    items: List[RegistryItem] = field(default_factory=list)

    def add(self, **kwargs):
        def wrapper(func: Callable):
            self.items.append(RegistryItem(func=func, **kwargs))

        return wrapper

    def __iter__(self):
        return iter(self.items)
