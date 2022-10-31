from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class UpdatePhoneCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):

        name=self.params[0]
        phone_number = self.params[1]

        new_phone = self.app_data.find_phone_contact_name(name)
        new_phone.add_phone_number(phone_number)
        return f'Phone contact with name: {name} is updated'
