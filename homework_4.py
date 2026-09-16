class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number):
        return len(phone_number) == 10 and phone_number.isdigit()

class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        if not Contact.validate_phone_number(phone_number):
            raise ValueError("Номер телефона должен содержать ровно 10 цифр")
        contact = Contact(name, phone_number)
        cls.all_contacts.append(contact)

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")
print(ContactList.all_contacts)

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number)

ContactList.add_contact("John Doe", "5551234")

