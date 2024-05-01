







#This script makes users in the system and gives them different groups and permissions 


import subprocess
import os
import time
import platform  


usernames_input = input("Type the names of the users you would like to add to the system with commans in between them:\n")


usernames = [name.strip() for name in usernames_input.split(',')]

for username in usernames:
    subprocess.call(['useradd','-m', username])
    
    
added_users = []


for username in usernames:
    try:
        subprocess.call(['grep', '-q', f'^{username}:' , '/etc/passwd']) 
        added_users.append(username)
    
    except subprocess.CalledProcessError:
        pass 
    
    
if added_users:
    
    print("Users added")
    
    for user in added_users:
        print(user)
        
else:
    print("No users were added") 
    


def sudofunction():
      
    
    sudoer = input("Would you like me to give sudo permissions to some of the users? yes/no:\n")

    if sudoer.lower() == 'yes':
        
        print("Please note that the user should have a password in order to use sudo. Please add password if the user doesn't have one")
        
        time.sleep(2)
        
        print(" ")
       
        whichuser = input('Which user should get those permissionss?\n:')
    
        try:
        
            subprocess.run(['usermod','-aG','wheel', whichuser], check=True)

            print("User was added to sudoers")
    
            
            
    
        except subprocess.CalledProcessError as error:
            print(f"An error occured: {error}")
    else:
    
        print("No changes made.")
    
    
sudofunction()
