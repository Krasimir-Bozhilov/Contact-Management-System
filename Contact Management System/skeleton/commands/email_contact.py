from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class EmailContactCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        name = self.params[0]
        email = self.params[1]
        self._app_data.create_email_contact(name, email)

        return f'Email contact with name: {name} was created.'
