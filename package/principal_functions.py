import re
import csv
from . import *
from .db_functions import *
from .csv_functions import *


            
# User selection to modify the contacts list
def get_selection():
    
    try :
        selection = int(input('Select an option in number:\n 1. Add new contact. \n 2. Show contact\'s list.\n 3. Update contact.\n 4. Delete contact. \n 5. Search contact.\n 6. Exit. : '))
        return selection
    except ValueError:
        print('Invalid input! Please enter a valid number between 1 to 6')
        return None

#User option to select what need to updated if contact exists in the list.
def get_option():    
    try:
        option = int(input('Please select in number which option you want to update: \n 1.Name.\n 2.Number phone.\n 3.Email.\n 4.Back. : '))
        return option
    except ValueError:
        print('Invalid input! Please enter a valid number between 1 to 4')
        return None
    
#Check if user, phone or email exists 

def exist_contact(user_name): 
    
    ACT = input(f'Do you want to update this contact {user_name}?: please enter Y/N: ').strip().upper()
    if ACT == 'Y':
        valid_option = False
        update_contact()
        return
                        
    elif ACT == 'N':
        valid_option = False
        get_selection()
        return
    else:
        print('Please enter a valid option!')
    
#add contact if contact not exists in the list
def add_contact():
   
    # Read csv file
    read_csv = read_file_csv()
    
    no_name= True
    while no_name:
        user_name = input('Enter the contact name: ').lower().strip().capitalize() 
        if user_name == "":
            print('No valid empty input, try again!')
            
        else:
            no_name = False
            
        
    for row in read_csv: 
        #If the list is empty continue
        if len(list(read_csv)) ==0:
            break
        #If the user in the list ask if want to update
        if row[0] == user_name:
            print('This contact is already exist!')
            # Ask user if realy wants to update contact and check
            return exist_contact(user_name)
            
        
    no_match = True
    while no_match:
        USER_PHONE = input('Enter the contact number phone ex (xxx) xxx-xxxx or xxx xxx-xxxx: ').strip()
        #Pattern number phone nice to have xxx xxx-xxxx or (xxx) xxx-xxxx
        pattern = r'\(?\d{3}\)?\s?-?\d{3}-\d{4}'
        if re.findall(pattern, USER_PHONE):
                #Read csv
                read_csv = read_file_csv()
                for each in read_csv:
                    if each[1] == USER_PHONE:
                        print(f'This phone exists whit contact {each[0]}')
                        no_match = False
                        return exist_contact(each[0])
                    else:
                        no_match = False
        else:
            print('Format number not valid, please try again!')

    no_match = True
    while no_match:
        USER_EMAIL = input('Enter the contact email: ').lower().strip()
      
        
        # Pattern to check if the input is valid email ex: name@mail.com
        pattern = r'[\w\.-]+\@[\w|.-]+\w+'
        if re.findall(pattern, USER_EMAIL):
            no_match = False
        else: 
            print('Format email not valid, please try!')
            
            
            
        info_user = [user_name, USER_PHONE, USER_EMAIL]
        
        #Update file csv       
        update_file_csv(info_user)
        print('User add to list.')
                
        #database modify
        db_add_contact(user_name, USER_PHONE, USER_EMAIL)
        

#show contacts list
def show_contact():
   
    read_csv = read_file_csv()
        
    for row in read_csv:
        print(row)
    
    #database list contact´s
    db_show_contact()        
   

#search especific contact
def search_contact():
    user = input('Write the name you are looking for: ').lower().strip().capitalize()
    #Read file csv
    read_csv = read_file_csv()
        
    #check if user exists in the list and show 
    user_found = False
    for row in read_csv:
        if row == read_csv[0]:
            pass
        if row[0] == user:
            print(f'User found: {row}')
            user_found = True
    if not user_found :
        print('User not found!')
     
    #database search and show
    db_search_contact(user) 

            
            
#Delete contact 
def delete_contact():
    user = input('Write the name you want to delete: ').lower().strip().capitalize()
    #Open csv file to read
    read_csv = read_file_csv()
    new_list = []
     
    #check if contact is in the list and ignore this contact in the new list
    user_found = False
        
    for row in read_csv:
        if row == read_csv[0]:
                pass
        if row[0] != user:
            new_list.append(row)
        elif row[0] == user:
            user_found = True
                
    #check is the contact is in the list, and ask if realy want to delete
    no_delete = True           
    while no_delete:
        
        if not user_found:
            print('The contact is not in the list!')
            no_delete = False                
        else:                
            question = input('Are you sure to delete this contact? Y/N: ').upper().strip()
            if question == 'Y':
                print('User was deleted!')
                no_delete = False
                #database delete contact
                db_delete_contact(user)
                #Write all the csv without new contact
                rewrite_csv(new_list)
                    
            elif question == 'N':
                no_delete = False
                return
            else:
                print('Option no valid, please try again!')
                
#Update contact
def update_contact():
    #Check if file exist
    create_csv()
    # Read csv file
    read_csv = read_file_csv()
    
    user = input('Write the name you want to update: ').lower().strip().capitalize()
    
    #Read csv file
    read_csv = read_file_csv()
    new_list= []

    for person in read_csv:
        new_list.append(person)
        
    for person in new_list:
            
        if person == new_list[0]:
            pass
            
        if person[0] == user:
                 
            #give options to user to modify the contact, like name, phone, email or simple back
            no_back= True
            while no_back:

                option = get_option()
                if option is None:
                    continue

                if option == 1:
                    old_name = person[0]
                    name = input('Write the new name: ').lower().strip().capitalize()
                    for row in read_csv: 
                    #If the user in the list ask if want to update
                        if row[0] == name:
                            print('This contact is already exist!')
                            # Ask user if realy wants to update contact and check
                            return exist_contact(name)
                    names = name.split(" ")
                    capitalize_name = " ".join([each.capitalize() for each in names])   
                    person[0] = capitalize_name
                    print(f'Name {old_name} change to {person[0]}, sucessufull!')
                    
                    #database update name
                    db_update_name(user,capitalize_name)
                    
                elif option == 2:

                    pattern = r'\(?\d{3}\)?\s?-?\d{3}-\d{4}'
                    no_match = True
                    while no_match:
                        old_number = person[1]
                        phone = input('Enter the new contact number phone ex.: (xxx) xxx-xxxx or xxx xxx-xxxx: ').strip()
                        if re.findall(pattern, phone):
                            no_match = False
                            person[1] = phone
                            print(f'Number {old_number}, changed to {person[1]} sucessfull')
                            #database
                            db_update_phone(phone, user)

                        else:
                            print('Format number not valid, please try again!')

                elif option == 3: 

                    pattern = r'[\w\.-]+\@[\w|.-]+\w+'
                    no_match = True
                    while no_match:
                        old_email = person[2]
                        email = input('Enter the contact email: ').lower().strip()
                        if re.findall(pattern, email):
                            no_match = False
                            person[2] = email
                            print(f'Email {old_email}, changed to {person[2]} sucessfull')
                            #database update email
                            db_update_email(email, user)
                        else: 
                            print('Format email not valid, please try!')
                                
                elif option == 4:
                    no_back = True
                    rewrite_csv(new_list)
                    return
                    
                    
                elif option not in [1,2,3]:
                    print('Option no valid, try again!')
                    
        elif person == new_list[-1]:
            if person[0] != user:
                print('Person not exists in the list!')   
        
    rewrite_csv(new_list)
        