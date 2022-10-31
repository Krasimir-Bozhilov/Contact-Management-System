from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class ViewCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):

        return self.app_data.to_string()