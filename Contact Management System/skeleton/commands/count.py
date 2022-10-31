from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class CountCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        return f'Number of Online contacts: {len(self.app_data.email_contacts)}\n' \
               f'Number of Phone contacts: {len(self.app_data.phone_contacts)}'