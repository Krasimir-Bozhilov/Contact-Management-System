from models.Contacts import Contacts


class PhoneContact(Contacts):
    def __init__(self, name: str, phone_number: str):
        super().__init__(name)
        self._phone_number = phone_number
        self._phone_numbers = []

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @property
    def phone_numbers(self):
        return self._phone_numbers

    def add_phone_number(self, phone_number1):
        old_number = self._phone_number
        self._phone_number = phone_number1
        self._phone_numbers.append(old_number)

    def to_string(self):

        output = f'Phone contact name: {self.name}\n' \
                 f'Phone number: {self._phone_number}'
        return output
        # else:
        #     output = f'Phone contact name: {self.name}\n' \
        #              f'Current phone number {self._phone_number}\n' \
        #              f'Old phone numbers:\n'
        #     i = 1
        #     for phone_number in self.phone_numbers:
        #         output += f'{i}. {str(phone_number)}\n'
        #         i += 1
        #     return output[:output.rfind('\n')]
