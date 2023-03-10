from rich.table import Table
from rich.box import ASCII2

from core.database.database import Database

database = Database()

# from core import database

from core.abstract.command import CommandBase
from core.logger import Logger


class Select(CommandBase):

    command = "select"
    description = "Select datas from the database"

    def init_arguments(self):
        self.parser.add_argument(
            "table",
            help="Table name",
            choices={table.full_name for table in database.tables},
        )

    def execute(self):
        data = self.database.select_data(self.arguments.table)

        if data is False:
            return Logger.warn("Table does not exist.")

        if data is []:
            return Logger.warn("Table is empty.")

        table = Table(box=ASCII2)

        table.add_column("#", style="bold bright_black")
        table.add_column("Value", style="bold green")
        table.add_column("Sub-data", style="bold magenta")

        for i, j in data.items():
            table.add_row(str(i), j.value, str(j.sub_data))

        self.console.print(table)
