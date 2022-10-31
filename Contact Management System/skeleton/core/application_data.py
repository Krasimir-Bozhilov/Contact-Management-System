from models.EmailContact import EmailContact
from models.PhoneContact import PhoneContact


class ApplicationData:
    def __init__(self):
        self._phone_contacts: list[PhoneContact] = []
        self._email_contacts: list[EmailContact] = []

    @property
    def phone_contacts(self):
        return self._phone_contacts

    @property
    def email_contacts(self):
        return self._email_contacts

    def create_phone_contact(self, name: str, phone_number: str):
        for phone_number1 in self._phone_contacts:
            if name == phone_number1.name:
                raise ValueError(f'Phone contact with name: {name} already exist!')
        new_phone = PhoneContact(name, phone_number)
        self._phone_contacts.append(new_phone)

    def create_email_contact(self, name: str, email: str):
        for email1 in self._email_contacts:
            if email1.name == name:
                raise ValueError(f'Email contact with name: {name} already exist!')
        new_email = EmailContact(name, email)
        self._email_contacts.append(new_email)

    def try_find_phone_contact_name(self, name):
        for phone_contact in self._phone_contacts:
            if phone_contact.name == name:
                return True
        return False

    def try_find_email_contact_name(self, name):
        for email_contact in self._email_contacts:
            if email_contact.name == name:
                return True
        return False

    def find_phone_contact_name(self, name):
        for phone_contact in self._phone_contacts:
            if phone_contact.name == name:
                return phone_contact
        raise ValueError(f'No phone contact with name: {name}')

    def find_email_contact_name(self, name):
        for email_contact in self._email_contacts:
            if email_contact.name == name:
                return email_contact
        raise ValueError(f'No email contact with name: {name}')

    def to_string(self):
        output = 'Phone Contacts:\n'
        if len(self._phone_contacts) == 0:
            output += 'No phone contacts.'
        else:
            for phone_contact in self._phone_contacts:
                output += '\n' + phone_contact.to_string()
        output += '\nEmail Contacts:\n'
        if len(self._email_contacts) == 0:
            output += 'No email contacts.'
        else:
            for email_contact in self._email_contacts:
                output += '\n' + email_contact.to_string()
        return "".join([s for s in output.strip().splitlines(True) if s.strip()])
    # @property
    # def shopping_cart(self) -> ShoppingCart:
    #     return self._ShoppingCart
    #
    # def find_product_by_name(self, name) -> Product:
    #     for product in self._phone_contacts:
    #         if product.name == name:
    #             return product
    #     raise ValueError('Product with that name does not exist')
    #
    # def find_category_by_name(self, name) -> Category:
    #     for category in self._email_contacts:
    #         if category.name == name:
    #             return category
    #     raise ValueError('There is no category with the given name.')
    #
    # def create_category(self, name) -> None:
    #     item = Category(name)
    #     self._email_contacts += (item,)
    #
    # def create_product(self, name, brand, price, gender) -> None:
    #     self._phone_contacts += (Product(name, brand, price, gender),)
    #
    # def category_exists(self, name) -> bool:
    #     for category in self._email_contacts:
    #         if category.name == name:
    #             return True
    #         raise ValueError('There is not a category that has the given name.')
    #
    # def product_exists(self, name) -> bool:
    #     for product in self._phone_contacts:
    #         if product.name == name:
    #             return True
    #         raise ValueError('There is not a product that has the given name.')
    #
