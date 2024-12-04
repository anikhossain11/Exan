from contacts import ContactBook
from file_handler import FileHandler

def main():
    contact_book = ContactBook()
    filename = "contacts.csv"
    
    # Load contacts from the file (creates the file if not present)
    contact_book.contacts = FileHandler.load_from_file(filename)

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            name = input("Enter Name: ").strip()
            email = input("Enter Email: ").strip()
            phone = input("Enter Phone Number: ").strip()
            address = input("Enter Address: ").strip()
            print(contact_book.add_contact(name, email, phone, address))
            FileHandler.save_to_file(filename, contact_book.contacts)

        elif choice == "2":
            print("\nContacts:")
            print(contact_book.view_contacts())

        elif choice == "3":
            phone = input("Enter Phone Number of the contact to remove: ").strip()
            print(contact_book.remove_contact(phone))
            FileHandler.save_to_file(filename, contact_book.contacts)

        elif choice == "4":
            keyword = input("Enter a name to search for: ").strip()
            print(contact_book.search_contact(keyword))

        elif choice == "5":
            print("Exiting the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
