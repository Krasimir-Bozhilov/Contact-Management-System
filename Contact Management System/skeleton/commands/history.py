from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class HistoryCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        name = self._params[0]
        phone_history = self.app_data.try_find_phone_contact_name(name)
        email_history = self.app_data.try_find_email_contact_name(name)

        if phone_history and email_history:

            phone = self.app_data.find_phone_contact_name(name)
            email = self.app_data.find_email_contact_name(name)
            new_list = []
            new_list.append(phone.phone_number)
            for number in phone.phone_numbers:
                new_list.append(number)
            for email in email.emails:
                new_list.append(email)
            return f'{name} contacts: {str(new_list)}'

        elif phone_history:
            phone = self.app_data.find_phone_contact_name(name)
            new_list = []
            new_list.append(phone.phone_number)
            for number in phone.phone_numbers:
                new_list.append(number)

            return f'{name} contacts: {str(new_list)}'

        elif email_history:
            email = self.app_data.find_email_contact_name(name)
            new_list = []
            new_list.append(email.email_address)
            for email1 in email.emails:
                new_list.append(email1)

            return f'{name} contacts: {str(new_list)}'
        else:
            raise ValueError(f'No phone and email contact with name: {name}')
