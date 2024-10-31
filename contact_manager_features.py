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


