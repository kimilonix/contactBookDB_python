import sqlite3

def creat_database():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            lastname TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

creat_database()

def add_contact(name, lastname, phone):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO contacts (name, lastname, phone)
        VALUES (?, ?, ?)
    ''', (name, lastname, phone))

    conn.commit()
    conn.close()

def view_contacts():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()

    conn.close()
    return contacts

def delete_contact(contact_id):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))

    conn.commit()
    conn.close()

def main():
    creat_database()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            lastname = input("Enter lastname: ")
            phone = input("Enter phone: ")
            add_contact(name, lastname, phone)
            print("Contact added!")
        
        elif choice == '2':
            contacts = view_contacts()
            print("\nContacts:")
            for contact in contacts:
                print(f"ID: {contact[0]}, Name: {contact[1]}, Lastname: {contact[2]}, phone: {contact[3]}")
        
        elif choice == '3':
            contact_id = int(input("Enter contact ID to delete: "))
            delete_contact(contact_id)
            print("Contact deleted!")

        elif choice == '4':
            print("Exiting.")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()



