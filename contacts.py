class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, email, phone, address):
        if phone in self.contacts:
            return "Error: This phone number already exists!"

        if not isinstance(name, str) or not name.strip():
            return "Error: Name must be a non-empty string."
        if not email or "@" not in email:
            return "Error: Invalid email address."
        if not phone.isdigit():
            return "Error: Phone number must be numeric."

        self.contacts[phone] = {"Name": name, "Email": email, "Address": address}
        return "Contact added successfully!"

    def view_contacts(self):
        if not self.contacts:
            return "No contacts found."
        result = []
        for phone, details in self.contacts.items():
            result.append(f"Name: {details['Name']}, Email: {details['Email']}, Phone: {phone}, Address: {details['Address']}")
        return "\n".join(result)

    def remove_contact(self, phone):
        if phone in self.contacts:
            del self.contacts[phone]
            return "Contact removed successfully!"
        return "Error: Contact not found!"

    def search_contact(self, keyword):
        results = [f"Name: {details['Name']}, Email: {details['Email']}, Phone: {phone}, Address: {details['Address']}"
                   for phone, details in self.contacts.items() if keyword.lower() in details['Name'].lower()]
        return "\n".join(results) if results else "No matches found."
