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


from package.principal_functions import *
#Create document CSV

create_csv()
db_create_table()

no_exit = True

while no_exit:
    
    selection = get_selection()
    
    
    
    if selection is None:
        continue
    
    if selection == 1:
        add_contact()
        
        
    elif selection == 2:
        show_contact()
       
        
    elif selection == 3:  
        update_contact()
       
        
    elif selection == 4: 
        delete_contact()
      
    
    elif selection == 5:
        search_contact()
     
        
    elif selection == 6:
        conn = abrir_base_de_datos()
        conn.close()
        no_exit = False
        print('Exit of program ...')
        
    else:
        print('Invalid option, please try again!')


