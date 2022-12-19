from rich.console import Console
from typing import Literal
from core.asena_core import VARIABLES

console = Console()

class Logger:
    """Logger class for Asena-Framework"""

    SUCCESS = "+"
    ERROR = "-"
    WARNING = "!"
    INFO = "*"

    @classmethod
    def reload(cls):
        maps = {
            "litteral": ("INFO", "SUCCESS", "WARNING", "ERROR"),
            "symbols": ("*", "+", "!", "-"),
            "emojis": ("ℹ️", "✅", "⚠️", "❌"),
            "fruits": ("🫐", "🍏", "🍋", "🍎"),
            "nerdfont": ("", "", "", ""),
        }

        cls.INFO, cls.SUCCESS, cls.WARNING, cls.ERROR = maps.get(
            VARIABLES["logging-type"][0], (" ",) * 4
        )

    @classmethod
    def __log(cls, message: str, prefix: str):
        """Log a message to the console"""
        console.print(
            f"[bright_black][{prefix}][/bright_black] {message}"
        )

    @classmethod
    def info(cls, message: str) -> Literal[True]:
        """Log an info message"""
        cls.reload()
        cls.__log(message, f"[cyan]{cls.INFO}[/cyan]")
        return True

    @classmethod
    def warn(cls, message: str) -> Literal[False]:
        """Log a warning message"""
        cls.reload()
        cls.__log(message, f"[yellow]{cls.WARNING}[/yellow]")
        return False

    @classmethod
    def error(cls, message: str) -> Literal[False]:
        """Log an error message"""
        cls.reload()
        cls.__log(message, f"[red]{cls.ERROR}[/red]")
        return False

    @classmethod
    def success(cls, message: str) -> Literal[True]:
        """Log a success message"""
        cls.reload()
        cls.__log(message, f"[green]{cls.SUCCESS}[/green]")
        return True
