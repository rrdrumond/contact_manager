# contact_manager
ADD new contact, list contacts, search contact, delete contact and update or modify contact.
Contact Manager
A simple Contact Manager application using SQLite in Python. This application allows you to store, retrieve, update, and delete contact information easily.

Features
Create a Database Table: Automatically creates a table to store contact data if it doesn't already exist.
Add New Contacts: Save new contacts with name, phone number, and email.
Show All Contacts: Display a list of all saved contacts.
Search Contacts: Find a contact by name.
Update Contacts: Modify a contact's name, phone number, or email.
Delete Contacts: Remove a contact from the database.
Requirements
Python 3.x installed.
SQLite3 (usually included with Python).
Installation
Clone or download this repository.
Make sure you have Python installed, as well as the sqlite3 library (usually included by default).
Place the contact_manager_features.db file in the same directory, or the program will create it automatically.
Usage
To get started with the Contact Manager, run the Python script in your terminal or preferred Python environment.

Available Functions
Create Table: db_create_table()

Creates the contacts table if it does not exist.
Add Contact: db_add_contact(user_name, user_phone, user_email)

Adds a new contact with the specified name, phone, and email.
Show Contacts: db_show_contact()

Displays all saved contacts.
Search Contact: db_search_contact(user)

Searches for a contact by name. Displays contact details if found.
Delete Contact: db_delete_contact(user)

Deletes the contact with the specified name.
Update Contact:

Name: db_update_name(user, new_name)
Phone: db_update_phone(user, new_phone)
Email: db_update_email(user, new_email)


# Import functions from contact manager
from contact_manager import *

# Create table
db_create_table()

# Add a new contact
db_add_contact("John Doe", "123-456-7890", "johndoe@example.com")

# Show all contacts
db_show_contact()

# Search for a specific contact
db_search_contact("John Doe")

# Update contact's phone number
db_update_phone("John Doe", "987-654-3210")

# Delete a contact
db_delete_contact("John Doe")

License
This project is licensed under the MIT License.
