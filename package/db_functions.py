import sqlite3
from . import *

DB_FILE_NAME = 'contact_manager_features.db'
CONTACTS = 'contacts'
TABLE_ID = 'id'
TABLE_NAME = 'name'
TABLE_PHONE = 'phone'
TABLE_EMAIL = 'email'

def abrir_base_de_datos():
    conn = sqlite3.connect(DB_FILE_NAME)
    return conn

#Create table 

def db_create_table():
    cursor = abrir_base_de_datos()
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {CONTACTS}(
        {TABLE_ID} INTEGER PRIMARY KEY AUTOINCREMENT,
        {TABLE_NAME} TEXT NOT NULL,
        {TABLE_PHONE} TEXT,
        {TABLE_EMAIL} TEXT)''')

#add contact 

def db_add_contact(user_name, user_phone, user_email):
    conn = abrir_base_de_datos()
    cursor = conn.cursor()
    cursor.execute(f'''
    INSERT INTO {CONTACTS} ({TABLE_NAME}, {TABLE_PHONE}, {TABLE_EMAIL})
    VALUES (?, ?, ?)''', (user_name, user_phone, user_email))
    conn.commit()
    
            
# Show contact list

def db_show_contact():
    with abrir_base_de_datos() as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {CONTACTS}')
        for each in cursor.fetchall():
            print(each)
        
#Search specific contact
        
def db_search_contact(user):   
    with abrir_base_de_datos() as conn:
        cursor = conn.cursor()
        cursor.execute(F'SELECT * FROM {CONTACTS}')
    
        for each in cursor.fetchall():
            if each[1] == user:
                print(each)
            
            
#Delete contact 

def db_delete_contact(user):
    with abrir_base_de_datos() as conn:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {CONTACTS} WHERE name = '{user}'")
        conn.commit()
    
#Update name contact

def db_update_name(user, capitalize_name):
    with abrir_base_de_datos() as conn:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {CONTACTS} SET name = '{capitalize_name}' WHERE  name = '{user}'")
        conn.commit()
    

#Update phone contact

def db_update_phone(phone, user):
    with abrir_base_de_datos() as conn:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {CONTACTS} SET phone = '{phone}' WHERE  name = '{user}'")
        conn.commit()

#Update email contact

def db_update_email(email, user):
    with abrir_base_de_datos() as conn:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {CONTACTS} SET email = '{email}' WHERE  name = '{user}'")
        conn.commit()
