from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class PhoneContactCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        name, phone_number = self._params
        self._app_data.create_phone_contact(name, phone_number)

        return f'Phone contact with name: {name} was created.'
