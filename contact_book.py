

def add_contact():
    contact_name = input("Enter contact name: ").lower()
    contact_phone_number = input("Enter contact phone number: ")
    contact_email = input("Enter contact Email: ")
    new_contact = {
        "name": contact_name,
        "phone_num": contact_phone_number,
        "Email": contact_email
    }
    contacts.append(new_contact)
    print("")
    print("Contact added successfully")


def search_contact():
    if not contacts:
        print("No contacts yet")
        return
    name = input("Enter contact name: ").lower()
    for contact in contacts:
         if contact["name"] == name:
              print("Name:", contact['name'])
              print("Phone:", contact['phone_num'])
              print("Email:", contact['Email'])
              return
    print("Contact not found")
    
    
def edit_contact():
    if not contacts:
            print("No contacts yet")
            return
    name = input("Enter contact name: ").lower()
    for contact in contacts:
         if contact["name"] == name:
              print("Press Enter to keep a value, or type a new one")
              new_name = input("New name: ")
              new_phone = input("New phone: ")
              new_email = input("New Email: ")

              if new_name:
                contact["name"] = new_name
              if new_phone:
                   contact["phone_num"] = new_phone
              if new_email:
                   contact["Email"] = new_email

              print("Contact updated successfully")
              print("")
              return
    print("Contact not found")
    print("")


def delete_contact():
    if not contacts:
        print("No contacts yet")
        return
    name = input("Enter contact name: ").lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("Contact deleted")
            return
    print("Contact not found")
               
    
def view_all_contacts():
         for contact in contacts:
             print(f"Name:  {contact['name']}")
             print(f"Phone: {contact['phone_num']}")
             print(f"Email: {contact['Email']}")
             print()
         



actions = {
            "1": add_contact,
            "2": search_contact,
            "3": edit_contact,
            "4": delete_contact,
            "5": view_all_contacts
}


contacts = []

while True:

    print("")
    print("========== CONTACT BOOK ==========")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. View all contacts")
    print("6. Exit")
    print("")



    choice = input("Choose an option: ")
    print("")

    if choice in actions:
         actions[choice]()
    elif choice == "6":
        print("Goodbye")
        break
    else:
         print("Enter a valid option")


#print("Contacts")
#        for number, contact in enumerate(tasks, start=1):
#            print(f"{number}. {task['name']}")
