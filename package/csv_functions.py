import csv
import os
FILE_NAME = 'contact_manager_features.csv'

#Create file CSV

#Create  file csv
def create_csv ():
    
    if not os.path.exists(FILE_NAME):
        data = [['Name', 'Phone', 'Email']]
        with open(FILE_NAME, mode= 'w', newline="") as file:
            write_csv = csv.writer(file)
            write_csv.writerows(data)
            
            
#Rewrite the file

def rewrite_csv(data):
    with open(FILE_NAME, mode= 'w', newline="") as file:
        write_csv= csv.writer(file)
        write_csv.writerows(data)
        
        
        
#Read file CSV

def read_file_csv():
    with open(FILE_NAME) as file:
        read_csv = csv.reader(file)
        return list(read_csv)
    

#Update file CSV

def update_file_csv(info_user):
    with open(FILE_NAME, mode = 'a', newline="")as file:
                write_csv = csv.writer(file)
                write_csv.writerow(info_user)
                