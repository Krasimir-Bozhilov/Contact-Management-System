from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class CheckCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        name = self._params[0]
        phone_check = self.app_data.try_find_phone_contact_name(name)
        email_check = self.app_data.try_find_email_contact_name(name)

        if phone_check and email_check:
            phone = self.app_data.find_phone_contact_name(name)
            email = self.app_data.find_email_contact_name(name)
            output = f'{phone.to_string()}\n' \
                     f'Registration date: {phone.registration_date}\n' \
                     f'{email.to_string()}\n' \
                     f'Registration date: {email.registration_date}'
            return output

        elif phone_check:
            phone = self.app_data.find_phone_contact_name(name)
            output = f'{phone.to_string()}\n' \
                     f'Registration date: {phone.registration_date}\n' \
                     f'No email contact with name: {name}'

            return output
        elif email_check:
            email = self.app_data.find_email_contact_name(name)
            output = f'{email.to_string()}\n' \
                     f'Registration date: {email.registration_date}\n' \
                     f'No phone contact with name: {name}'
            return output
        else:
            raise ValueError(f'No phone and email contact with name: {name}')
