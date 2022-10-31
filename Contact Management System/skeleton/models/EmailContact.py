from models.Contacts import Contacts


class EmailContact(Contacts):
    def __init__(self, name: str, email_address: str):
        super().__init__(name)
        self._email_address = email_address
        if len(email_address) == 0 or '@' not in email_address:
             raise ValueError('Please insert valid email address')
        self._emails: list[str] = []

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value: str):
        self._email_address = value

    @property
    def emails(self):
        return self._emails

    def add_email(self, email):
        old_email: str = self._email_address
        self._email_address = email
        self.emails.append(old_email)

    def to_string(self):
        output = f'Email contact name: {self.name}\n' \
                 f'Email address: {self._email_address}'

        return output
        # else:
        #     output = f'Email contact name: {self.name}\n' \
        #              f'Current email address: {self._email_address}\n' \
        #              f'Old emails:\n'
        #     i = 1
        #     for email in self.emails:
        #         output += f'{i}. {email}\n'
        #         i += 1
        #     return output[:output.rfind('\n')]
