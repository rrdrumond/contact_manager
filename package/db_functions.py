import sqlite3
from . import *

DB_FILE_NAME = 'contact_manager_features.db'
CONTACTS = 'contacts'
TABLE_ID = 'id'
TABLE_NAME = 'name'
TABLE_PHONE = 'phone'
TABLE_EMAIL = 'email'

def open_data_base():
    return sqlite3.connect(DB_FILE_NAME)

#Create table 

def db_create_table():
    with open_data_base() as conn:
        cursor = conn.cursor()
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {CONTACTS}(
            {TABLE_ID} INTEGER PRIMARY KEY AUTOINCREMENT,
            {TABLE_NAME} TEXT NOT NULL,
            {TABLE_PHONE} TEXT,
            {TABLE_EMAIL} TEXT)''')

#add contact 

def db_add_contact(user_name, user_phone, user_email):
    with open_data_base() as conn:
        cursor = conn.cursor()
 
        cursor.execute(f'''
            INSERT INTO {CONTACTS} ({TABLE_NAME}, {TABLE_PHONE}, {TABLE_EMAIL})
            VALUES (?, ?, ?)
            ''', (user_name, user_phone, user_email))
        conn.commit()
    
            
# Show contact list

def db_show_contact():
    with open_data_base() as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {CONTACTS}')
        for each in cursor.fetchall():
            print(each)
        
#Search specific contact
        
def db_search_contact(user):   
    with open_data_base() as conn:
        cursor = conn.cursor()
        cursor.execute(F'SELECT * FROM {CONTACTS} WHERE  {TABLE_NAME}=?', (user,) )
        result = cursor.fetchone()
        if result :
            print(result)
        else:
            print('Contact not found!')

            
            
#Delete contact 

def db_delete_contact(user):
    with open_data_base() as conn:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {CONTACTS} WHERE name =?", (user,))
        conn.commit()
    
#Update name contact

def db_update_name(user, new_name):
    with open_data_base() as conn:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {CONTACTS} SET {TABLE_NAME} = ? WHERE  {TABLE_NAME} = ?", (new_name, user,))
        conn.commit()
    

#Update phone contact

def db_update_phone(user, new_phone):
    with open_data_base() as conn:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {CONTACTS} SET {TABLE_PHONE} = ? WHERE  {TABLE_NAME} = ?", (new_phone, user))
        conn.commit()

#Update email contact

def db_update_email(user, new_email):
    with open_data_base() as conn:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {CONTACTS} SET {TABLE_EMAIL} = ? WHERE  {TABLE_NAME} =?", (new_email, user))
        conn.commit()
