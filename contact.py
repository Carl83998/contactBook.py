class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []
# Display the menu function
    def add_contact(self):
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact.name} - {contact.phone_number} - {contact.email} - {contact.address}")

    def update_contact(self):
    #display current task
        self.view_contacts()
        contact_number = int(input("Enter the contact number to update: "))
        if 1 <= contact_number <= len(self.contacts):
            name = input("Enter new name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter address: ")
            self.contacts[contact_number - 1] = Contact(name, phone_number, email, address)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")

    def delete_contact(self):
        self.view_contacts()
        contact_number = int(input("Enter the contact number to delete: "))
        if 1 <= contact_number <= len(self.contacts):
            del self.contacts[contact_number - 1]
            print("Contact deleted successfully!")
        else:
            print("Invalid contact number.")
