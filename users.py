

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
