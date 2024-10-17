#Funcionalidades del gestor de contactos:

#Agregar un contacto: El usuario puede agregar un nuevo contacto, con información como nombre, número de teléfono y correo electrónico.

#Listar contactos: Mostrar todos los contactos guardados.

#Buscar un contacto: Permitir al usuario buscar un contacto por nombre.

#Eliminar un contacto: Eliminar un contacto existente del archivo.

#Actualizar un contacto (opcional): Modificar los detalles de un contacto ya existente.

#Recomendaciones:
#Guardar los contactos en un archivo de texto o CSV para practicar el manejo de archivos.
#Usar funciones separadas para cada funcionalidad para mejorar la modularidad y la legibilidad del código.

#pseucodigo:

# solicitar al usuario que desea realizar, agregar un contacto con informacion como nombre y numero de telefono, mostrar lista de contactos, buscar contacto, eliminar contacto, actualizar contacto.
import os 
import csv
import re

file_name = 'contact_manager_features.csv'



if not os.path.exists(file_name):
    data = [
        ['Name', 'Phone', 'Email']]
    with open(file_name, mode= 'w', newline="") as file:
        write_csv = csv.writer(file)
        write_csv.writerows(data)

#crear funcion de agregar contacto solicitar informacion al usuario, indicar si el contacto ya existe si pretende actualizarlo, si no existe mostrar que no existe.

def add():
    
    pattern = r'\(?\d{3}\)?\s?-?\d{3}-\d{4}'
    user_name = input('Enter the contact name: ').lower().strip().capitalize()
    
    no_match = True
    while no_match:
        user_phone = input('Enter the contact number phone ex (xxx) xxx-xxxx or xxx xxx-xxxx: ').strip()
        if re.findall(pattern, user_phone):
            no_match = False
        else:
            print('Format number not valid, please try again!')
    pattern = r'[\w\.-]+\@[\w|.-]+\w+'
    
    no_match = True
    while no_match:
        user_email = input('Enter the contact email: ').lower().strip()
        if re.findall(pattern, user_email):
            no_match = False
        else: 
            print('Format email not valid, please try!')
            
    with open(file_name, mode='r', newline="") as file:
        read_csv = csv.reader(file)
        
        for row in read_csv:
            
            if row[0] == user_name:
                print('This contact is already exist!')
                
                valid_option = True
                while valid_option:
                    act = input('Do you want to update this contact?: please enter Y/N: ').strip().upper()
                    if act == 'Y':
                        valid_option = False
                        print('OK')
                        return
                        
                    elif act == 'N':
                        print('Okay!')
                        valid_option = False
                        return
                    else:
                       print('Please enter a valid option!')
            
            
        info_user = [user_name, user_phone, user_email]
                
        with open(file_name, mode = 'a', newline="")as file:
                write_csv = csv.writer(file)
                write_csv.writerow(info_user)
                print('User add to list.')
               
#add()

# crear funcion de listar contactos, mostrar uno a uno los contactos

def show_contact():
    with open(file_name, mode='r', newline="")as file:
        read_csv = csv.reader(file)
        
        for row in read_csv:
            print(row)

show_contact()
# crear funcion de buscar contacto, solicitar el nombre del contacto que desea, presentarlo si se encuentra, caso contrario indicar que no existe y preguntar si desea agregarlo

def search_contact():
    user = input('Write the name you are looking for: ').lower().strip().capitalize()
    with open(file_name, mode = 'r', newline="") as file:
        read_csv = csv.reader(file)
        
        user_found = False
        for row in read_csv:
            
            if row[0] == user:
                print(f'User found: {row}')
                user_found = True
    if not user_found :
        print('User not found!')
search_contact()
            

#elminar contacto, solicitar cual contacto desea eliminar, buscar en la lista, si no existe el contacto mostrarlo, caso que si exista eliminarlo y avisar que fue eliminado.

def delete_contact():
    user = input('Write the name you want to delete: ').lower().strip().capitalize()
    with open(file_name, mode = 'r', newline="") as file:
        read_csv = csv.reader(file)
        new_list = []
        [new_list.append(row) for row in read_csv if row[0] != user]
        
        with open(file_name)
                
delete_contact()
#actualizar, preguntar que contacto desea acualizar, buscar si existe, caso que si exista preguntar que desea modificar si el telefono, el correo o ambos, caso que no exista indicarlo y preguntar si desea agregarlo.


#salir, salir del programa e indicar la salida