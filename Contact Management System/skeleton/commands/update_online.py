from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class UpdateOnlineCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        name: str = self.params[0]
        email: str = self.params[1]

        new_email = self.app_data.find_email_contact_name(name)
        new_email.add_email(email)
        return f'Email contact with name: {name} is updated'
