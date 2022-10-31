from datetime import datetime


class Contacts:
    def __init__(self, name: str):
        self._name = name
        if len(name) == 0:
            raise ValueError('Name cannot be empty!')
        self._registration_date = datetime.now()

    @property
    def name(self):
        return self._name

    @property
    def registration_date(self):
        date = self._registration_date
        date_time_str = date.strftime("%d-%m-%Y %H:%M:%S")
        return f'[{date_time_str}]'
