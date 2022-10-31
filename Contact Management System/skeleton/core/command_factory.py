from commands.check import CheckCommand
from commands.count import CountCommand
from commands.email_contact import EmailContactCommand
from commands.history import HistoryCommand
from commands.phone_contact import PhoneContactCommand
from commands.update_online import UpdateOnlineCommand
from commands.update_phone import UpdatePhoneCommand
from commands.view import ViewCommand


class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "phonecontact":
            return PhoneContactCommand(params, self._app_data)
        if cmd.lower() == "emailcontact":
            return EmailContactCommand(params, self._app_data)
        if cmd.lower() == "count":
            return CountCommand(params, self._app_data)
        if cmd.lower() == "check":
            return CheckCommand(params, self._app_data)
        if cmd.lower() == "updatephone":
            return UpdatePhoneCommand(params, self._app_data)
        if cmd.lower() == "updateonline":
            return UpdateOnlineCommand(params, self._app_data)
        if cmd.lower() == "history":
            return HistoryCommand(params, self._app_data)
        if cmd.lower() == "view":
            return ViewCommand(params, self._app_data)


        raise ValueError(f'Invalid command name: {cmd}!')
