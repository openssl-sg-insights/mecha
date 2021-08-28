__all__ = [
    "get_argument_examples",
    "get_command_examples",
]


import json
from importlib.resources import read_text

from beet import Function
from beet.core.utils import JsonDict


def get_argument_examples() -> JsonDict:
    return json.loads(read_text("mecha.resources", "argument_examples.json"))


def get_command_examples() -> Function:
    return Function(read_text("mecha.resources", "command_examples.mcfunction"))
