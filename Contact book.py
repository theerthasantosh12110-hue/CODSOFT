contacts = []

while True:
    print("\nCONTACT BOOK")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        contacts.append(contact)
        print("Contact added!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContacts:")
            for i in range(len(contacts)):
                print(i + 1, ".", contacts[i]["name"], "-", contacts[i]["phone"])

    elif choice == "3":
        search = input("Enter name or phone: ")
        found = False

        for contact in contacts:
            if search == contact["name"] or search == contact["phone"]:
                print("\nContact Found:")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("Address:", contact["address"])
                found = True

        if not found:
            print("Contact not found.")

    elif choice == "4":
        num = int(input("Enter contact number to update: ")) - 1

        if 0 <= num < len(contacts):
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")

            contacts[num] = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }

            print("Contact updated!")
        else:
            print("Invalid contact number.")

    elif choice == "5":
        num = int(input("Enter contact number to delete: ")) - 1

        if 0 <= num < len(contacts):
            contacts.pop(num)
            print("Contact deleted!")
        else:
            print("Invalid contact number.")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")

input("Press Enter to exit...")