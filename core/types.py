from typing import Type

from core.abstract.module import ModuleBase
from core.abstract.command import CommandBase

CommandType = Type[CommandBase]  # command base type
ModuleType = Type[ModuleBase]  # module base type
